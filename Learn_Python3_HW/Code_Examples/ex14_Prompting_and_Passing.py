# imports argv from the system library
from sys import argv

# declare variables for the argv parameters
script, user_name = argv

# pre-define the prompt to be reused later
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")

likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about like me.
You live in {lives}. Not sure wher that is.
And you have a {computer} computer. Nice.
""")
