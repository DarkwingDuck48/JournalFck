import json


def ShowAllAcc(mappings):
    for acc in mappings.keys():
        print(acc)


# Read mappings for accounts
with open("Mapping.json", "r", encoding="utf-8") as file:
    alldict = json.load(file)
    mappings = alldict["Mappings"]

# ShowAllAcc(mappings)
acc = input("Check acc - ")
if acc in mappings.keys():
    print("Added")
else:
    print("Not Add")
