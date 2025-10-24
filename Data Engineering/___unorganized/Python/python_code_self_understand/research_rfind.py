import string
from collections import Counter

sample_passage = '''
In the 16th century, an age of great marine and terrestrial exploration, Ferdinand Magellan led the first expedition to sail around the world. As a young Portuguese noble, he served the king of Portugal, but he became involved in the quagmire of political intrigue at court and lost the king’s favor. After he was dismissed from service by the king of Portugal, he offered to serve the future Emperor Charles V of Spain.

A papal decree of 1493 had assigned all land in the New World west of 50 degrees W longitude to Spain and all the land east of that line to Portugal. Magellan offered to prove that the East Indies fell under Spanish authority. On September 20, 1519, Magellan set sail from Spain with five ships. More than a year later, one of these ships was exploring the topography of South America in search of a water route across the continent. This ship sank, but the remaining four ships searched along the southern peninsula of South America. Finally they found the passage they sought near 50 degrees S latitude. Magellan named this passage the Strait of All Saints, but today it is known as the Strait of Magellan.
'''


# Trying to find the number of times each word appears
def remove_punctuations(text:str) -> str:
    strings= list(string.punctuation) #convert every punctuation to a list
    no_trans = ["" for i in range(0,len(string.punctuation))] #make emppty string for the length of punctuation string

    sam_dic = dict(zip(strings, no_trans)) #create a dictionary for passing to `maketrans`
    trans_table = str.maketrans(sam_dic) #creating the translation table

    return text.translate(trans_table) #translate here


formatted_str = remove_punctuations(sample_passage)

def count_of_words(ls:list) -> dict:
    words_counted = Counter(ls)
    return words_counted

words_coiunted = count_of_words(formatted_str.split(" "))

# print(words_coiunted)


# Researching `rfind` method

print(sample_passage.rfind('the')) # To find the index of the last occurence of the substring
print(sample_passage.rfind('the', 0, 100)) # To find the index of the last occurence between 0th and 100th indices
print(sample_passage.rfind('the', 90, 140)) # To find the index of the last occurence between 90th and 130th indices



