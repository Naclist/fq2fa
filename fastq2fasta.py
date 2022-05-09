import gzip
import argparse
import os
import time

parser = argparse.ArgumentParser(
    description='Convert an fastq file to an fasta file.',
    add_help=False,
    usage='\nfastq2fasta.py --fastq[Even if it is compressed, there is no problem.]')

parser.add_argument(
    '--fastq',
    metavar='[input.fq]',
    required=True,
    type=str)

args = parser.parse_args()


def fq2fa(fqfile):
    fastq = open(fqfile, 'rt')
    fasta = open(fqfile.split('.f')[0] + '.fasta', 'w')
    i = 0
    for line in fastq:
        i += 1
        if i % 4 == 1:
            line_new = line[1:]
            fasta.write('>' + line_new)
        elif i % 4 == 2:
            fasta.write(line)
    fasta.close()


def un_gz(file_name):
    f_name = file_name.replace(".gz", "")
    g_file = gzip.GzipFile(file_name)
    open(f_name, "wb+").write(g_file.read())
    g_file.close()


if 'gz' == args.fastq.split('.')[-1]:
    un_gz(args.fastq)
    filename = args.fastq[:-3]
    fq2fa(filename)
    os.remove(filename)

else:
    filename = args.fastq
    fq2fa(filename)
