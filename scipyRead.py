import numpy as np
from numpy import (asarray, iscomplexobj, sinc)
import wave
import struct
import sys

_big_endian = False
WAVE_FORMAT_PCM = 0x0001
WAVE_FORMAT_IEEE_FLOAT = 0x0003
WAVE_FORMAT_EXTENSIBLE = 0xfffe
KNOWN_WAVE_FORMATS = (WAVE_FORMAT_PCM, WAVE_FORMAT_IEEE_FLOAT)


# True if we are running on Python 3.
PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str
else:
    string_types = basestring

def _read_fmt_chunk(fid):
    if _big_endian:
        fmt = '>'
    else:
        fmt = '<'
    res = struct.unpack(fmt+'iHHIIHH',fid.read(20))
    size, comp, noc, rate, sbytes, ba, bits = res
    if comp not in KNOWN_WAVE_FORMATS or size > 16:
        comp = WAVE_FORMAT_PCM
        warnings.warn("Unknown wave file format", WavFileWarning)
        if size > 16:
            fid.read(size - 16)

    return size, comp, noc, rate, sbytes, ba, bits


def _read_riff_chunk(fid):
    global _big_endian
    str1 = fid.read(4)
    if str1 == b'RIFX':
        _big_endian = True
    elif str1 != b'RIFF':
        raise ValueError("Not a WAV file.")
    if _big_endian:
        fmt = '>I'
    else:
        fmt = '<I'
    fsize = struct.unpack(fmt, fid.read(4))[0] + 8
    str2 = fid.read(4)
    if (str2 != b'WAVE'):
        raise ValueError("Not a WAV file.")
    if str1 == b'RIFX':
        _big_endian = True
    return fsize

# assumes file pointer is immediately
#   after the 'data' id
def _read_data_chunk(fid, comp, noc, bits, mmap=False):
    if _big_endian:
        fmt = '>i'
    else:
        fmt = '<i'
    size = struct.unpack(fmt,fid.read(4))[0]

    bytes = bits//8
    if bits == 8:
        dtype = 'u1'
    else:
        if _big_endian:
            dtype = '>'
        else:
            dtype = '<'
        if comp == 1:
            dtype += 'i%d' % bytes
        else:
            dtype += 'f%d' % bytes
    if not mmap:
        data = np.fromstring(fid.read(size), dtype=dtype)
    else:
        start = fid.tell()
        data = np.memmap(fid, dtype=dtype, mode='c', offset=start,
                            shape=(size//bytes,))
        fid.seek(start + size)

    if noc > 1:
        data = data.reshape(-1,noc)
    return data


def read(filename, mmap=False):
    
    if hasattr(filename,'read'):
        fid = filename
        mmap = False
    else:
        fid = open(filename, 'rb')

    try:
        fsize = _read_riff_chunk(fid)
        noc = 1
        bits = 8
        comp = WAVE_FORMAT_PCM
        while (fid.tell() < fsize):
            # read the next chunk
            chunk_id = fid.read(4)
            if chunk_id == b'fmt ':
                size, comp, noc, rate, sbytes, ba, bits = _read_fmt_chunk(fid)
            elif chunk_id == b'fact':
                _skip_unknown_chunk(fid)
            elif chunk_id == b'data':
                data = _read_data_chunk(fid, comp, noc, bits, mmap=mmap)
            elif chunk_id == b'LIST':
                # Someday this could be handled properly but for now skip it
                _skip_unknown_chunk(fid)
            else:
                warnings.warn("Chunk (non-data) not understood, skipping it.",
                              WavFileWarning)
                _skip_unknown_chunk(fid)
    finally:
        if not hasattr(filename,'read'):
            fid.close()
        else:
            fid.seek(0)

    return rate, data

