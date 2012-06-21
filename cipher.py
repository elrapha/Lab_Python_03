"""
letter = 'a'
# converts a letter to ascii code
ascii_code = ord(letter)
# convers ascii code to a letter
letter_res = chr(ascii_code)
print ascii_code, letter_res
"""
phrase= raw_input('Enter a phrase to encrypt: ')
shift= input('Enter shift value: ')

encString=''
for c in phrase:
    print 'c is ' + c
    if ord(c)>=65 and ord(c)<=90:
        temp=ord(c)-65
        temp= (temp + shift) % 26
        temp=temp+65
        encString=encString+chr(temp)
    elif ord(c)>=97 and ord(c)<=122:
        temp=ord(c)-97
        temp= (temp + shift) % 26
        temp=temp+97
        encString=encString+chr(temp)
    else:
        encString=encString+c
         
print 'Encryption ' + encString
