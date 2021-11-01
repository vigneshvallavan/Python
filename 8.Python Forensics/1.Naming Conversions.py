from hashlib import md5

md5_object=md5(b"vignesh vallavan") 
print("\n",md5_object.digest())          # byte equivalent of hash
print("\n",md5_object.hexdigest())       # hexadecimal equivalent of hash


str1 = "vignesh vallavan"
result = md5( str1.encode() )
print("\n",result )  
print("\n",result.hexdigest())


''' encode()    --> Converts string into bytes to be acceptable by hash fn
    digest()    --> Returns the encoded data in byte format
    hexdigest() --> Returns the encoded data in hexadecimal format
'''