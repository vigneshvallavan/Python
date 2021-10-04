import re

file = open("file-with-url.txt","r")
output = open("url_extract.txt","w")

print("\n\n\nFILE --> file-with-url.txt\n")
for a in file:
    print(a)

print("\n\n\n_____urls in file-with-url.txt_____\n")
file = open("file-with-url.txt","r")
for b in file:
    urls = re.findall(r' (https?://\S+)', b)
    print(urls)
                                            # put urls in to new file -- output (url_extract.txt)
    for x in urls:
        output.writelines("%s\n"%x)         # %s\n --> new line for next string
     
print("\n\n\nFILE --> output.txt\n")
output = open("url_extract.txt","r")        # change output file mode to read
for c in output:
    print(c)
    