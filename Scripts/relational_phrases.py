import csv
import re
def get_labeled_relational_triples():

	print "Creating the dictionary with all the relational phrases"
	with open("sorted_relational_phrases.txt","r") as relationalPhrases:
		csvReader = csv.reader(relationalPhrases)
		phrases = {}
		for row in csvReader:
			phrases.setdefault(row[0],row[0])
		#relationalPhrases.close()
		print "Searching for relational triples"
		with open ("./lector_sentences/sentences/sorted_extracted_sentences_with_triples.tsv","rb") as triples:
			triplesReader = csv.reader(triples,delimiter = "\t")
			for row in triplesReader:
				#list, phrase[0] == the actual phrase
				phrase = re.findall(r'(?<=\]\])[^\]]+(?=\[\[)',row[0])
				phrase[0] = phrase[0].lstrip()
				phrase[0] = phrase[0].rstrip()
				if phrase[0] in phrases.keys():
					with open ("labeled_triples.tsv", "a+") as labeledTriples:
						csvWriter = csv.writer(labeledTriples)
						csvWriter.writerow([row[0]])

		triples.close()
		
		print "Done"
				
	

			


if __name__ == "__main__":
	get_labeled_relational_triples()	