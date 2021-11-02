import hashlib  
import uuid  

# Function for encoding user password and added with random string  

def hash_pass(password):  
    s = uuid.uuid4().hex        # Gives random hexadecimal string
    pswrd_encode = hashlib.sha256( s.encode() + password.encode() ).hexdigest() + ':' + s  
    return pswrd_encode

# Function for verifying user password with hashed password

def verify_password(hashed_password, user_password):  
    password, s = hashed_password.split(':')  
    return password == hashlib.sha256(s.encode() + user_password.encode()).hexdigest() 


new_password = input('Enter your password :')    
hashed_password = hash_pass(new_password)  
print('The hash string to store in the db is: ' + hashed_password)


old_password = input('Enter new password ')  
if verify_password(hashed_password, old_password):  
    print('Entered password is correct')  
else:  
    print('Passwords do not match')  