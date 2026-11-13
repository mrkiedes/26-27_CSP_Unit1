def simple_message():
    print("Hi, Have a good day!")


def translated_message(language):
    if language == "English":
        print("Have a good day!")
    elif language == "Spanish":
        print("Tenga un buen dia")
    elif language == "French":
        print("Bonne journee")
    elif language == "Portuguese":
        print("Tenha um bom dia")


# call on the functions
simple_message()
translated_message("Portuguese")