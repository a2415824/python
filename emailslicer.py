email=input("Enter your Email: ".strip())
username=email[:email.index('@')]
domain=email[email.index('@')+1:]
print(f"your username is {username} & domain is {domain}")