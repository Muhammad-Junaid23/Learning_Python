# python treat strings as objects, so we can have methods/functions on the strings
# we have many built-in functions on strings like lower,upper,title,find,strip,replace

course = "python Programming"
instructor = " mosh "
print(len(course))  # print the length of string
print(course.upper())  # convert the string to uppercase
print(course.lower())  # convert the string to lowercase
print(course.title())  # convert the string to title case
print(course.capitalize())  # convert the string to capitalize
print(instructor.strip())  # it will remove the white spaces
# it will return the index of character/string to be found
print(instructor.find("s"))

# it will replace the character/string with another
print(instructor.replace("mosh", "Mosh H"))

# it will find the character/string and return true/false
print("H" in instructor)
print("mo" in instructor)

# it works the opposite of the above
print("js" not in course)
