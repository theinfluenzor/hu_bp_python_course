import matplotlib as mpl
import numpy as np
import pandas as pd 
import processes
import random as rd
import time

np.random.seed(int(time.time()))
time = np.arange(0,1001,1.)
dna_length = 1000
dna_nucleotides = 'ATGC'
mrna_nucleotides =  'AUGC'
aa = processes.Translation.code.values()
while '*' in aa: aa.remove('*')

dna_seq = []
mrna_seq = []
protein_seq = []


for l in xrange(dna_length):
    dna_seq.append(rd.choice(dna_nucleotides))
    mrna_seq.append(rd.choice(mrna_nucleotides))
for p in xrange(dna_length/3):
	protein_seq.append(rd.choice(aa))

dna_count = np.random.random(len(time))
mran_count = np.random.random(len(time))
protein_count = np.random.random(len(time))

dna_seq = ''.join(dna_seq)
mrna_seq = ''.join(mrna_seq)
protein_seq = ''.join(protein_seq)

dna_test =     {'sequence'   : dna_seq,
                'time_course': dna_count,
                'mass'       :100}
mrna_test =    {'sequence'   : mrna_seq,
                'time_course': mran_count,
                'mass'       :100}
protein_test = {'sequence'   : protein_seq,
                'time_course': protein_count,
                'mass'       :1000} 

result = {'dna'    :dna_test,
          'mrna'   :mrna_test,
          'protein':protein_test}

