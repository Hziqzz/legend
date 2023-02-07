#Mohd Nur Haziq Bin Dahia
#014-9002960
#mohdnhaziq04@gmail.com

name = input ("What is your name?")
greeting = "Hello" + " " + name
print(greeting)

weight = float(input ("What is your weight?\n"))
height = float(input ("What is your height?\n"))
#BMI = weight / (height*height)
BMI = weight/(height*height)
print(name + " " + ",your BMI is" + str(BMI))

#Develop a software to calculate Sales
#1)Ask name of user
#2)Ask for How many percent is the sales Tax,How much is the price of the goods
#sales tax = percentage of tax * price amount of good
#3)The output: "Hi xxxxx , the total amount to pay is xxxx, the sales tax is xxxx
#sales amount = total sales + sales tax
#barang $1500 tax 6.25% maka nilai keseluruhan ialah 1631.25

user = input ("What is your name?")
greeting = "Hi" + " " + user
tax = float (input("How many percent is the sales Tax?\n"))
price = int (input("How much is the price of the goods?\n"))
salestax = (tax/100) * price
salesamount = price + salestax
print(greeting + " " + ",the total amount to pay is " + str(salestax) + "the sales tax is " + str(tax))
print(salesamount)

#name,student id,c-> F
#ask the user for input
#Change the c to F(fahrenheit = (celsius * 1.8) + 32)

user = input ("What is your name?")
greeting = "Hi" + " " + user
celsius = float (input("What is the current temperature in celsius?\n"))
fahrenheit = (celsius * 1.8) + 32
print(greeting + " " + ",the current temperature in celsius is " + str(celsius) + "the current temperature in fahrenheit is" + str(fahrenheit))