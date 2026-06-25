s=input("Enter a string:")
vowels=""
consonants=""
vowel_count=0
consonant_count=0
for i in s:
    if i in "aeiouAEIOU":
       vowel_count+=1
       vowels+=i
    else:
         consonant_count+=1
         consonants+=i
print("Number of vowels in a given string is",vowel_count)
print("The vowels present are:",vowels) 
print("Number of consonants in a given string is",consonant_count)
print("The consonants are present in the given string:",consonants)    

        
