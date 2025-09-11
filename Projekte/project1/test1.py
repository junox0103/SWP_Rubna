from numba.cuda.printimpl import int_print_impl

print("Name:")
name = input()
if name == "Julian":
    print("Hallo Julian du Sigma!")
elif name == "leon":
    print("Leon geh weg!")

while (True):
    print("Was willst du machen ?")
    print("1. Addieren")
    print("2. Subtrahieren")
    print("3. Exit")
    print("4. Name anzeigen")
    auswahl=input()
    if auswahl=="1":
        print("Zahl 1 eingeben:")
        zahl1=int(input())
        print("Zahl 2 eingeben:")
        zahl2=int(input())
        print("Ergebnis: " + str(zahl1+zahl2))
    elif auswahl=="2":
        print("Zahl 1 eingeben:")
        zahl1 = int(input())
        print("Zahl 2 eingeben:")
        zahl2 = int(input())
        print("Ergebnis: " + str(zahl1 - zahl2))

    elif auswahl=="3":
        break

    elif auswahl=="4":
        print(name)
        continue

print("Wie weit wollen sie zählen?")
zahl=int(input())
i=0;
for i in range(zahl):
    i=i+1
    print(i)

def neueFunkion():
    pass

print("Gib eine zahl ein")

try:
    nummer = int(input())

except:

    print("Expected")
else:
    print("Sie gaben eine Zahl an")
finally:
    print("Prozess beendet")
