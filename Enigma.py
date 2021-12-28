# -*- coding: utf-8 -*-

# -- Sheet --

from random import*

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def shuffle_alphabet(): # Return static rotor
    rotor1=alphabet.copy()
    shuffle(rotor1)
    return rotor1
"""
First step : Search the letter in alphabet. Save his index
Second step : Search in the first rotor the associate letter
Third step : Search this last letter in the alphabet and save his index
Fourth step : Search in the second rotor the index of third step
Fifth step : Return the letter
"""
def code(a,b,m): #Input : 2 rotors and a message
    code_mess=[]
    
    for i in range(len(m)):
    
        if m[i]==' ':
            code_mess.append(' ')
            continue

        for j in range(len(alphabet)):
            if alphabet[j]==m[i]:
                tmp=j #Index - First step done.
        
        indRotor1=a[tmp] #Second step - Done

        for k in range(len(alphabet)):
            if alphabet[k]==indRotor1:
                tmp1=k # Third step - Done
        
        indRotor2=b[tmp1]

        code_mess.append(indRotor2)

    for l in range(len(code_mess)):
        print(code_mess[l],end='')
    print("")

    #Return

"""
First step : Search the letter in the second rotor. Save his index
Second step : Search in the alphabet at the index
Third step : Search the letter in the first rotor and save his index
Fourth step : Search in the alphabet at this last index
"""
def decode(a,b,m): # Input : 2 rotors (same as in code algorithme) and the crypted message
    decode_mess=[]
    for i in range(len(m)):
    
        if m[i]==' ':
            decode_mess.append(' ')
            continue

        for j in range(len(b)):
            if b[j]==m[i]:
                tmp=j #First step - Done

        alphaPosi=alphabet[tmp] #Second step - Done

        for k in range(len(a)):
            if a[k]==alphaPosi:
                tmp1=k #Third step - Done

        finalLetter=alphabet[tmp1] #Fourth step - Done

        decode_mess.append(finalLetter) 
    
    for l in range(len(decode_mess)):
        print(decode_mess[l],end='')

    print("")

def rotation(a):
    b=a.copy()
    for m in range(len(a)):
        if m==len(a)-1:
            b[0]=a[m]
        else:
            b[m+1]=a[m]
    return b

def rotation_finale(a,b): #Temporaire
    compt_rota=0
    rota_b=0
    if compt_rota==(len(a)-1):
        b=rotation(b)
        a=rotation(a)
        print(a)
        print(b)
        compt_rota+=1
        rota_b+=1
        print("compteur : ",compt_rota)
        print("Rotation de b : ",rota_b)
        print("")
        compt_rota=0
    else:
        a=rotation(a)
        print(a)
        print(b)
        compt_rota+=1
        print("compteur : ", compt_rota)
        print("Rotation de b : ",rota_b)
        print("")



def code_enigma(a,b,m):
    compt_rota=0
    rota_b=0
    code_mess=[]
    
    for i in range(len(m)):
    
        if m[i]==' ':
            code_mess.append(' ')
            continue

        for j in range(len(alphabet)):
            if alphabet[j]==m[i]:
                tmp=j #Index - First step done.
        
        indRotor1=a[tmp] #Second step - Done

        for k in range(len(alphabet)):
            if alphabet[k]==indRotor1:
                tmp1=k # Third step - Done
        
        indRotor2=b[tmp1]
        code_mess.append(indRotor2)
    
        if compt_rota==(len(a)-1):
            b=rotation(b)
            a=rotation(a)
            rota_b+=1
            compt_rota=0
        else:
            a=rotation(a)
            compt_rota+=1
        

    for l in range(len(code_mess)):
        print(code_mess[l],end='')
    print("")

    return code_mess

    

saveRotor1=['f', 'g', 'r', 'o', 'w', 'd', 'c', 'i', 'y', 't', 'p', 'z', 'u', 'a', 'h', 'm', 'l', 'q', 's', 'j', 'b', 'x', 'k', 'n', 'v', 'e']
saveRotor2=['u', 'i', 'f', 'e', 'w', 'x', 'z', 't', 'n', 'j', 'q', 'a', 'm', 's', 'h', 'c', 'l', 'o', 'v', 'd', 'b', 'y', 'g', 'k', 'p', 'r']
print(alphabet)
print("")
print(saveRotor1)
print(saveRotor2)
print("")


code(saveRotor1,saveRotor2,"je suis en classe de nsi")
decode(saveRotor1,saveRotor2,"dg vipv gu orxvvg hg uvp")

