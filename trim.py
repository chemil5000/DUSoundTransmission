import wave
import numpy as np

w = wave.open('outRecX.wav','r')
for i in range(w.getnframes()):
    ### read 1 frame and the position will updated ###
    frame = w.readframes(1)

    all_zero = True
    for j in range(len(frame)):
        # check if amplitude is greater than 0
        if ord(frame[j]) > 100:
            print ord(frame[j])
            all_zero = False
            break

    if all_zero:
        # perform your cut here
        print 'silence found at frame %s' % w.tell()
        print 'silence found at second %s' % (w.tell()/w.getframerate())
    print np.max(ord(frame))
    print np.min(ord(frame))
    print np.mean(ord(frame))
