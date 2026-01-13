"""
Code to take in a .fasta file and convert it to a AF3 compatible JSON file.
The .fasta header is used to populate information such as sequence name and
the number of chains. 
"""
import json
import protfasta
import os



