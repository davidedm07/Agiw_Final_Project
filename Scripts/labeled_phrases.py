import csv
import re
def labeled_phrases():
	#phrases = map {phrase, count occurrences}
	with open("/home/davide/Scrivania/Agiw_Final_Project/Labeled/sorted_clean_labeled_triples.tsv","rb") as csvfile:
		csvReader = csv.reader(csvfile, delimiter = "\t")
		phrases ={}
		for row in csvReader:
			relation = row[1]
			#print "Searching correspondences for entity ",row[0]
			phrases = setdefault (row[1],0)
			#cambiare file, bisogna prendere quello con le triple e frasi relazionali, risultato join mysql
			with open("/home/davide/Scrivania/Agiw_Final_Project/lector_sentences/sentences/sorted_extracted_sentences.tsv", "rb") as sentences:
				sentencesReader = csv.reader(sentences,delimiter = "\t")
				for sentence in sentences:
					#print sentence
					entities = re.findall(r'(?<=\[\[)[^\|]+',sentence)
					entity1 = entities[0]
					entity2 = entities[1]
					if row[0] and row[2] in sentence:
						#print "Trovato"
						phrase  = re.findall(r'\]\](.+?)\[\[',sentence)
						phrases[phrase] = phrases.get(phrase) +	1
			relationFile = open("/home/davide/Scrivania/Agiw_Final_Project/Labeled/" + row[1] + ".tsv", "a+")
			csvWriter = csv.writer(relationFile)
			fileLine = relation + "\t" +phrase + "\t" + phrases.get(phrase)		
			csvWriter.writerow([fileLine])
					

if __name__ == "__main__":
	labeled_phrases()