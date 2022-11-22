def are_anagrams(word1, word2):
	'''return true if words are anagrams'''
	word1_sorted = sorted(word1)
	word2_sorted = sorted(word2)
	return word1_sorted == word2_sorted

print('Anagram Solver')

two_words = input("Enter two space separated words: ")
word1, word2 = two_words.split()

if are_anagrams(word1,word2):
	print("The words are anagrams")
else:
	print("The words are not anagrams")
