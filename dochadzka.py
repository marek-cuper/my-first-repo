#!/usr/bin/python

cas = (time.strftime("%d/%m/%Y"))
print("Zapis svoju aktivitu v tento den.")
print("Bol si v posilke?")
posilka_1 = raw_input("0-nie, 1-ano, 2-na plavarni, 3-ina aktivita:  ")
kroky_1 = raw_input("A zadaj pocet krokov, ktore si dnes vykonal: ")

def aktivita(posilka_2, kroky_2):
	f = open(l_dochadzka, "a+")
	f.write(cas + (" aktivita: ") + posilka_2 + (", Pocet krokov: ") + kroky_2 + "\n")
	f.close

aktivita(posilka_1, kroky_1)
