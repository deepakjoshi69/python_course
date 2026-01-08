'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.'''

spam_messages = ["Make a lot of money", "buy now", "subscribe this", "click this"]
messages = input("Enter the message: ")

for i in spam_messages:
    if i == messages:
        print("This is a spam message")
        break
else:
    print("This is not a spam message")