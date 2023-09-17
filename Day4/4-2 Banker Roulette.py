# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
a=len(names)
b=int(random.randint(0,a-1))
person=names[b]
print(f"{person} is going to buy the meal today!")