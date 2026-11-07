digit_0 = "###\n# #\n# #\n# #\n###\n"
digit_0 = digit_0.split("\n")

digit_1 = "  #\n  #\n  #\n  #\n  #\n"
digit_1 = digit_1.split("\n")

digit_2 = "###\n  #\n###\n#  \n###\n"
digit_2 = digit_2.split("\n")

digit_3 = "###\n  #\n###\n  #\n###\n"
digit_3 = digit_3.split("\n")

digit_4 = "# #\n# #\n###\n  #\n  #\n"
digit_4 = digit_4.split("\n")

digit_5 = "###\n#  \n###\n  #\n###\n"
digit_5 = digit_5.split("\n")

digit_6 = "###\n#  \n###\n# #\n###\n"
digit_6 = digit_6.split("\n")

digit_7 = "###\n  #\n###\n # \n#  \n"
digit_7 = digit_7.split("\n")

digit_8 = "###\n# #\n###\n# #\n###\n"
digit_8 = digit_8.split("\n")

digit_9 = "###\n# #\n###\n  #\n###\n"
digit_9 = digit_9.split("\n")

digits = [digit_0, digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9]

user_number = input("Write your digit:")

for row in range(5):
    for char in user_number:
        digit_index = int(char)
        print(digits[digit_index][row], end=" ")
    print()
