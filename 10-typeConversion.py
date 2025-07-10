# in this file we will see type converions and trully falsy values

x = input("X : ")
print('value of X :', x)
# y = x + 6    # this will give an error cause the value x is an string and we can't add string to number
y = int(x) + 8
print('value of Y :', y)

print(f"value of X: {x} -- value of Y: {y}")

# Falsy values
# ""
# 0
# None

print(bool(""))
print(bool(0))
print(bool(None))

print(bool("False"))
