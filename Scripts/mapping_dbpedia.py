import csv
import re

def mapping_triples():
	with open ("/home/davide/Scrivania/Agiw_Final_Project/dbpedia/dbpedia_mapping_based_triples.tsv","rb") as csvfile:
		csvReader = csv.reader(csvfile,delimiter = "\t")
		cleanTriples = []
		for row in csvReader:
			primaryEntity = row[0].rpartition('/')[2]
			relation  = row[1].rpartition('/')[2]
			secondaryEntity = row[2].rpartition('/')[2]
			triple = [primaryEntity,relation,secondaryEntity]
			cleanTriples.append(triple)
			#print triple

	#print cleanTriples

	with open("/home/davide/Scrivania/Agiw_Final_Project/clean_labeled_triples.tsv", "w+") as csvfile:
		csvWriter = csv.writer(csvfile,delimiter = "\t")
		for triple in cleanTriples:
			csvWriter.writerow(triple)
		csvfile.close()

if __name__ == "__main__":
	mapping_triples()

