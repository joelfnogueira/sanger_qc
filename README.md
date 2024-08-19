🧬 sanger_qc
>A Python script for converting .ab1 files to .fasta and .qual, and trimming sequences based on a moving average of quality scores.
>sanger_qc is a Python script designed to streamline the process of converting .ab1 files from Sanger sequencing into .fasta and .qual formats, followed by sequence trimming based on quality scores.

🚀 Quick Start
>You can start using sanger_qc with the following commands:

    git clone https://github.com/yourusername/sanger_qc.git
    cd sanger_qc
    pip install -r requirements.txt
    Run the script:
    ./sanger_qc.py -i /path/to/ab1_files -o /path/to/output_dir -w 10 -q 30.0

⚙️ Installation
>Ensure you have Python 3.6+ installed. Install the required packages with:
>pip install numpy biopython

🔧 Usage
>Run sanger_qc.py with the following options:

./sanger_qc.py -i <input_directory> -o <output_directory> [-w <window_size>] [-q <quality_cutoff>]
Arguments

    -i, --input_dir: (Required) Directory containing .ab1 files.
    -o, --output_dir: (Required) Directory for the output files.
    -w, --window_size: (Optional) Window size for moving average (default: 10).
    -q, --qual_cutoff: (Optional) Quality score cutoff for trimming (default: 30.0).
 
📂 Output Structure

    fasta/: Converted .fasta files.
    qual/: Converted .qual files.
    trimmed_fasta/: Trimmed .fasta files.
    trimmed_qual/: Trimmed .qual files.

