from songmaker.song import *

notes = Note.cluster([
    (4,1),(2,1),(0,1),(2,1),
    (4,1),(4,1),(4,2),
    (2,1),(2,1),(2,2),
    (4,1),(7,1),(7,2),
    (4,1),(2,1),(0,1),(2,1),
    (4,1),(4,1),(4,1),(4,1),
    (2,1),(2,1),(4,1),(2,1),
    (0,4)
])
little_lamb_melody = Song(notes)

notes = Note.cluster([
    (0,1),(0,1),(0,1),(4,1),
    (7,1),(7,2),(7,1),
    (5,1),(4,1),(0,1),(2,1),
    (4,1),(5,1),(4,0.5),(5,0.5),(4,0.25),(5,0.25),(4,0.25),(5,0.25),
    (9,1),(11,1),(12,1),(9,1),
    (7,1.5),(4,0.5),(4,1),(4,1),
    (2,1),(5,0.5),(4,0.5),(2,1.5),(-1,0.5),
    (0,4)
])
little_lamb_countermelody = Song(notes)

little_lamb_both = little_lamb_melody.copy().add(little_lamb_countermelody)

little_lamb = little_lamb_melody.copy().append(little_lamb_countermelody).append(little_lamb_both)
