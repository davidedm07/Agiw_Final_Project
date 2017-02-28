from lxml import html
import requests
import csv
import re
def check_types():
	print "Working"
	#maps containing the name of the relation and the link to the dbpedia page
	relations = create_maps_relations()
	#maps containing the entities with their dbpedia types
	entitiesType = create_maps_entities()
	fileName = "/home/davide/Scrivania/Agiw_Final_Project/new_facts/triples_not_in_dbpedia_estimated_relation.csv"
	relationsWithTypes = {}
	with open (fileName, "rb") as csvfile:
		csvReader = csv.reader(csvfile,delimiter = ";")
		for row in csvReader:
			relation  = row[4]
			if relation in relations.keys():
				page = requests.get(relations.get(relation))
				tree = html.fromstring(page.content)
				domainType = tree.xpath("//a[@rel = 'rdfs:domain']/text()")
				if len(domainType) != 0:
					domainType[0] = domainType[0].lstrip(':')
					rangeType = tree.xpath("//a[@rel = 'rdfs:range']/text()")
					if len(rangeType)!= 0:
						rangeType[0] = rangeType[0].lstrip(':')
						relationsWithTypes.setdefault(relation,[domainType[0],rangeType[0]])
						firstEntity = row[1]
						firstEntity = firstEntity.lstrip("\"")
						print firstEntity
						secondEntity = row[3]
						secondEntity = secondEntity.rstrip("\"")
						print secondEntity
						if firstEntity in entitiesType.keys() and secondEntity in entitiesType.keys():
							typeFirst = entitiesType.get(firstEntity)
							typeSecond = entitiesType.get(typeSecond)
							if typeFirst == rangeType[0] and typeSecond == domainType[0] or typeFirst == domainType[0] and typeSecond == rangeType :
								outputFile = open("/home/davide/Scrivania/new_facts_checked.csv", "a+")
								csvWriter = csw.writer(outputFile)
								csvWriter.writerow([row])
						
	
	csvfile.close()
	relationsOutput = open("/home/davide/Scrivania/map.tsv","a+")
	csvWriter = csv.writer(relationsOutput)
	csvWriter.writerow(relationsWithTypes)
	print "Done"


		

def create_maps_relations():
	relations = {}
	fileName = "/home/davide/Scrivania/Agiw_Final_Project/dbpedia/dbpedia_info_schema.tsv"
	with open (fileName, "r") as csvfile:
		csvReader = csv.reader(csvfile,delimiter = "\t")
		for row in csvReader:
			relation = row[0].rpartition('/')[2]
			link = row[0]
			relations.setdefault(relation,link)

	csvfile.close()
	print "relations map ready"
	return relations

def create_maps_entities():
	fileName = "/home/davide/Scrivania/Agiw_Final_Project/dbpedia/instances_types.tsv"
	with open(fileName,"rb") as csvfile:
		csvReader = csv.reader(csvfile, delimiter = '\t')
		entitiesType = {}
		for row in csvReader:
			entity = row[0].rpartition('/')[2]
			entityType = row[2].rpartition('/')[2]
			if entityType != "owl#Thing":
				entitiesType.setdefault(entity,entityType)

	print "entities map ready"
	return entitiesType
	
    
if __name__ == "__main__":
	check_types()