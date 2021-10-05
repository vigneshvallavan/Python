from textblob import TextBlob

str1 = input("\n\nEnter the strings : ")

l1 = list(str1.split(" "))

result = []

for word in l1:
    result.append( TextBlob(word) )

print("\nSpell Corrector   : ",end = "")

for word in result:
    print(word.correct(), end = " ")

