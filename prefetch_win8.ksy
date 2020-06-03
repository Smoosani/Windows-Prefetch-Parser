meta:
   id: prefetch_win8
   title: Windows 8.1 prefetch file 
   file-extension: lnk
   endian: le
doc: |
   Windows .pf files (AKA "prefetch" file), stored under C:\Windows\Prefetch, are created
   to optimize the loading time of applications. When an application is ran, data is cached
   into the prefetch files.
doc-ref: 'https://en.wikipedia.org/wiki/Prefetcher'
seq:
  - id: header
    type: file_header
  - id: fileinformation
    type: file_information
  - id: metricsarray
    type: metrics_array
    size: fileinformation.section_a_entries * 32
  - id: tracechainsarray
    type: trace_chains_array
    size: fileinformation.section_b_entries * 12
types:
  file_header:
    seq:
      - id: format_version
        type: u4
        doc: |
          Format Version 26 is Windows 8
      - id: magic_header
        contents: [0x53, 0x43, 0x43, 0x41]
      - id: unknown_bits_1
        size: 4
      - id: file_size
        type: u4
      - id: file_name
        type: str
        size: 60
        encoding: UTF-16LE
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
        size: 4
      - id: section_d_offset
        size: 4
      - id: section_d_entries
        size: 4
      - id: section_d_length
        size: 4
      - id: unknown_bits_1
        size: 8
      - id: last_execution_time
        size: 64
      - id: unknown_bits_2
        size: 16
      - id: run_count
        type: u4
      - id: unknown_bits_3
        size: 92
  metrics_array:
    seq:
      - id: fill
        size: 0
  trace_chains_array:
    seq:
      - id: fill
        size: 0
