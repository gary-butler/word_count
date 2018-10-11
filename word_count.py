from os import path
import csv
import re

#change "sample.txt" to your text input file
text_infile = "sample.txt"

#change "word_freq.csv" if you want a different output .csv file
file_path = 'word_freq.csv'

#get text from infile
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d, text_infile)).read()

#use regex to remove special characters, and just in case force unicode text
text = re.sub(r"[().!?,:'\"]", " ", text).encode('utf-8').decode('utf-8')

#get list of words from text data
wordlist = text.split()

#initialize the array that will contain the word frequencies
wordfreq=[]

#count the instances of each word in the text
for w in wordlist:
    wordfreq.append(wordlist.count(w))

#combine our list of words and word counts into a single list
wfreqlist = list(zip(wordlist, wordfreq))

#reorder the combined words and word counts list
wfreqlist.sort()

#get the last word from the combined list to check for duplicates
last = wfreqlist[-1]

#iterate from the end to the beginning of the combined list
for i in range(len(wfreqlist)-2, -1, -1):
    
    #if the check word is in the list again remove it, otherwise get the next word to check
    if last == wfreqlist[i]:
        del wfreqlist[i]
    else:
        last = wfreqlist[i]

#uncomment this line to see the list of words and their frequencies
#print(wfreqlist)

#create or overwite existing .csv output file
with open(file_path, mode='w') as count_file:
    w_writer = csv.writer(count_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    #label the columns
    w_writer.writerow(['word', 'frequency'])

    #iterate through the list of words and frequencies adding each to the new .csv file
    for i in range(len(wfreqlist)):
        text = wfreqlist[i][0]
        freq = wfreqlist[i][1]
        w_writer.writerow([text, freq])