from songmaker import instrument
from songmaker import samplesongs
from songmaker import song

import sounddevice as sd

if __name__ == "__main__":
    nparray = instrument.Sinewaver.perform(samplesongs.little_lamb)
    sd.play(nparray, instrument.default_sample_rate)
    sd.wait()