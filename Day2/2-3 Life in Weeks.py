# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int=(int(age))
day=(90-age_int)*365
month=(90-age_int)*12
week=(90-age_int)*52

print(f"You have {day} days, {week} weeks and {month} months left.")