# Exercise #1
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']
def rev_list(words):
    words.reverse()
    count = 0
    for word in words:
        word_rev = word [::-1]
        words[count] = word_rev
        count += 1
    return words

# print(rev_list(words))





# Exercise #2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def count_word_occurances(a_text):
    hist = {}
    for word in a_text.split():
        word = word.strip(",.").lower()
        if word not in hist.keys():
            hist[word] = 1
        else:
            hist[word] += 1
    return hist
    
# print(count_word_occurances(a_text))





# Exercise #3
# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

# Hint: Linear Searching will require searching a list for a given number.

list_to_search = [1,5,2,7,4,8,3,9,5,44,55,2,444,7,443,72,48,94]

def linear_search(input_list, target):
    count = 0
    for item in input_list:
        if item == target:
            return f"{target} is at index {count}."
        count += 1
    return f"{target} is not in the list." 

# print(linear_search(list_to_search, 94))

#Time Complexity is O(n).