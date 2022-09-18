import main

while True:
    text = input('አቡጊዳ >> ')
    if text.strip() == '': continue
    result, error = main.run('<stdin>', text)

    if error: 
        print(error.message())
    elif result: 
        if(len(result.elements)) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))