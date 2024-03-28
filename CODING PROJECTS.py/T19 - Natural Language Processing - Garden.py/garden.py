import spacy

nlp = spacy.load("en_core_web_sm")


web_example_1 = "The old man the boat."
web_example_2 = "The complex houses married and single soldiers and their families."
# https://en.wikipedia.org/wiki/Garden-path_sentence

# Create a list containing the two examples from the web.
#########################################################
gardenpathSentences =  [web_example_1, web_example_2]

# Add the sentences from the task to gardenpathSentences list.
###############################################################
gardenpathSentences.append("Mary gave the child a Band-Aid.")
gardenpathSentences.append("That Jill is never here hurts.")
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi.")


for i in gardenpathSentences:
    named_entity_recognition = nlp(i)

    # Print punctuation tokens and word tokens. # (token.orth_ returns a string representation of the token.
    #--------------------------------------------------------------------------------------------------------
    #print([token.orth_ for token in named_entity_recognition])

    # Print tokens without punctuations.
    ####################################
    print([token.orth_ for token in named_entity_recognition if not token.is_punct | token.is_space])

    # Get (i - Entity), (.label_string - Label as as string), (.label - Label as an interger) and print them.
    #--------------------------------------------------------------------------------------------------------
    #print([(i, i.label_, i.label) for i in named_entity_recognition.ents])
    
    # Get (i - Entity), (.label_string - Label as as string) and print them.
    ########################################################################
    print([(i, i.label_) for i in named_entity_recognition.ents])


#for i in named_entity_recognition.ents:
    # Get (Entity - i.text), Start position of entity - i.start_char), (End position of entity - i.end_char ), (i.label - Label as a string) and print them
    #-------------------------------------------------------------------------------------------------------------------------------------------------------
    #print(i.text, i.start_char, i.end_char, i.label_)
    
    # Get (Entity - i.text),(i.label - Label as a string) and print them.
    #####################################################################
    #print(i.text, i.label_)
    

# Entity explanation:
###############################################################################################################
    
    entity_person = spacy.explain("PERSON")
    entity_gpe = spacy.explain("GPE")
    print(f"PERSON: {entity_person}") #  People, including fictional - This was correctly assigned to Mary & Jill.
    print(f"GPE: {entity_gpe}") # Countries, cities, states - This was correctly assigned to Mississippi.
    # As for the two sentences there were not any words that could be identified as entities.

##############################################################################################################

    #----------------------------------------------
    #print(spacy.explain("PERSON")) # - Alternate 1
    #print(spacy.explain("GPE")) # - Alternate 1
    #----------------------------------------------

################################################################

for i in gardenpathSentences:
    named_entity_recognition = nlp(i)
    
    # Is the token in title case? Identify tokens is title case. 
    for word in named_entity_recognition:
        if word.is_title == True:
            print(word)
    
    # Is the token part of a “stop list”? Identify Stop words. 
    for word in named_entity_recognition:
        if word.is_stop == True:
            print(word)
#################################################################
