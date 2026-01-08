dictionary = {
    "Abundant": "Available in large quantity",
    "Brave": "Showing courage and not afraid",
    "Curious": "Eager to know or learn something",
    "Delicate": "Easily broken or damaged",
    "Efficient": "Doing work in a well-organized way with less effort",
    "Genuine": "Real and honest",
    "Humble": "Not proud; modest",
    "Journey": "Travel from one place to another",
    "Loyal": "Faithful and trustworthy",
    "Wisdom": "Ability to make good decisions based on knowledge and experience"
}
choise = input("do yoy want to see a word meaning? (yes/no): ")
if choise.lower() == "yes":
    word = input("Enter the word you want to know the meaning of: ")
    meaning = dictionary.get(word)
    if meaning:
        print(f"The meaning of '{word}' is: {meaning}")
    else:
        print(f"Sorry, the word '{word}' is not in the dictionary.")