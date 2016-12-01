#find and sort words by largest consecutive string of consonants
with open('words.txt','r') as words:
	#add the words to a set before changing it to a list so as to remove duplicates.
	wordSet = set()
	for line in words:
			if '\'' not in line:
				line = line.replace("\n","")
				wordSet.add(line.lower())
	wordList = list(wordSet)
	wordList.sort()
	vowels = ('a','e','i','o','u','y') 
	#'y' is counted as a catch-all here, generally you wont find a bunch of consonants in a row with 'y' also used as one. 'y' is interestingly not counted for the vowel count script because then the top results are things like "taiyuan", in which the 'y' is not used as a vowel
	wordConsonantList = []
	for word in wordList:
		biggestConsonantList = []
		consonantList = []
		for letter in word:
			if letter not in vowels:
				consonantList.extend(letter) #add consonant to temporary list
				if letter == word[len(word)-1] and len(consonantList) >= len(biggestConsonantList):
					biggestConsonantList = consonantList #if last letter is consonant, clear the temp list
					consonantList = []
			elif len(consonantList) >= len(biggestConsonantList): #if the last letter is a vowel, just replace biggestConsonantList with the temp one (containing the largest of that word)
				biggestConsonantList = consonantList 
				consonantList = []
			else:
				consonantList = [] 
				#this is to make sure it returns the longest string of consecutive consonants, not just the last one

		wordConsonantList.append([word,(len(biggestConsonantList))])

wordConsonantList.sort(key=lambda consonantCount: consonantCount[1])
#for word in wordConsonantList:
#	print(word)

print(wordConsonantList[5])