def string_alternative(s):
    print("Str: ", s)

    print("Output: ", end="", flush=True)
    for i, c in enumerate(s):
        if i % 2 == 0:
            print(c, end="", flush=True)

string = str(input("Enter a string to the program: "))
string_alternative(string)

