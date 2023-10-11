from psonic import *

number_of_pieces = 8

for i in range(16):
    s = random.randrange(0,number_of_pieces)/number_of_pieces #sample starts at 0.0 and finishes at 1.0
    f = s + (1.0/number_of_pieces)
    sample(LOOP_AMEN,beat_stretch=2,start=s,finish=f)
    sleep(2.0/number_of_pieces)