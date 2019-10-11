from songmaker import song
from songmaker import samplesongs

import numpy as np
import sounddevice as sd
import abc

default_sample_rate = 44100

class Instrument (abc.ABC):
    sample_rate = default_sample_rate

    @abc.abstractclassmethod
    def perform_note(cls, note, tempo):
        pass

    @abc.abstractclassmethod
    def perform(cls, song):
        pass

class Sinewaver (Instrument):
    
    trim = 0
    tempo = 120

    @classmethod
    def perform_note(cls, song_note):
        duration = song_note.duration(cls.tempo)-cls.trim
        t = np.linspace(0, duration, cls.sample_rate * duration)
        return np.sin(song_note.note.pitch.frequency() * 2 * np.pi * t)

    @classmethod
    def perform(cls, song):
        size = int(cls.sample_rate * song.duration(cls.tempo))
        song_array = np.zeros(size)
        for song_note in song.song_notes:
            note_array = cls.perform_note(song_note)
            padded_note_array = np.zeros(size)
            start_index = int(cls.sample_rate * song_note.start_duration(cls.tempo))
            padded_note_array[start_index:start_index+note_array.size] = note_array
            song_array += padded_note_array
        return song_array

if __name__ == '__main__':
    nparray = Sinewaver.perform(samplesongs.little_lamb)
    sd.play(nparray, default_sample_rate)
    sd.wait()