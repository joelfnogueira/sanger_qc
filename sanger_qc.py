#!/usr/bin/env python3

import argparse
import glob
import os
import numpy as np
from Bio import SeqIO

def convert_ab1_to_fasta_and_qual(input_dir, fasta_dir, qual_dir):
    """Converte arquivos .ab1 para .fasta e .qual, e salva em diretórios separados."""
    files = sorted(glob.glob(f"{input_dir}/*.ab1"))
    
    for x in files:
        sample_seq = SeqIO.read(x, "abi")
        sample_seq.id = sample_seq.name
        SeqIO.write(sample_seq, f"{fasta_dir}/{sample_seq.id}.fasta", "fasta")
        SeqIO.write(sample_seq, f"{qual_dir}/{sample_seq.id}.qual", "qual")
        print(f"fasta and qual file created for {sample_seq.id}")

def movingaverage(data_in, window_size):
    """Calcula a média móvel de uma lista de dados."""
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(data_in, window, 'same')

def trim_sequences(window_size, qual_cutoff, fasta_dir, qual_dir, output_fasta_dir, output_qual_dir):
    """Realiza o corte das sequências baseado na qualidade média móvel e salva em diretórios separados."""
    files = sorted(glob.glob(f"{qual_dir}/*.qual"))

    for x in files:
        sample_qual = SeqIO.read(x, "qual")
        sample_seq = SeqIO.read(f"{fasta_dir}/{sample_qual.id}.fasta", "fasta")
        sample_qual_score = sample_qual.letter_annotations["phred_quality"]
        sample_qual_MA = np.array(movingaverage(sample_qual_score, window_size))

        if np.max(sample_qual_MA) > qual_cutoff:
            qual_above = list(np.where(sample_qual_MA > qual_cutoff))[0]
            sample_qual_min = np.min(qual_above)
            sample_qual_max = np.max(qual_above)
            sample_qual_trim = sample_qual[sample_qual_min:sample_qual_max]
            sample_seq_trim = sample_seq[sample_qual_min:sample_qual_max]

            SeqIO.write(sample_qual_trim, f"{output_qual_dir}/{sample_qual.id}.trim.qual", "qual")
            SeqIO.write(sample_seq_trim, f"{output_fasta_dir}/{sample_seq.id}.trim.fasta", "fasta")
            print(f"Trimmed fasta and qual file created for {sample_qual.id}")
        else:
            print(f"The maximum quality score for {sample_qual.id} is below the cutoff")

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Este script converte arquivos .ab1 para .fasta e .qual, "
            "e realiza o corte das sequências baseado na qualidade média móvel.\n\n"
            "Uso:\n"
            "./sanger_qc.py -i <diretório_de_entrada> -o <diretório_de_saida> -w <tamanho_da_janela> -q <corte_de_qualidade>\n\n"
            "Argumentos:\n"
            "  -i, --input_dir    Diretório de entrada contendo os arquivos .ab1.\n"
            "  -o, --output_dir   Diretório de saída para os arquivos .fasta e .qual convertidos e/ou aparados.\n"
            "  -w, --window_size  Tamanho da janela de média móvel (padrão: 10).\n"
            "  -q, --qual_cutoff  Corte de qualidade para aparar as sequências (padrão: 30.0).\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('-i', '--input_dir', type=str, required=True,
                        help='Diretório de entrada contendo os arquivos .ab1')
    parser.add_argument('-o', '--output_dir', type=str, required=True,
                        help='Diretório de saída para os arquivos .fasta e .qual convertidos e/ou aparados')
    parser.add_argument('-w', '--window_size', type=int, default=10,
                        help='Tamanho da janela de média móvel (padrão: 10)')
    parser.add_argument('-q', '--qual_cutoff', type=float, default=30.0,
                        help='Corte de qualidade para aparar as sequências (padrão: 30.0)')
    
    args = parser.parse_args()

    # Criar subdiretórios para arquivos fasta e qual
    fasta_dir = os.path.join(args.output_dir, "fasta")
    qual_dir = os.path.join(args.output_dir, "qual")
    trimmed_fasta_dir = os.path.join(args.output_dir, "trimmed_fasta")
    trimmed_qual_dir = os.path.join(args.output_dir, "trimmed_qual")
    
    os.makedirs(fasta_dir, exist_ok=True)
    os.makedirs(qual_dir, exist_ok=True)
    os.makedirs(trimmed_fasta_dir, exist_ok=True)
    os.makedirs(trimmed_qual_dir, exist_ok=True)

    # Converte arquivos .ab1 para .fasta e .qual
    convert_ab1_to_fasta_and_qual(args.input_dir, fasta_dir, qual_dir)

    # Realiza o corte das sequências baseado na qualidade
    trim_sequences(args.window_size, args.qual_cutoff, fasta_dir, qual_dir, trimmed_fasta_dir, trimmed_qual_dir)

if __name__ == '__main__':
    main()
