logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
def encrypt(text,shift):
    caeser=""
    for let in text:
            if(let>='a' and let<='z'):
                if((ord(let)+shift)>ord('z')):
                    caeser+=chr(((ord(let)+shift)%ord('z'))+ord('a')-1)
                else:
                    caeser+=chr((ord(let)+shift))
            else:
                caeser+=let
    return caeser
def decrypt(text,shift):
    caeser=""
    for let in text:
            if(let>='a' and let<='z'):
                if(ord(let)-shift<ord('a')):
                    temp=ord('a')-(ord(let)-shift)
                    caeser+=chr(ord('z')+1-temp)
                else:
                    caeser+=chr(ord(let)-shift)
            else:
                caeser+=let
    return caeser
i=0
while(i!=1):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if(direction!='encode' and direction!='decode'):
        print("No such command. Try again.")
        continue

    text = list(input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))
    caeser=""

    if(direction=='encode'):
        caeser=encrypt(text,shift)
    elif(direction=='decode'):
        caeser=decrypt(text,shift)
    
    print(f"{direction}d message: {caeser}")
    cont=input("Type 'yes' if you want to continue otherwise 'no': ").lower()
    if(cont=='no'):
        i=1
