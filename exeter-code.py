import numpy as np
import pandas as pd
import os, psutil
import re
import time


start = time.time() #start time

#store the words to be found and replaced in a list

list_words = list()
for line in open('find_words.txt'):
    list_words.append(line.strip().split('\n'))
print(list_words)


#store the english and french words to a dictionary

french_dictionary = pd.read_csv('french_dictionary.csv', header=None)
eng_list = french_dictionary[0].to_list()
french_list = french_dictionary[1].to_list()

l = len(french_list)

#create a dictionary
dictionary = {eng_list[i]:french_list[i] for i in range(l)}

print(dictionary)

#open the file in which the words need to be replaced

with open('t8.shakespeare.txt', 'r') as file:
    data = file.read()

#function to replace the words in the text file

def replace_words(text, dictionary):
    check=[]
    frequency = []
    for key in dictionary:
        frequency.append([a.start() for a in re.finditer(key, text)])
        text = text.replace(key, dictionary[key])
        check.append([a.start() for a in re.finditer(dictionary[key], text)])
    
    return text, frequency, check

#store the replaced text files, frequency of words and checked words

replaced_text, frequency_words, check_words = replace_words(data, dictionary)

#find the number of words replaced

count=0

for i in range(len(frequency_words)):
    print(len(frequency_words[i]),'\t',len(check_words[i]))
    if len(frequency_words[i])>0:
        count+=1 

print("Number of words replaced are : ", count)

#find the frequency of words

freq = []
for i in range(len(frequency_words)):
    freq.append(len(frequency_words[i]))

#store the replaced text

file = open("t8.shakespeare.translated.txt", "w")
file.write(" %s " % replaced_text)
file.close()

#store the data as csv

Dict_words=[{'English word':eng, 'French word':fre, 'Frequency':fr} for eng,fre,fr in zip(eng_list,french_list,freq)]

dataFrame = pd.DataFrame (Dict_words, columns = ['English word','French word','Frequency'])

print(dataFrame)

dataFrame.to_csv("frequency.csv", index=None)

#find the total number of words replaced

list_of_words = []
for i in range(len(dataFrame)):
    if dataFrame['Frequency'][i]>0:
        list_of_words.append(dataFrame['English word'][i])

print(list_of_words)

print(len(list_of_words))

#find the time taken and memory used

end=time.time()
print(end - start, "seconds")

with open("performance.txt", "w") as file:
    file.write("Time to process: %s seconds\n" % str(end - start))
    file.write("Memory used: %s MB" % str(psutil.Process(os.getpid()).memory_info().rss / 1024**2))
