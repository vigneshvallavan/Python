import difflib

print ("string-1 = abc     string-2 = abc    --> " , difflib.SequenceMatcher(None, "abc", "abc").ratio() )

print ("string-1 = abcabc  string-2 = abcdef --> " , difflib.SequenceMatcher(None, "abcabc", "abcdef").ratio() )

print ("string-1 = abc     string-2 = def    --> " , difflib.SequenceMatcher(None, "abc", "def").ratio() )

def find_similarity(a,b):
    result = difflib.SequenceMatcher(None,a,b).ratio()
    print("\nSimilarity of word '",a,"' and '",b,"' is ",result)

str1 = "how are you?"
str2 = "how r u?"
str3 = "how is your work going on?"
find_similarity(str1,str2)
find_similarity(str1,str3)
find_similarity(str2,str3)
