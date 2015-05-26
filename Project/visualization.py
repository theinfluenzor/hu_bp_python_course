import matplotlib as mpl
import numpy as np
import pandas as pd 
import processes
import random as rd

time = np.arange(0,1001,1.)
dna_nucleotides = 'ATGC'
mrna_nucleotides =  'AUGC'
aa = processes.Translation.code.values()
while '*' in aa: aa.remove('*')

dna_seq = []
mrna_seq = []
protein_seq = []


for point in time:
    dna_seq.append(rd.choice(dna_nucleotides))
    mrna_seq.append(rd.choice(mrna_nucleotides))
    protein_seq.append(rd.choice(aa))

dna_seq = ''.join(dna_seq)
mrna_seq = ''.join(mrna_seq)
protein_seq = ''.join(protein_seq)

dna_test = {'sequence': dna_seq
}
mrna_test = {'sequence': mrna_seq}
protein_test = {'sequence' : protein_seq} 
