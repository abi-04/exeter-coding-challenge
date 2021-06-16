import numpy as np
import pandas as pd
import os, psutil
import re
import time


start = time.time()


list_words = list()
for line in open('find_words.txt'):
    list_words.append(line.strip().split('\n'))
print(list_words)



french_dictionary = pd.read_csv('french_dictionary.csv', header=None)
eng_list = french_dictionary[0].to_list()
french_list = french_dictionary[1].to_list()

l = len(french_list)

d = {eng_list[i]:french_list[i] for i in range(l)}

dictionary = dict(zip(eng_list,french_list))
print(dictionary)

with open('t8.shakespeare.txt', 'r') as file:
    data = file.read()

def replace_words(text, dictionary):
    check=[]
    frequency = []
    for key in dictionary:
        frequency.append([a.start() for a in re.finditer(key, text)])
        text = text.replace(key, dictionary[key])
        check.append([a.start() for a in re.finditer(dictionary[key], text)])
    
    return text, frequency, check


replaced_text, frequency_words, check_words = replace_words(data, dictionary)

count=0

for i in range(len(frequency_words)):
    print(len(frequency_words[i]),'\t',len(check_words[i]))
    if len(frequency_words[i])>0:
        count+=1 

print("Number of words replaced are : ", count)

freq = []
for i in range(len(frequency_words)):
    freq.append(len(frequency_words[i]))



file = open("t8.shakespeare.translated.txt", "w")
file.write(" %s " % replaced_text)
file.close()

Dict_words=[{'English word':eng, 'French word':fre, 'Frequency':fr} for eng,fre,fr in zip(eng_list,french_list,freq)]

dataFrame = pd.DataFrame (Dict_words, columns = ['English word','French word','Frequency'])

print(dataFrame)

dataFrame.to_csv("frequency.csv", index=None)

list_of_words = []
for i in range(len(dataFrame)):
    if dataFrame['Frequency'][i]>0:
        list_of_words.append(dataFrame['English word'][i])

print(list_of_words)

print(len(list_of_words))

end=time.time()
print(end - start, "seconds")

with open("performance.txt", "w") as file:
    file.write("Time to process: %s seconds\n" % str(end - start))
    file.write("Memory used: %s MB" % str(psutil.Process(os.getpid()).memory_info().rss / 1024**2))
