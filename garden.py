
# DS T20 Compulsory Task 1 - Introduction to Natural Language Processing

# Importing spacy
import spacy

# Load the English language model for spaCy
nlp = spacy.load("en_core_web_sm")

# Define the garden path sentences
gardenpathSentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Process each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)

    # Print the tokens and named entities
    print("Sentence:", sentence)
    print("Tokens:", [token.text for token in doc])
    print("Named Entities:", [(i.text, i.label_) for i in doc.ents])
    print("---------------")

# Get an explanation of an entity and print it
entity_fac_1 = spacy.explain("GPE")
print(f"GPE:{entity_fac_1}")
entity_fac_2 = spacy.explain("PERSON")
print(f"PERSON:{entity_fac_2}")

# Entity 1 is GPE:Countries, cities, states. The word associated was Mississippi which is correct.
# Entity 2 is PERSON:People, including fictional. The words assiciated were Jill, Mary, which are name of the person.