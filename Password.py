d = {"Pencil":"ERASERRR", "Sharpener":"GRAPHITEEEE", "Eraser":"LETITBEEEEE"}
name = input("Enter username: ")
if name in d:
    pw = input("Enter password: ")
    if pw==(d[name]):
        print("Welcome.")
    else:
        print("Faker.")
else:
    print("Go away.")