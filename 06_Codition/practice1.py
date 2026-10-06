# If-Else condition

age=15
if age>=18 :
    print("Adult")

else:
    print("Minor")


 # From user input ,,,,If-Else

age=int(input("Please Enter your age: "))

if age>=18 :
    print("You are a adult persion")
else:
    print("You are a minor persion")



# Even Odd number checking

number=int(input("Please Enter a number: "))

if number %2==0:
    print("Even number")
else:
    print("Odd number")

# Elif condition

marks=75

if marks >=90 :
    print("Excellent")
elif marks>=80:
    print("Good")
elif marks==50:
    print("Only pass")
else:
    print("Fail")


# Grade calculation taking a number from user input

marks=int(input("Please Enter a marks: "))

if marks>=80:
    print("You got A+")
elif marks>=70:
    print("You got A")
elif marks>=60:
    print("You got B")
elif marks>=55:
    print("You got C")
elif marks>=50:
    print("You got D")
else:
    print("You are fail")


# Multiple condition And

age=24
cgpa=3.50

if age>=22 and cgpa>=2.50:
 print("You are eligable")
else:
    print("You are not eligable")


# Another exaple

day="Friday"

if day=="Friday" or day=="Saturday":
    print("Today is weekend")
else:
    print("Today is working day")


# If with String

password="12345"

if password=="12345":
    print("Login successful!")
else:
    print("Login is fail")


# Nested if 

age=23
cgpa=3.53

if age>=22:
    if cgpa>=3.00:
        print("Eligable")
    else:
        print("Cgpa is too low")
else:
    print("Age is too low")


# Positive , Negative number checking
    number = int(input("Enter a number: "))

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")








