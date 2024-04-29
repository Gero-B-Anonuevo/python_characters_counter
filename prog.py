sent = (input("Please input a string: ")).lower()

vowels = sent.count("a") + sent.count("e") + sent.count("o") + sent.count("i") + sent.count("u")

consonant = sent.count("b") + sent.count("c") + sent.count("d") + sent.count("f") + sent.count("g") 
+ sent.count("h") + sent.count("j") + sent.count("k") + sent.count("l") + sent.count("m") + sent.count("n") 
+ sent.count("p") + sent.count("q") + sent.count("r") + sent.count("s") + sent.count("t") + sent.count("v") 
+ sent.count("w") + sent.count("x") + sent.count("y") + sent.count("z")

digits = sent.count("0") + sent.count("1") + sent.count("2") + sent.count("3") + sent.count("4") + sent.count("5") 
+ sent.count("6") + sent.count("7") + sent.count("8") + sent.count("9")

specchar = len(sent) - (vowels + consonant + digits)

total = len(sent)
print(f"Number of vowels:{vowels} \nNumber of consonants:{consonant} \nNumber of digits:{digits}")
print(f"Number of special characters (including spaces):{specchar} \nTotal number of characters found on a string:{total}")