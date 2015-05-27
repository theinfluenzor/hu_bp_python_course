# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3 as lite
import cPickle as pickle

####Input aus Excel-Tabellen
#Einlesen der Gen-, Metabolit- und Mediumsspezifikation
genes = pd.read_csv('genes.csv',header=4, index_col=None)
metabolites =pd.read_csv('metabolite.csv',header=4, index_col=0, na_values=['NaN'], keep_default_na=False)
media = pd.read_csv('media.csv',header=3,index_col=0, na_values=['NaN'],keep_default_na=False)
protein_hl = pd.read_csv('mRNA.csv',header=4, index_col=0, na_values=[' '],keep_default_na=False)


#Editieren der Dataframes
#Herauswerfen aller unwichtigen Spalten
metabolites = metabolites['Name']
genes = genes[['BioCyc','SwissProt','GenBank','Sequence','Coordinate']]
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

#Ueberscrheiben der csv files



#name=genes/metabolites/media
def writeData(data,name):
	f = open(name+'.sql','w')
	with f:
		f.write(data)

#Schreiben in die Datenbank
con = lite.connect('./database/knowledgebase.db')
con.text_factory = str



#Writing sql-files for the database
#helplist
helplist1 = ['genes', 'protein_hl','metabolites','conc']
helplist2 = [genes, protein_hl, metabolites, conc]
helper = dict((helplist1[t], helplist2[t]) for t in xrange(len(helplist1)))
for j in helper.keys():
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS "+j )
		wert=helper[j].to_sql(j,con)
		data = '\n'.join(con.iterdump())
		writeData(data, "./database/"+j)

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS genome" )
	cur.execute("CREATE TABLE genome(Sequence TEXT)")
	cur.execute("INSERT INTO genome VALUES('"+genome+"')")
	data = '\n'.join(con.iterdump())
	writeData(data, "./database/genome.sql")




#Reading from db
helplist = ['genes', 'protein_hl','metabolites','conc', 'genome']
con = lite.connect('./database/knowledgebase.db')
with con:
	for j in helplist:
		cur = con.cursor()    
		cur.execute('SELECT * FROM '+j)
		data = cur.fetchall()
		indexhelp = [data[i][0] for i in xrange(len(data))]
		if j=='genes':
			dframe = pd.DataFrame(data, index=indexhelp, columns=['dump','BioCyc', 'SwissProt','GenBank','Sequence', 'Coordinate'])
			dframe = dframe.drop('dump',axis=1)
		if j=='protein_hl':
			indexhelp = [data[i][0] for i in xrange(len(data))]
			dframe = pd.DataFrame(data,index = indexhelp, columns=['dump','Name','Halflife min'], dtype=float)
			dframe = dframe.drop('dump',axis=1)
		if j=='metabolites':
			indexhelp = [data[i][0] for i in xrange(len(data))]
			dframe = pd.DataFrame(data, index=indexhelp, columns=['dump','Name'])
			dframe = dframe.drop('dump',axis=1)
		if j=='conc':
			dframe = pd.DataFrame(data, index=indexhelp, columns=['dump','Name', 'Concentration mM'], dtype=float)
			dframe = dframe.drop('dump',axis=1)
		if j=='genome':
			pass#print data
#dframe = pd.DataFrame(data, index=indexhelp, columns=['dump','Name', 'Concentration mM'], dtype=float)
#dframe = dframe.drop('dump',axis=1)
