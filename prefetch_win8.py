# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class PrefetchWin8(KaitaiStruct):
    """Windows .pf files (AKA "prefetch" file), stored under C:\Windows\Prefetch, are created
    to optimize the loading time of applications. When an application is ran, data is cached
    into the prefetch files.
    
    .. seealso::
       Source - https://en.wikipedia.org/wiki/Prefetcher
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = self._root.FileHeader(self._io, self, self._root)
        self.fileinformation = self._root.FileInformation(self._io, self, self._root)
        self._raw_metricsarray = self._io.read_bytes((self.fileinformation.section_a_entries * 32))
        io = KaitaiStream(BytesIO(self._raw_metricsarray))
        self.metricsarray = self._root.MetricsArray(io, self, self._root)
        self._raw_tracechainsarray = self._io.read_bytes((self.fileinformation.section_b_entries * 12))
        io = KaitaiStream(BytesIO(self._raw_tracechainsarray))
        self.tracechainsarray = self._root.TraceChainsArray(io, self, self._root)

    class FileHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.format_version = self._io.read_u4le()
            self.magic_header = self._io.ensure_fixed_contents(b"\x53\x43\x43\x41")
            self.unknown_bits_1 = self._io.read_bytes(4)
            self.file_size = self._io.read_u4le()
            self.file_name = (self._io.read_bytes(60)).decode(u"UTF-16LE")
            self.prefetch_hash = self._io.read_u4le()
            self.unknown_bits_2 = self._io.read_bytes(4)


    class FileInformation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.section_a_offset = self._io.read_u4le()
            self.section_a_entries = self._io.read_u4le()
            self.section_b_offset = self._io.read_u4le()
            self.section_b_entries = self._io.read_u4le()
            self.section_c_offset = self._io.read_u4le()
            self.section_c_length = self._io.read_bytes(4)
            self.section_d_offset = self._io.read_bytes(4)
            self.section_d_entries = self._io.read_bytes(4)
            self.section_d_length = self._io.read_bytes(4)
            self.unknown_bits_1 = self._io.read_bytes(8)
            self.last_execution_time = self._io.read_bytes(64)
            self.unknown_bits_2 = self._io.read_bytes(16)
            self.run_count = self._io.read_u4le()
            self.unknown_bits_3 = self._io.read_bytes(92)


    class MetricsArray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.fill = self._io.read_bytes(0)


    class TraceChainsArray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.fill = self._io.read_bytes(0)



