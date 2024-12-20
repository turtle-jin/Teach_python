

name1 = input("What is your name?")
name2 = input("What is his/her name?")

combined_names = name1 + name2

name_string = combined_names.lower()

t = name_string.count('t')
r = name_string.count('r')
u = name_string.count('u')
e = name_string.count('e')

true = t + r + u + e

l = name_string.count('l')
o = name_string.count('0')
v = name_string.count('v')
e = name_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love)) 

if love_score < 10 or love > 90:
    print(f"Your love score is {love_score} and you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score} and you are alright together")
else:
    print(f"Your love score is {love_score}")
