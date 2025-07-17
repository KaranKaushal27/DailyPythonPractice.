
def count_string_elements(text):
    letters = 0
    digits = 0
    specials = 0

    for char in text:
        if char.isalpha():
            letters += 1

        elif char.isdigit():
            digits +=1
        else :
            specials +=1

    print("total letters is: ", letters)
    print("Total digits is: ", digits)
    print("Total special characters is : ", specials)

user_input = input("Enter a string :")
count_string_elements(user_input)

