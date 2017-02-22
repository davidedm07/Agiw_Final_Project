import csv
import re

def split_row(sentence):
	splitRow = re.findall(r'(\[\[[^\[]+\]\][^\[]+\[\[[^\[]+\]\])',sentence) 
	return splitRow


def get_phrases():
	print("Reading file with the Wikipedia Sentences")
	with open("/home/davide/Scrivania/Agiw_Final_Project/lector_sentences/sentences/sentences_all.tsv", "rb") as csvfile:
		csvReader = csv.reader(csvfile,delimiter = "\t")
		splittedSentences = {}
		for row in csvReader:
			splitRow = split_row(row[3])
			for sentence in splitRow:
				splittedSentences.setdefault(sentence,sentence)
					
	print "Writing sentences in file extracted_sentences.tsv"	
	with open("/home/davide/Scrivania/Agiw_Final_Project/lector_sentences/sentences/extracted_sentences.tsv", "w+") as csvfile:
		csvWriter = csv.writer(csvfile)
		for sentence in splittedSentences:
			csvWriter.writerow([sentence])
		
		csvfile.close()
	print "Done"
if __name__ == "__main__":
	get_phrases()
