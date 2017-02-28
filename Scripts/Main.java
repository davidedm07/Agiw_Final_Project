package com.company;

import FSM.RelationalFilter;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {


    public static void main(String[] args) throws IOException {

        RelationalFilter rf = new RelationalFilter();
        String csvFile = "../cleaned_entities_phrase_from_sentences_u.tsv";
        String line = "";
        MaxentTagger tagger = new MaxentTagger("stanford-postagger-2016-10-31/models/english-left3words-distsim.tagger");
        File file = new File("rel_phrases.txt");

        if (!file.exists()) {
            file.createNewFile();
        }
        FileWriter fw = new FileWriter(file);
        BufferedWriter bw = new BufferedWriter(fw);

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {

            while ((line = br.readLine()) != null) {
                String taggedString = tagger.tagTokenizedString(line.trim());
                String[] tags = extractTag(taggedString);
                boolean isRel = rf.isRelational(tags);
                if (isRel){
                    bw.write(line.trim());
                    bw.newLine();
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        bw.close();
    }

    private static String[] extractTag(String taggedString) {
        List<String> tags = new ArrayList<>();
        String[] words = taggedString.split(" ");
        for (String word : words) {
            tags.add(word.substring(word.lastIndexOf("_") + 1));
        }
        return tags.toArray(new String[0]);
    }

}