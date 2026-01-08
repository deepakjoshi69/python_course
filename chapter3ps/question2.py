# program to fill details in letter template

# name = input("Enter your name: ")
# date = input("Enter the date: ")

# letter = f'''
# Dear {name},
# This is to inform you that your appointment is scheduled on {date}.
# Please be on time.'''

# print(letter)

letter = '''Dear <|name|>,
This is to inform you that your appointment is scheduled on <|date|>.
Please be on time.'''
print(letter.replace("<|name|>", input("Enter your name: ")).replace("<|date|>", input("Enter the date: ")))