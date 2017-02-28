import csv


def map_relation_types():
    #salvo in una mappa relazione=>lista tipi (presi da domain e range)
    fileName = "C:\Users\Alessio\Desktop\Alessio\Roma 3\Magistrale\Secondo anno\Primo semestre\Analisi e gestione delle informazioni sul web\Progetto finale\clean_info_schema_domainRange.tsv"
    relationsWithTypes = {}
    with open(fileName, "r") as csvfile:
        csvReader = csv.reader(csvfile, delimiter="\t")
        for row in csvReader:
            relation = row[1]
            rdf = row[2]
            types = row[3]
            if relation in relationsWithTypes.keys():
                if rdf == 'domain' or rdf == 'range':
                    if rdf == 'domain':
                        domainType = types
                        relationsWithTypes[relation].append(domainType)
                    if rdf == 'range':
                        rangeType = types
                        relationsWithTypes[relation].append(rangeType)
            else:
                if rdf == 'domain' or rdf == 'range':
                    if rdf == 'domain':
                        domainType = types
                        relationsWithTypes.setdefault(relation, [domainType])
                    if rdf == 'range':
                        rangeType = types
                        relationsWithTypes.setdefault(relation, [rangeType])
    csvfile.close()
    return relationsWithTypes


def entity_control_type():
    # inserisco in una mappa l'entita' come chiave e il tipo come valore
    with open("C:\Users\Alessio\Desktop\Alessio\Roma 3\Magistrale\Secondo anno\Primo semestre\Analisi e gestione delle informazioni sul web\Progetto finale\clean_instances_types.tsv","rb") as csvfile:
        csvReader = csv.reader(csvfile, delimiter = "\t")
        entity_type = {}
        for row in csvReader:
            entity = row[0]
            type = row[1]
            entity_type.setdefault(entity,type)
    csvfile.close()
    return entity_type


def extract_facts():
    #estraggo nuovi fatti
    fileNameRelations = "C:\Users\Alessio\Desktop\Alessio\Roma 3\Magistrale\Secondo anno\Primo semestre\Analisi e gestione delle informazioni sul web\Progetto finale\\triples_not_in_dbpedia_estimated_relation.csv"
    relationsWithTypes = map_relation_types() #mappa relazione=>lista tipi
    entityWithType = entity_control_type() #mappa entita'=>tipo
    new_facts = []
    with open(fileNameRelations, "r") as csvfile:
        csvReader = csv.reader(csvfile, delimiter=";")
        for row in csvReader:
            relation = row[4]
            if relation in relationsWithTypes.keys(): #se la relazione e' presente in clean_info_schema_domainRange
                entity1 = row[1]
                phrase = row[2]
                entity2 = row[3]
                type1 = entityWithType.get(entity1)
                type2 = entityWithType.get(entity2)
                #salvo il fatto se i tipi delle due entita' sono contenuti nella lista della relazione
                if (type1 in relationsWithTypes.get(relation)) or (type2 in relationsWithTypes.get(relation)):
                    quadruple = [entity1,phrase,entity2,relation]
                    new_facts.append(quadruple)
    csvfile.close()
    print(new_facts)


    with open("C:\Users\Alessio\Desktop\Alessio\Roma 3\Magistrale\Secondo anno\Primo semestre\Analisi e gestione delle informazioni sul web\Progetto finale\\new_facts.tsv", "w+") as csvfile:
        csvWriter = csv.writer(csvfile, delimiter="\t")
        for quadruple in new_facts:
           csvWriter.writerow(quadruple)
        csvfile.close()


if __name__ == "__main__":
    extract_facts()