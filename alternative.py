# DS T11 Compulsory Task 1 - String Handling

# Create a program that reads in a string and makes each alternate character an UPPERCASE and lowercase character

input_str = input("Please enter a string: ")
output_str = ""
for i in range(len(input_str)):
    if i % 2 == 0:
        output_str += input_str[i].upper()
    else:
        output_str += input_str[i].lower()
print("Alternative character lower and upper case:",output_str.strip()) # We use strip() to remove any extra whitespace at the beginning or end of the string.

# Starting with the same string but making each alternative word lower and upper case.
words = input_str.split() # Split the input string into a list of words using the split() function.
output_words = ""
for i in range(len(words)):
    if i % 2 == 0:
        output_words += words[i].lower()+" "
    else:
        output_words += words[i].upper()+" "
    
print("Alternative word lower and upper case:", "".join(output_words).strip()) # We use strip() to remove any extra whitespace at the beginning or end of the string.