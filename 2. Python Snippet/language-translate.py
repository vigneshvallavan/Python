# - *- coding: utf- 8 - *-

from textblob import TextBlob

word = TextBlob('தமிழ்')
a = word.detect_language()
print(word," --> ",word.translate(from_lang = a, to = 'en'))

word = TextBlob('Welcome')
a = word.detect_language() 
print(word," --> ",word.translate(from_lang = a, to = 'ta'))

get_word = input("Enter a word to convert into Tamil :")
word = TextBlob(get_word)
a = word.detect_language() 
print(word," --> ",word.translate(from_lang = a, to = 'ta'))
