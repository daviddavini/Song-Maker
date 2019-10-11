import numpy as np
import sounddevice as sd

default_sample_rate = 44100
center_octave = 4

class Pitch:

    names = [
        ['C', 'B#'],['C#', 'Db'],['D'],['D#', 'Eb'],['E'],['E#', 'F'],
        ['F#', 'Gb'],['G'],['G#', 'Ab'],['A'],['A#', 'Bb'],['B', 'Cb']
    ]

    number_lookup = {}
    for i in range(len(names)):
        for name in names[i]:
            number_lookup[name] = i

    def __init_by_number(self, number):
        self.number = number % 12
        self.octave += (number - self.number) // 12
        self.name = self.names[self.number]

    def __init_by_name(self, name):
        self.name = name
        self.number = self.number_lookup[name]

    __init_map = {
        int : __init_by_number,
        str : __init_by_name
    }
    def __init__(self, arg, octave = center_octave):
        self.octave = octave
        self.__init_map[type(arg)](self, arg)

    def frequency(self):
        return 440 * 2**(self.number / 12) * 2**(self.octave-center_octave)

    def __repr__(self):
        return '*%s*' % (self.number)

class Note:

    def __init__(self, pitch, count):
        self.pitch = pitch
        self.count = count

    def __repr__(self):
        return repr(self.pitch)
    
    @classmethod
    def cluster(self, args_list):
        notes = []
        for pitch, *args in args_list:
            notes.append(Note(Pitch(pitch), *args))
        return notes

class SongNote:
    
    def __init__(self, start_count, note):
        self.start_count = start_count
        self.note = note
        self.end_count = start_count + note.count
    
    def start_duration(self, tempo):
        return self.start_count / (tempo / 60)

    def end_duration(self, tempo):
        return self.end_count / (tempo / 60)

    def duration(self, tempo):
        return self.note.count / (tempo / 60)

class Song:
    #TODO separate song data from song playing (song player class?)
    def __init__(self, notes = []):
        self.song_notes = []
        self.count = 0

        self.add_strand(notes)

    def duration(self, tempo):
        return self.count / (tempo / 60)

    def add_note(self, song_note):
        self.song_notes.append(song_note)
        self.count = max(self.count, song_note.end_count)

    def add_cluster(self, notes):
        for note in notes:
            self.add_note(SongNote(self.count, note))
    
    def add_strand(self, notes):
        start_count_sum = self.count
        for note in notes:
            self.add_note(SongNote(start_count_sum, note))
            start_count_sum += note.count

    def add(self, song):
        for song_note in song.song_notes:
            self.add_note(SongNote(song_note.start_count, song_note.note))
        return self

    def append(self, song):
        count = self.count
        for song_note in song.song_notes:
            self.add_note(SongNote(count + song_note.start_count, song_note.note))
        return self

    def copy(self):
        song = Song()
        song.add(self)
        return song

if __name__ == '__main__':
    note = Note(Pitch('C'), 1)
    print(note)
