temperature = 65
if temperature > 80 :
    print("It's too hot!!")
    print("Stay Inside")
elif temperature > 55 :
    print ("Still quite hot!!")
else :
    print("Have a nice day")

#grade 80 print you are brilliant
#60 print you display better luck next time
user = input ("What is your name?")
greeting = "Hi" + " " + user
mark = int(input ("What is your mark?\n"))
grade = str(input ("What is your grade?\n"))

if mark > 79 :
    print("you are brilliant!!")
elif mark < 61 :
    print("Better luck next time")
else :
    print("Keep it up!!")

print(greeting + ",your marks is " + str(mark) + ",your grade is " + str(grade))