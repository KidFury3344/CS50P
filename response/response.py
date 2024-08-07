import validators

input_email = input("What's your email address? ")

if validators.email(input_email):
    print("Valid")
else:
    print("Invalid")