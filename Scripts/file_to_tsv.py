import csv
import re
def add_tabs():
	with open ("/home/davide/Scrivania/Agiw_Final_Project/lector_sentences/sentences/sorted_extracted_sentences_with_triples.tsv","rb") as csvfile:
		csvReader = csv.reader(csvfile)		
		for row in csvReader:
			entities = []
			phrase = []
			entities = re.findall(r'\[\[[^\]]+\]\]',row[0])
			phrase = re.findall(r'(?<=\]\])[^\]]+(?=\[\[)',row[0])
			#print len(entities)
			if entities!= None and phrase!= None:
				if len(entities)== 2 and len(phrase)==1:
					sentence = entities[0] + "\t" + phrase[0] + "\t" + entities[1]
					with open("sorted_extracted_sentences_with_triples_tabs.tsv","a+") as tabsFile:
						csvWriter = csv.writer(tabsFile)
						csvWriter.writerow([sentence])
			
	csvfile.close()

""" Da usare se il join tra triple con frasi relazionali e triple labeled viene fatto con mysql"""
def clean_extracted_sentences():
	with open ("/home/davide/Scrivania/Agiw_Final_Project/Labeled/relational_labeled_triples.tsv","rb") as csvfile:
		csvReader = csv.reader(csvfile)
		for row in csvReader:
			entities = []
			phrase = []
			entities = re.findall(r'(?<=\[\[)[^\|]+',row[0])
			phrase = re.findall(r'(?<=\]\])[^\]]+(?=\[\[)',row[0])
			if entities!= None and phrase!= None:
				if len(entities)== 2 and len(phrase)==1:
					sentence = entities[0] + phrase[0] + entities[1]
					with open("clean_relational_labeled_triples.tsv","a+") as tabsFile:
						csvWriter = csv.writer(tabsFile)
						csvWriter.writerow([sentence])
			
	csvfile.close()

def trim_spaces():
	with open ("/home/davide/Scrivania/Agiw_Final_Project/sorted_per_phrase_triples.tsv","rb") as csvfile:
		csvReader = csv.reader(csvfile)		
		for row in csvReader:
			entities = []
			phrase = []
			entities = re.findall(r'\[\[[^\]]+\]\]',row[0])
			phrase = re.findall(r'(?<=\]\])[^\]]+(?=\[\[)',row[0])
			
			#print len(entities)
			if entities!= None and phrase!= None:
				if len(entities)== 2 and len(phrase)==1:
					phrase[0] = phrase[0].lstrip()
					phrase[0] = phrase[0].rstrip()
					sentence = entities[0]  + "\t" + phrase[0] + "\t" +entities[1]
					with open("sorted_extracted_sentences_with_triples_tabs_trimmed.tsv","a+") as tabsFile:
						csvWriter = csv.writer(tabsFile)
						csvWriter.writerow([sentence])
			
	csvfile.close()
	print "Done"


if __name__ == "__main__":
	#trim_spaces()
	clean_extracted_sentences()
	#add_tabs()
