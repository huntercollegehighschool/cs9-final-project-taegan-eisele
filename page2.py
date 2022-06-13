#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.

import random
print("My First Day of School")

word1=input("Choose an adjective: ")
word2=input("Choose a present tense verb: ")
word3=input("Choose a positive integer: ")
while not word3.isdigit(): 
  word3=input("Please enter a positive integer: ")
word4=str(int(word3)-(random.randint(1, int(word3)-1)))
word5=input("Choose a number: ")
word6=input("Choose a body part: ")
word7=input("Choose an adjective: ")
word8=input("Choose a person: ")
word9=input("Choose an adjective: ")
word10=input("Choose an adjective: ")

print("My first day of school was totally "+word1+". The teacher made us "+word2+" "+word3+" times, and when I tried to get away with only "+word4+" times, the teacher hit me "+word5+" times on my "+word6+". Now I'm completely "+word7+". "+word8+" tells me I'll be "+word9+" again by tomorrow, but I still do NOT want to go back to that "+word10+" school.")