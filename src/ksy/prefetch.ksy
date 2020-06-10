meta:
   id: prefetch
   title: Windows 8 prefetch file 
   file-extension: pf
   endian: le
doc: |
   Windows .pf files (AKA "prefetch" file), stored under C:\Windows\Prefetch, are created
   to optimize the loading time of applications. When an application is ran, data is cached
   into the prefetch files.
doc-ref: 'https://en.wikipedia.org/wiki/Prefetcher'
seq:
  - id: header
    type: file_header
    size: 84
  - id: fileinformation
    type: file_information
    size: 224
  - id: metricsarray
    type: metrics_array
  - id: tracechains
    type: trace_chains_array
  - id: filenamestrings
    type: filenames_strings
  - id: volumesinformation
    type: volumes_information
    size: 104
types:
  file_header:
    seq:
      - id: format_version
        type: u4
        doc: |
          Format Version 26 is Windows 8.1
      - id: magic_header
        size: 4
      - id: unknown_bits_1
        size: 4
      - id: file_size
        type: u4
      - id: file_name
        type: str
        size: 60
        encoding: ASCII
      - id: prefetch_hash
        type: u4
      - id: unknown_bits_2
        size: 4
  file_information:
    seq:
      - id: section_a_offset
        type: u4
      - id: section_a_entries
        type: u4
      - id: section_b_offset
        type: u4
      - id: section_b_entries
        type: u4
      - id: section_c_offset
        type: u4
      - id: section_c_length
        type: u4
      - id: section_d_offset
        type: u4
      - id: section_d_entries
        type: u4
      - id: section_d_length
        type: u4
      - id: unknown_bits_1
        size: 8
      - id: last_execution_time
        type: u8
      - id: older_execution_times
        type: u8
        repeat: expr
        repeat-expr: 7
      - id: unknown_bits_2
        size: 16
      - id: run_count
        type: u4
      - id: unknown_bits_3
        size: 92
  metrics_array:
    instances:
      metrics_array:
        pos: _root.fileinformation.section_a_offset
        size: _root.fileinformation.section_a_entries * 32
  trace_chains_array:
    instances:
      trace_chains_array:
        pos: _root.fileinformation.section_b_offset
        size: _root.fileinformation.section_b_entries * 12
  filenames_strings:
    instances:
      filenames_string:
        pos: _root.fileinformation.section_c_offset
        size: _root.fileinformation.section_c_length
  volumes_information:
    instances:
      volumes_device_path_offset:
        pos: _root.fileinformation.section_d_offset
        type: u4
      volumes_device_path_len:
        pos: _root.fileinformation.section_d_offset + 4
        type: u4
      volume_creation_time:
        pos: _root.fileinformation.section_d_offset + 8
        type: u8
      volume_serial_number:
        pos: _root.fileinformation.section_d_offset + 16
        size: 4
      ntfs_file_ref_offset:
        pos: _root.fileinformation.section_d_offset + 20
        type: u4
      ntfs_file_ref_len:
        pos: _root.fileinformation.section_d_offset + 24
        type: u4
      directory_strings_offset:
        pos: _root.fileinformation.section_d_offset + 28
        type: u4       
      directory_strings_len:
        pos: _root.fileinformation.section_d_offset + 32
        type: u4  
      extra_bits:
        pos: _root.fileinformation.section_d_offset + 36
        size: 68
      volume_name:
        pos: _root.fileinformation.section_d_offset + _root.volumesinformation.volumes_device_path_offset
        size: volumes_device_path_len * 2
