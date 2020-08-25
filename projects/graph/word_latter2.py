from util import Stack, Queue  
# These may come in handy

# Given two words (begin_word and end_word), and a dictionary's word list, 
# return the shortest transformation sequence from begin_word to end_word, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:

# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']

# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

# beginWord = "hungry"
# endWord = "happy"
# None
f = open('words.txt', 'r')
words = f.read().lower().split("\n")
f.close()

# Put our words in a set for O(1) lookup
word_set = set()
for word in words:
      word_set.add(word.lower())

def get_neighbors(word):
    '''
    Get all words thare one letter
    away from the given word
    '''
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    results = []
    list_word = list(word)
    # go through each letter in the word
    for i in range(len(list_word)):
    # swap with each letter in the alphabet
        for letter in letters:
            # check if that equals given word
            temp_word = list_word.copy()
            temp_word[i] = letter
            joined_word = "".join(temp_word)
            if joined_word in word_set and joined_word != word:  
                results.append(joined_word)
    return results

print(get_neighbors("dog"))

# def words_are_neighbors(w1, w2):
#     # return true of letters are one word apart
#     # otherwise return false
#     # convert the word into a list
#     letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#     list_word = list(w1)
#     # go through each letter in the word
#     for i in range(len(list_word)):
#     # swap with each letter in the alphabet
#         for letter in letters:
#             # check if that equals given word
#             temp_word = list_word.copy()
#             if "".join(temp_word) == w2:
#                 return True
#     return False 

# alternative
# def words_are_neighbors(w1, w2):
#     list_word1 = list(w1)
#     list_word2 = list(w2)

#     print(f"comparing {w1} - {w2}")
#     if len(w1) != len(w2):
#         return False
#     for i in range(len(w1)):
#         # print(f"{w1[:i]}{w2[:i]}{w1[:i + 1]}{w2[:i + 1]}")
#         if w1[:i] == w2[:i] and w1[:i + 1] == w2[:i + 2]:
#             return True 
#     return False 

# def words_are_neighbors(w1, w2)
#     for in range(len(w1)):
#         list_word1 = list(w1)
#         list_word2 = list(w2)
#         list_word1.pop(i)
#         list_word2.pop(i)
#           if list_word1 == list_word1:
#             return True 

neighbors = {}
# go through each word
# for word in words:
#     neighbors[word] = set()
#     # go through each potential neighbor
#     for potenitial_neighbor in words:
#         # add potential neighbor if they match  
#         if words_are_neighbors(word, potenitial_neighbor):
#             neighbors[word].add(potenitial_neighbor)



def word_ladder(begin_word, end_word):
    # crate a queue
    q = Queue()
    # enqueue a path to the starting word
    q.enqueue([begin_word])
    # create a visited set
    visited = set()
    # while queue is not empty...
    while q.size() > 0:
        # dequeue path 
        path = q.dequeue()
        # grab the last word from the path
        w = path[-1]
        # check if it is our target word
        if w == end_word:
            return path 
        # check if it has been visited
        # if not, mark as visited
        if w not in visited:
            visited.add(w)
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)

print(word_ladder("rat", "bar")) 
print(word_ladder("sail", "boll")) 