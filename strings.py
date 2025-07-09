# triple qoutes are used for formatting long strings
# single and double qoutes for string

course = "python crash course"
instructor = 'Mosh'
message = """ 
Hi Mosh!

This is Unknown-404 from Not found

Hope you are doing fine...
"""

print("Course : ", course)
print("Instructor : ", instructor)
print("Message : ", message)


# len function take an argument as input and returns the length of it
print(len(course))

print(course[5])    # This will provide us a specific letter on that index
print(course[-4])   # This will count from the last index

# This will slice from the string and return a new string
print(course[3:13])
print(course[3:])    # This will slice from the index 3 till the end of string

# This will slice from the start till the index 15 of string
print(course[:15])

print(course[:])  # This will return a new copy of the string
