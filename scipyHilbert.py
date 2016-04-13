import numpy as np
from numpy import (asarray, iscomplexobj, sinc)

def hilbert(x, N=None, axis=-1):
    x = asarray(x)
    if iscomplexobj(x):
        raise ValueError("x must be real.")
    if N is None:
        N = x.shape[axis]
    if N <= 0:
        raise ValueError("N must be positive.")

    Xf = np.fft.fft(x, N, axis=axis)
    h = np.zeros(N)
    if N % 2 == 0:
        h[0] = h[N // 2] = 1
        h[1:N // 2] = 2
    else:
        h[0] = 1
        h[1:(N + 1) // 2] = 2

    if len(x.shape) > 1:
        ind = [newaxis] * x.ndim
        ind[axis] = slice(None)
        h = h[ind]
    x = np.fft.ifft(Xf * h, axis=axis)
    return x

