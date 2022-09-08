from re import T
import main

while True:
    text = input('basic >> ')
    result, error = main.run('<stdin>', text)

    if error: print(error.message())
    else: print(result)


# hello = 'ሃለመሰረሰሸቀበተቸኘአከሀወዘጀየደገፐፈቨ'
# test = 'ሃለመሰረሰሸቀበተቸኘአከሀወዘጀየደገፐፈቨ'
# print(hello, test)
# print(hello == test)