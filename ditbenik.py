
import datetime
naam = "stefan"
date = datetime.datetime.now()

a = "a"
b = "b"

print(date)
print("hello world!")
print("Mijn naam is " + naam + " en wie ben jij?")
print("hallo " + input())
print("Ik heb een vraagje voor je ben ik een a: appelman, b: bananenman of een c: citroenman")

print("vul in a,b of c ")

antwoord = input()

if(antwoord == a):
    print("Dat is fout, want ik hou wel van appels maar meer van citroenen.")

elif(antwoord == b):
    print("Dat is fout, want ik hou wel van bananen maar meer van citroenen.")

else:
    print("Dat is goed, citroenen zijn mijn faforieten.")

print("Oke nog een vraagje, hoe oud ben ik? Ben ik a: 18, b: 19 of c: 20 jaar?")

antwoord = input()

if(antwoord == a):
    print("Dat is goed, want ik ben inderdaad 18.")

elif(antwoord == b):
    print("Dat is fout, want ik ben 18 niet 19.")

else:
    print("Dat is fout, want ik ben 18 niet 20.")


print("Nog een laatste dan, wat zeg ik als ik wegga is het a: laters, b: joejoe of c: tot ziens?")

antwoord = input()

if(antwoord == a):
    print("Dat is fout, het was joejoe dus voor nu joejoe.")

elif(antwoord == b):
    print("Dat is goed, dus voor nu joejoe.")

else:
    print("Dat is fout, het was joejoe dus voor nu joejoe.")

