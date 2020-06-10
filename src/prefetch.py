# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Prefetch(KaitaiStruct):
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
        self._raw_header = self._io.read_bytes(84)
        io = KaitaiStream(BytesIO(self._raw_header))
        self.header = self._root.FileHeader(io, self, self._root)
        self._raw_fileinformation = self._io.read_bytes(224)
        io = KaitaiStream(BytesIO(self._raw_fileinformation))
        self.fileinformation = self._root.FileInformation(io, self, self._root)
        self.metricsarray = self._root.MetricsArray(self._io, self, self._root)
        self.tracechains = self._root.TraceChainsArray(self._io, self, self._root)
        self.filenamestrings = self._root.FilenamesStrings(self._io, self, self._root)
        self._raw_volumesinformation = self._io.read_bytes(104)
        io = KaitaiStream(BytesIO(self._raw_volumesinformation))
        self.volumesinformation = self._root.VolumesInformation(io, self, self._root)

    class TraceChainsArray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def trace_chains_array(self):
            if hasattr(self, '_m_trace_chains_array'):
                return self._m_trace_chains_array if hasattr(self, '_m_trace_chains_array') else None

            _pos = self._io.pos()
            self._io.seek(self._root.fileinformation.section_b_offset)
            self._m_trace_chains_array = self._io.read_bytes((self._root.fileinformation.section_b_entries * 12))
            self._io.seek(_pos)
            return self._m_trace_chains_array if hasattr(self, '_m_trace_chains_array') else None


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
            self.section_c_length = self._io.read_u4le()
            self.section_d_offset = self._io.read_u4le()
            self.section_d_entries = self._io.read_u4le()
            self.section_d_length = self._io.read_u4le()
            self.unknown_bits_1 = self._io.read_bytes(8)
            self.last_execution_time = self._io.read_u8le()
            self.older_execution_times = [None] * (7)
            for i in range(7):
                self.older_execution_times[i] = self._io.read_u8le()

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
            pass

        @property
        def metrics_array(self):
            if hasattr(self, '_m_metrics_array'):
                return self._m_metrics_array if hasattr(self, '_m_metrics_array') else None

            _pos = self._io.pos()
            self._io.seek(self._root.fileinformation.section_a_offset)
            self._m_metrics_array = self._io.read_bytes((self._root.fileinformation.section_a_entries * 32))
            self._io.seek(_pos)
            return self._m_metrics_array if hasattr(self, '_m_metrics_array') else None


    class VolumesInformation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def extra_bits(self):
            if hasattr(self, '_m_extra_bits'):
                return self._m_extra_bits if hasattr(self, '_m_extra_bits') else None

            _pos = self._io.pos()
            self._io.seek((self._root.fileinformation.section_d_offset + 36))
            self._m_extra_bits = self._io.read_bytes(68)
            self._io.seek(_pos)
            return self._m_extra_bits if hasattr(self, '_m_extra_bits') else None

        @property
        def directory_strings_offset(self):
            if hasattr(self, '_m_directory_strings_offset'):
                return self._m_directory_strings_offset if hasattr(self, '_m_directory_strings_offset') else None

            _pos = self._io.pos()
            self._io.seek((self._root.fileinformation.section_d_offset + 28))
            self._m_directory_strings_offset = self._io.read_u4le()
            self._io.seek(_pos)
            return self._m_directory_strings_offset if hasattr(self, '_m_directory_strings_offset') else None

        @property
        def volume_serial_number(self):
            if hasattr(self, '_m_volume_serial_number'):
                return self._m_volume_serial_number if hasattr(self, '_m_volume_serial_number') else None

            _pos = self._io.pos()
            self._io.seek((self._root.fileinformation.section_d_offset + 16))
            self._m_volume_serial_number = self._io.read_bytes(4)
            self._io.seek(_pos)
            return self._m_volume_serial_number if hasattr(self, '_m_volume_serial_number') else None

        @property
        def volume_creation_time(self):
            if hasattr(self, '_m_volume_creation_time'):
                return self._m_volume_creation_time if hasattr(self, '_m_volume_creation_time') else None

            _pos = self._io.pos()
            self._io.seek((self._root.fileinformation.section_d_offset + 8))
            self._m_volume_creation_time = self._io.read_u8le()
            self._io.seek(_pos)
            return self._m_volume_creation_time if hasattr(self, '_m_volume_creation_time') else None

        @property
        def ntfs_file_ref_len(self):
            if hasattr(self, '_m_ntfs_file_ref_len'):
                return self._m_ntfs_file_ref_len if hasattr(self, '_m_ntfs_file_ref_len') else None

            _pos = self._io.pos()
            self._io.seek((self._root.fileinformation.section_d_offset + 24))
            self._m_ntfs_file_ref_len = self._io.read_u4le()
            self._io.seek(_pos)
            return self._m_ntfs_file_ref_len if hasattr(self, '_m_ntfs_file_ref_len') else None

        @property
        def volumes_device_path_len(self):
            if hasattr(self, '_m_volumes_device_path_len'):
                return self._m_volumes_device_path_len if hasattr(self, '_m_volumes_device_path_len') else None

            _pos = self._io.pos()
            self._io.seek((self._root.fileinformation.section_d_offset + 4))
            self._m_volumes_device_path_len = self._io.read_u4le()
            self._io.seek(_pos)
            return self._m_volumes_device_path_len if hasattr(self, '_m_volumes_device_path_len') else None

        @property
        def ntfs_file_ref_offset(self):
            if hasattr(self, '_m_ntfs_file_ref_offset'):
                return self._m_ntfs_file_ref_offset if hasattr(self, '_m_ntfs_file_ref_offset') else None

            _pos = self._io.pos()
            self._io.seek((self._root.fileinformation.section_d_offset + 20))
            self._m_ntfs_file_ref_offset = self._io.read_u4le()
            self._io.seek(_pos)
            return self._m_ntfs_file_ref_offset if hasattr(self, '_m_ntfs_file_ref_offset') else None

        @property
        def volumes_device_path_offset(self):
            if hasattr(self, '_m_volumes_device_path_offset'):
                return self._m_volumes_device_path_offset if hasattr(self, '_m_volumes_device_path_offset') else None

            _pos = self._io.pos()
            self._io.seek(self._root.fileinformation.section_d_offset)
            self._m_volumes_device_path_offset = self._io.read_u4le()
            self._io.seek(_pos)
            return self._m_volumes_device_path_offset if hasattr(self, '_m_volumes_device_path_offset') else None

        @property
        def directory_strings_len(self):
            if hasattr(self, '_m_directory_strings_len'):
                return self._m_directory_strings_len if hasattr(self, '_m_directory_strings_len') else None

            _pos = self._io.pos()
            self._io.seek((self._root.fileinformation.section_d_offset + 32))
            self._m_directory_strings_len = self._io.read_u4le()
            self._io.seek(_pos)
            return self._m_directory_strings_len if hasattr(self, '_m_directory_strings_len') else None

        @property
        def volume_name(self):
            if hasattr(self, '_m_volume_name'):
                return self._m_volume_name if hasattr(self, '_m_volume_name') else None

            _pos = self._io.pos()
            self._io.seek((self._root.fileinformation.section_d_offset + self._root.volumesinformation.volumes_device_path_offset))
            self._m_volume_name = self._io.read_bytes((self.volumes_device_path_len * 2))
            self._io.seek(_pos)
            return self._m_volume_name if hasattr(self, '_m_volume_name') else None


    class FilenamesStrings(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def filenames_string(self):
            if hasattr(self, '_m_filenames_string'):
                return self._m_filenames_string if hasattr(self, '_m_filenames_string') else None

            _pos = self._io.pos()
            self._io.seek(self._root.fileinformation.section_c_offset)
            self._m_filenames_string = self._io.read_bytes(self._root.fileinformation.section_c_length)
            self._io.seek(_pos)
            return self._m_filenames_string if hasattr(self, '_m_filenames_string') else None


    class FileHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.format_version = self._io.read_u4le()
            self.magic_header = self._io.read_bytes(4)
            self.unknown_bits_1 = self._io.read_bytes(4)
            self.file_size = self._io.read_u4le()
            self.file_name = (self._io.read_bytes(60)).decode(u"ASCII")
            self.prefetch_hash = self._io.read_u4le()
            self.unknown_bits_2 = self._io.read_bytes(4)



