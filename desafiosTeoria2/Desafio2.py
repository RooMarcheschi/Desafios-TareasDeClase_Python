chain = input("Input a word: ")
while chain.upper() != "FIN":
    print(f"{chain} follows the rule" if chain[0] == chain[len(chain)-1] else f"{chain} doesn't follow the rule")
    chain = input("Input a word: ")