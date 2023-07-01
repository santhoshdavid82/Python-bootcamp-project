# DS T21 Compulsory Task 2 - Semantic Similarity (NLP)

import spacy

# Load the English language model 
nlp = spacy.load('en_core_web_md')

def find_similar_movie(description):
    # Read the movies.txt file and store the descriptions in a list
    with open('movies.txt', 'r') as file:
        movie_descriptions = file.read().splitlines()

    # Initialize variables to store the most similar movie title and its similarity score.
    # The below variable is initialized as None. It will be used to store the title of the movie that is found to be the most 
    # similar to the given query description.
    most_similar_movie = None

    # The below variable is initialized as 0.0. It represents the highest similarity score found so far between the 
    # query description and the movie descriptions.
    highest_similarity = 0.0

    # Iterate over each movie description and calculate the similarity with the input description
    for movie_description in movie_descriptions:
        # Calculate the similarity using spaCy's similarity function
        similarity = nlp(description).similarity(nlp(movie_description))

        # Update the most similar movie if a higher similarity is found
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_movie = movie_description

    # Return the title of the most similar movie
    return most_similar_movie

# Test the function
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = find_similar_movie(description)
print("Next movie to watch:", similar_movie)
