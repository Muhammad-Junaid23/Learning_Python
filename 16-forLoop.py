# for loop in python

# for number in range(5):   # it takes the initial number 0 and ends before 5
# for number in range(5, 10): # it will start from 5 and ends before 10
for number in range(1, 13, 2):  # it jumps two numbers while looping
    print("Attemting", number, number * '.')


# for loop with condition
age = 2
for number in range(3):
    print("Attempt", number)
    if age > 18:
        print('Eligible')
        break
else:
    print("Not Eligible")
