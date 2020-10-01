#Given a string, remove the vowels from the string and return the string without vowels.
#Input : what is your name ?
#Output : wht s yr nm ?

#Homemade whith love in python 2.7

vowels=["a","e","i","o","u","A","E","I","O","U"]
text = "Hello my name is kevin"
print(text)

for i in text: 
    if i in vowels:
        i=i
    else:
        print i,