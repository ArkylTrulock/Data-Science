import spacy

nlp = spacy.load('en_core_web_md') # Load advanced language model to find similarities and differences.

# Define our function
def film_to_watch_next(film):
     
     # The open() function opens the file if possible and returns the corresponding file object.
     # r - Open a file for reading mode (default if the mode is not specified).
    file_path = open("C:/Users/tailb/Data Science/JUPYTER NOTEBOOK/movies.txt", 'r')


     # The readlines() function reads all the lines from the text file and returns each line as a string element in a list.
     # Define with variable of your choosing.
    synopsis = file_path.readlines()
    
    token_1 = nlp(film)

    # Declare an empty string where our end result will be appended/added
    sim_list = []

    for item in synopsis:
        # Ignore index 0 - 8 and select from index 9. Select text from starting only from index 9.
        token_2 = nlp(item[9::])
        
        # Add/append result(s) of similarity comparison
        sim_list.append(token_1.similarity(token_2))

    max_sim = max(sim_list)
    movie = synopsis[sim_list.index(max_sim)][0:9]
    print(movie, max_sim)
    
watch_planet_Hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

film_to_watch_next(watch_planet_Hulk)