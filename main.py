import spacy
from spacy import displacy
import os


# Exercise 1


def write_to_file(text: str, output_file_path):
    with open(output_file_path, 'w') as file:  # need to open it in write mode
        file.write(text)  # writing the text into the file
    if os.path.exists(output_file_path):  # to check if the file already exists
        raise FileExistsError(f'There is already a file saved for {output_file_path}')


# Exercise 2


def count_stopwords(input_file_path):
    nlp = spacy.load(
        r'C:\Users\lisal\AppData\Local\Programs\Python\Python311\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.5.0')
    # I have to load it like that, as the other way raises an error and this is the only way I could find to fix it
    with open(input_file_path) as inpt:
        inp = nlp(inpt.read())  # feeding the text into the doc at the same time as reading it
    counter = 0  # creating a variable to count occurrences
    for i in inp:  # looping through our input
        if i.is_stop:  # checking if it's a stopword
            counter = counter + 1  # adding to the counter
    if counter > 0:  # I think this might not be necessary, I could just return the counter in both cases,
        # as it would just return the value 0 if there weren't any stopwords,
        # but in case there is a situation where that wouldn't be true, I'm making it explicit
        print(counter)
        return counter
    else:
        return 0


# Exercise 3

def remove_stopwords(input_file_path, output_file_path):
    nlp = spacy.load(
        r'C:\Users\lisal\AppData\Local\Programs\Python\Python311\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.5.0')
    with open(input_file_path, 'r') as inpt:
        inp = list(nlp(inpt.read()))  # need to turn it into a list to loop through it
    rem_stop = []
    for i in inp:
        if not i.is_stop:  # appending the words to the list, if they aren't stop words
            rem_stop.append(i.text)  #
    with open(output_file_path, 'w') as output:
        output.writelines(rem_stop)


remove_stopwords('test.txt', 'rem_test.txt')


# Exercise 4

def tokenize_text(input_file_path, output_file_path):
    nlp = spacy.load(
        r'C:\Users\lisal\AppData\Local\Programs\Python\Python311\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.5.0')
    with open(input_file_path, 'r') as inpt:
        inp = nlp(inpt.read())
    with open(output_file_path, 'w') as output:
        for token in inp:
            output.write(f"{token.text:{10}}{token.pos_:{10}}{token.dep_:{10}}")


# Exercise 5

def save_visualization(input_file_path, output_file_path):
    with open(input_file_path, 'r') as inpt:
        inp = inpt.read()
    with open(output_file_path, 'w') as output:
        output.write(f"{displacy.render(inp)}")

