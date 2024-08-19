
Sanger Sequence Quality Control Script
Overview
This Python script processes .ab1 files (ABI sequence files) by converting them into .fasta and .qual formats and then trims the sequences based on a moving average of quality scores. The script outputs the processed .fasta and .qual files in specified directories, making it easier to manage and analyze Sanger sequencing data.

Features
Convert .ab1 Files: Converts .ab1 files to .fasta and .qual formats.
Trim Sequences: Trims sequences based on the moving average of quality scores.
Organized Output: Outputs files into separate directories for easy management.
Dependencies
This script requires the following Python packages:

argparse (for command-line argument parsing)
glob (for file pattern matching)
os (for directory management)
numpy (for numerical operations)
biopython (for sequence processing)
You can install the necessary packages using pip:

pip install numpy biopython


Usage
To use the script, run it from the command line with the following options:

./sanger_qc.py -i <input_directory> -o <output_directory> [-w <window_size>] [-q <quality_cutoff>]

Arguments
-i, --input_dir: (Required) Directory containing .ab1 files.
-o, --output_dir: (Required) Directory where converted and/or trimmed files will be saved.
-w, --window_size: (Optional) Size of the moving average window for quality trimming. Default is 10.
-q, --qual_cutoff: (Optional) Quality score cutoff for trimming sequences. Default is 30.0.

Output
The script generates the following subdirectories inside the specified output directory:

fasta/: Contains the converted .fasta files.
qual/: Contains the converted .qual files.
trimmed_fasta/: Contains the trimmed .fasta files.
trimmed_qual/: Contains the trimmed .qual files.
