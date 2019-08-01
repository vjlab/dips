# DIPs.  Defective interfering particles project.

Identify defective particles across different virus, segmented and no-segmented (flu,dengue,RSV, etc).

### Folders' map

- `src/`: Code folder containing snakemake pipelines:
  - `DIPipe.snk`. It runs a INDEL Aware aligner (STAR) and DI-tector 0.6 (https://www.ncbi.nlm.nih.gov/pubmed/30012569) to identify the DIPs. To perform the alignments it requires a single reference.
  - `DIPipe_multiref.snk`. Same as `DIPipe.snk` but it requires one reference per each sample.
  - `DIPipe_multirefPaired.snk`. Same as `DIPipe_multiref.snk` but input raw data is paired.
  - `assembly_DENGUE.snk`. Generate consensus sequences from raw data of no-segmented virus.
