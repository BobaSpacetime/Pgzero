vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}
word = input("Gimme a word and I shall count your vowels 👹👺 ")
for i in word:
    print(i)
    if i in vowels:
        vowels[i]+=1
print(vowels)