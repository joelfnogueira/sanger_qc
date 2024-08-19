from setuptools import setup, find_packages

setup(
    name="sanger_qc",
    version="0.1.0",
    author="Joel Fonseca Nogueira",
    author_email="joelfnogueira@hotmail.com",
    description="A Python script for converting .ab1 files to .fasta and .qual, and trimming sequences based on quality scores.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sanger_qc",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18.0",
        "biopython>=1.78"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'sanger_qc=sanger_qc:main',
        ],
    },
)
