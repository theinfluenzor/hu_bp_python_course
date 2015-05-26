import pandas as pd

print 'vor einlesen'
genes = pd.read_csv('genes.csv',header=4, index_col=1)
print 'nach einlesen'
#print genes
sequence = genes[['SwissProt','GenBank','Name','Sequence']]
print sequence.head()