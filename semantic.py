
# DS T21 Compulsory Task 1 - Semantic Similarity (NLP)

import spacy  # importing spacy.
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. 

# spaCy commands to determine similarity.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Note about what you found interesting about the similarities between cat, monkey and banana.

# The interesting aspect of the results you get is that they reflect certain semantic relationships between the words.

# The word1.similarity(word2) line calculates the similarity score (0.5929929675536907) between "cat" and "monkey".
# Since cats and monkeys are both animals, but belong to different species, the similarity score may not be very high but is likely 
# to indicate some shared characteristics. 

# The word3.similarity(word2) line computes the similarity score (0.4041501317354622) between "banana" and "monkey".
# In this case, the similarity score is expected to be relatively low because bananas and monkeys are not closely
# related in terms of their semantic meaning. Hence the score was less than between the cat and monkey similarity score.

# Lastly, the word3.similarity(word1) line calculates the similarity score (0.22358825939615987) between "banana" and "cat." Again,
# these two words are unrelated in terms of their semantic meaning, so the similarity score is expected to be the 
# lowest compare to other two scores.

# As for an example of my own, let's consider the words "car," "bicycle," and "ocean." The similarity between "car" and 
# "bicycle" is expected to be relatively high since they both represent modes of transportation, although they differ  
# in terms of size and mechanism. On the other hand, the similarity between "ocean" and "car" or "ocean" and "bicycle" is 
# anticipated to be much lower as they are unrelated concepts.

# spaCy commands to determine similarity:
word1 = nlp("car")
word2 = nlp("bicycle")
word3 = nlp("ocean")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


# Working with Vectors.
# We will use two for loops to allow us to undertake a comparison of the words.
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Working with Sentences.
# The text similarity is often computed by first embedding the two short texts
# and then calculating the cosine similarity between them.

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# For the task Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on 
# what you notice is different from the model 'en_core_web_md'. Please see 
# the pdf file 'DS T21 Compulsory Task 1 - Semantic Similarity (NLP)' on the same folder. 
# Thank you.