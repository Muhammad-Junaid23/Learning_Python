# we have three logical operators   AND OR NOT

high_balance = False
good_credits = True
student = True

if high_balance or good_credits and not student:
    print("Eligible")
else:
    print("Not Eligible")
