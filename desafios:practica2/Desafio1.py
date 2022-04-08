for i in range(4):
    chain = input("Input a word: ")
    # Usando expresiones lambda
    print(f"{chain} contains letter r" if "r" in chain else f"{chain} doesn't contain letter r")
    # Sin usar expresiones lambda
    #if "r" in chain:
    #    print(f"{chain} contains letter r")
    #else:
    #    print(f"{chain} doesn't contain letter r")