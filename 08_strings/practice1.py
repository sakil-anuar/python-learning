name="sakil"
university="AIUB"
message="I am learning python"
print(name)
print(university)
print(message)
print(type(name))
print(type(university))
print(type(message))

# string indexing

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print()

# Negative indexing

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])

print()

# String slicing

print(name[0:3])
print(name[1:4])
print(name[2:4])

# From start to before the limited portion

print(name[:3])


# For full string

print(name[:])

# Negative slicing

print(name[-3:])


# len()

print(len(name))
print(len(university))
print(len(message))


# .upper and .lower

print(name.upper())
print(university.lower())
print(message.upper())


# .Strip(),,,,,,,,,removing starting and ending whitespace

text=" whats up "
print(text.strip())
print(text)

# .lstrip only for removing lesft side space

print(text.lstrip())

# .rstrip() for removing right side space

print(text.rstrip())


# Replace,,,,replace()

txt="i love java"
print(txt.replace("java","python"))

# For data cleaning ,,using replace()

phone="013-0899-8386"
print(phone.replace("-",""))

# .split(),,,,,,,,string to list

say="python sql pandas"
result=say.split()

print(result)


record="sakil,Aiub,3.53"
parts=record.split(",")

print(parts[0])
print(parts[1])
print(parts[2])


# String concatenation

first_name="sakil"
last_name="anuar"

full_name= first_name + " " + last_name
print(full_name)


# F-string   string formating

name="sakil"
age=24
cgpa=3.53

print(f"My name  is{name}")
print(f"i am {age} years old.")
print(f"My cgpa is {cgpa}")

