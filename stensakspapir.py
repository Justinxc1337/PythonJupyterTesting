import random

bruger = input("Vælg sten, saks eller papir: ")

komputer = random.choice(["sten", "saks", "papir"])

print(f"Komputeren valgte {komputer}")
print(f"Brugeren valgte {bruger}")
print("\n")

if bruger == komputer:
    print("Det blev uafgjort")
elif bruger == "sten":
    if komputer == "saks":
        print("Brugeren vandt")
    else:
        print("Komputeren vandt")
elif bruger == "saks":
    if komputer == "papir":
        print("Brugeren vandt")
    else:
        print("Komputeren vandt")
elif bruger == "papir":
    if komputer == "sten":
        print("Brugeren vandt")
    else:
        print("Komputeren vandt")
else:
    SyntaxError
    print("fejl, bruger valgte ikke sten, saks eller papir")