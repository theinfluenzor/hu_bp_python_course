# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3 as lite
import cPickle as pickle

####INput aus Excel-Tabellen
#Einlesen der Gen-, Metabolit- und Mediumsspezifikation
genes = pd.read_csv('genes.csv',header=4, index_col=None)
metabolites =pd.read_csv('metabolite.csv',header=4, index_col=0, na_values=['NaN'], keep_default_na=False)
media = pd.read_csv('media.csv',header=3,index_col=0, na_values=['NaN'],keep_default_na=False)
protein_hl = pd.read_csv('mRNA.csv',header=4, index_col=0, na_values=[' '],keep_default_na=False)


#Editieren der Dataframes
#Herauswerfen aller unwichtigen Spalten
metabolites = metabolites['Name']
genes = genes[['BioCyc','SwissProt','GenBank','Name','Sequence','Coordinate']]
media = media['Concentration mM']
protein_hl = protein_hl[['Symbol', 'Protein Halflife']]


#Konkatenieren der Listen an entsprechender Stelle und Herauswerfen der NaN Werte
conc = pd.concat([metabolites, media], axis=1)
conc = conc[pd.notnull(conc['Concentration mM'])]


##Laden des vollstaendigen Genoms in einen Objekt
with open('sequence.fasta','r') as f:
	genome = f.readlines()
f.close()
#Herauswerfen der ersten Zeile und zusammenhaengen der Sequenzen in einen String
genome = [line[:-1] for line in genome if line[0] != '>']
genome = ''.join(genome)


#ueberscrheiben der csv files


#TODO
#import in sql
#schnittstelle zu anderen modulen

#name=genes/metabolites/media
def writeData(data,name):
	f = open(name+'.sql','w')
	with f:
		f.write(data)


con = lite.connect(':memory:')
con.text_factory = str

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Genes")
	cur.execute("CREATE TABLE Genes(BioCyc , SwissProt , GenBank, Name, Sequence, Coordinate);")
	for i in xrange(len(genes)):
		#string='MG_'+str(i)
		#cur.execute("INSERT INTO Genes (CMR )VALUES(?);", string) 
		cur.execute("INSERT INTO Genes (BioCyc, SwissProt , GenBank, Name, Sequence, Coordinate) VALUES(?,?, ?, ?, ?, ?);", genes.iloc[i,0:6]) 
	data = '\n'.join(con.iterdump())

	writeData(data, 'genes')
