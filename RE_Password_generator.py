import random
import re
import secrets
import string

def generate_password(length=16,nums=1,special_chars=1,uppercase=1,lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    #print(all_characters)
    #print(secrets.choice(all_characters))

    while True:
        password = ""
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
            constraints = [(nums,r'\d'),
                           (lowercase,r'[a-z]'),
                           (uppercase),r'[A-Z]',
                           (special_chars),fr'[{symbols}]']
            # Check constraints

            #count = 0
            #for constraint, pattern in constraints:
            #    pass_len = len(re.findall(pattern,password))
            #    if constraint <= pass_len:
            #        count += 1
            #if count == 4:
            #    break
            if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints):
                break 
        return password
    
#pattern = re.compile('l+')
quote = "Not all those who wander are lost."
#print(pattern.search(quote))#
pattern = r'\W'
#print(re.search(pattern,quote))
#print(re.findall(pattern,quote))

def main():
    print(generate_password(8,2,2,2,2))
main()
