# - *- coding: utf- 8 - *-

from textblob import TextBlob

word = TextBlob('தமிழ்')
print(word.detect_language())

word = TextBlob('Welcome')
print(word.detect_language())

word = TextBlob('स्वागत हे')
print(word.detect_language())

word = TextBlob('أهلا بك')
print(word.detect_language())

word = TextBlob('സ്വാഗതം')
print(word.detect_language())

