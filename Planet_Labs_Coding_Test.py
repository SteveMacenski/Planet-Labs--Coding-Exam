#Coding test for Planet Labs
# Steve Macenski October 21, 2015

#This program will use a dictionary to check an inputted word's anagrams
#then print out all possible anagrams made up of such word>4 characters

import itertools
#from sets import Set

Word = raw_input('input at least a 4 letter word with as many anagrams: '); #user input
Word = Word.lower();                                    #force input to be lowercase, to display nice
noAnagrams = False

def ErrorCheck(Word):                                   #make sure inputs are right size
    if Word == 0:
        print 'You did not input anything, try again?'
        Word = raw_input('input at least a 4 letter word with as many anagrams: ');
        ErrorCheck(Word);
    if len(Word) < 4 :
        print 'Word is less than 4 characters, of course there is no valid anagrams!'
        Word = raw_input('input at least a 4 letter word with as many anagrams: '); 
        ErrorCheck(Word);
        
def GetDictionary():
    dictionary =  open("Dictionary.txt");               
    wordlist = [];                                     
    for line in dictionary:
        wordlist.append(line[0:line.find('\n')]);       #makes a word list
    return wordlist
        
def FindingAnagramsofInputWord(wordlist):
    Letters = list(Word)                                #splits the string into its letters
    Letters_set = set(Letters);                         #makes into non-ordered set
    Anagrams = [];
    for Entry in wordlist:
        dictionaryWord = set(Entry)                    #reads in the dictionary entries as a set
        isword = True
        if len(Entry) <= len(Letters):                  #anagrams MUST be as long as or short than word input
            for all_word_letters in Letters_set:
                if Entry.count(all_word_letters) > Letters.count(all_word_letters): #anagrams MUST have <= instances of letters of word input
                    isword = False    
        if len(Entry) > len(Letters):
            isword = False   
        if isword and dictionaryWord.issubset(Letters_set) and Entry != "":
            Anagrams.append(Entry)                      #creates set of all anagrams of any length with ONLY characters of Letter_set    
    if not Anagrams:
        noAnagrams = False
    return Anagrams, noAnagrams
        

def AnagramSize(Anagrams):
    SizedAnagrams = [];
    for entry in Anagrams:
        if len(entry) >= 4:                             #limiting case of anagrams being length of 4 characters or more 
            SizedAnagrams.append(entry)
    return SizedAnagrams

def AnagramsofAnagrams(SizedAnagrams):
    entryParadise = [];
    elementParadise = [];
    final_list = [];
    index = 0;
    i = 0;
    j = 0;
    
    for entry in SizedAnagrams:
        for element in SizedAnagrams:
            entrylist = list(entry)
            entrySet = set(entrylist)
            elementlist = list(element)
            elementSet = set(elementlist)               #creates lists/set for both to compare against eachother knowing they are anagrams of inputted word
            if elementSet.issubset(entrylist) and entrySet.issubset(elementlist) and entry != element and len(entry) == len(element):
                elementParadise.append(element)
                entryParadise.append(entry)             #appending both to check against eachother

    while (i < (-2+len(entryParadise))):

        if entryParadise[i] == entryParadise[i+1]:      #finds where the pattern from the nested loops exists and exploits it
            final_list.append(elementParadise[i])
            i += 1
            
        if entryParadise[i] != entryParadise[i+1]:
            final_list.append(entryParadise[i])
            final_list.append(elementParadise[i])
            final_list.append('break')                  #break to mark end of sub-anagram chain 
            i+=1
            
    final_list.append(elementParadise[i-1])               #picking up last values where forward difference breaks down
    final_list.append(entryParadise[i-1])
    final_list.append(elementParadise[i])
    return final_list             


def PrintAnagrams(final_list):
    index = 0
    pokedex = []
    value = []
    words = []
    printer = ""
    for entry in final_list:                            #using the break, breaks the list and prints a comma deliniated listing
        if entry == 'break':
            if len(value) < len(final_list[index-1]):   #makes sure there are as many words as letters 
                value = []
                index += 1
            if len(value) >= len(final_list[index-1]):
                if value[-1] in pokedex:                #adds in a word from sub-set to check for repeats
                    value = []
                    index +=1
                    pass
                else:
                    printer = ', '.join(value)
                    pokedex.append(value[-1])
                    print printer
                    value = []                          #prints the lines
                    index += 1
        else:
            value.append(entry)                         #generates sub-set lines
            value.sort()
            index +=1
    return

         #TODO: fix case if there are no anagrams and throws line85 error.
            #(if there are some anagrams but not enough, program completes)
#calling functions
ErrorCheck(Word)
wordlist       = GetDictionary()
Anagrams, noAnagrams  = FindingAnagramsofInputWord(wordlist)
if noAnagrams:
    SizedAnagrams  = AnagramSize(Anagrams)
    final_list     = AnagramsofAnagrams(SizedAnagrams)
    PrintAnagrams(final_list)
