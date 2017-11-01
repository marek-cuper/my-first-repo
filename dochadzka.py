#!/usr/bin/python


from time import strftime


dochadzka_file = "posilka.txt"


def aktivita(posilka, kroky):
	f = open(dochadzka_file, "a+")
	f.write(strftime("%d/%m/%Y") + (" aktivita: ") + posilka + (", Pocet krokov: ") + kroky + "\n")
	f.close


print("Zapis svoju aktivitu v tento den.")
print("Bol si v posilke?")

posilka = raw_input("0-nie, 1-ano, 2-na plavarni, 3-ina aktivita:  ")
kroky = raw_input("A zadaj pocet krokov, ktore si dnes vykonal: ")

aktivita(posilka, kroky)

