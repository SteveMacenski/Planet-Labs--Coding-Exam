# Planet-Labs--Coding-Exam
Coding Test in Python for Planet Labs


"An anagram is a word formed by rearranging the letters of another, like "topside" and "deposit". In some cases, there might be as many (or more) anagrams than there are characters, like "post", "spot", "stop" and "tops".

Write a program to find all of the anagrams in a dictionary in which there are at least 4 letters in the word and at least as many anagrams as there are letters.

The dictionary will be a file on disk with one line per word. Your operating system likely already has such a file in /usr/dict/words or /usr/share/dict/words.

The output produced by your code should be in this format:

emit, item, mite, time

merit, miter, mitre, remit, timer

reins, resin, rinse, risen, serin, siren

inert, inter, niter, retin, trine

inset, neist, snite, stein, stine, tsine"


So... rules are: 

1. Find anagrams of input 

2. Find all anagrams making up any number of letters of the input (since sample output has lines of multiple numbers of characters)

3. Compare these anagrams to a dictionary (file I used attached to repo)

4. Anagrams must be 4 characters long 

5. For each n letter combination, there must be n+ words, where n>=4

6. Prints lines where each line is in alphabetical order 

7. Prints lines such that each line is made up of the same letters in different combinations 

8. Have fun :-) overall, it was a nice afternoon project, would recommend. 

NOTE: Dictionary I used has words missing from sample output so sample output.png has different results


MIT License and all, feel free to use for all of your word-manipulating needs. Throw me a line if you think of something cool to use this for, I would love to hear about it. 
