# exeter-coding-challenge

The task

Given a text file, replace all possible words in English to French using any programming language of choice

What is the input? The zip file ( TranslateWordsChallenge.zip ) has 4 files:

    Instruction document ( Translate Words Challenge.pdf )
    A text file ( t8.shakespeare.txt ) that has more than one lakh lines
    A find words list ( find_words.txt ) that has a 1000 words. The words in the list should be replaced with case being maintained.
    The English to French dictionary ( french_dictionary.csv ) to do the look up

What needs to be done?

    Read the input text file, find words list text file and dictionary csv file
    Find all words that is in the find words list, that has a replacement word in the dictionary
    Replace the words in the input text file
    Save the processed file as output

NOTE: Accuracy of the replace in terms of all occurrences, casing and special characters to be maintained

What is the expected output?

    Unique list of words that was replaced with French words from the dictionary
    Number of times a word was replace
    Time taken to process
    Memory taken to process
