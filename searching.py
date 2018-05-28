#!/usr/bin/python


def binary_search(hladane,list):
        cast = len(list)-1
        posun = 0
	pocet_krokov = 0
        for i in range(1,len(list)):
                pocet_krokov += 1
		if hladane == list[cast + posun]:
                        pozicia = cast + posun
                        break
                if hladane >= list[cast+posun]:
                        posun = posun + cast
                else:
                        cast = cast /2
	print("Binarne vyhladavanie")
	print("pocet krokov: " + str(pocet_krokov))
        print("pozicia cisla: " + str(pozicia) + "." + "\n")


def sequence_search(hladane,list):
	pocet_krokov = 0
	for i in range(1,len(list)):
		pocet_krokov += 1
		if list[i] == hladane:
			pozicia = i
			break

        print("Sekvencne vyhladavanie")
        print("pocet krokov: " + str(pocet_krokov))
        print("pozicia cisla: " + str(pozicia) + "." + "\n")







zoznam = []
for i in xrange(1,1001):
	zoznam.append(i)
print zoznam

cislo = input("Napiste lubovolne cislo zo zoznamu vysie a vypise vam poziciu v zozname:  ")
print(" ")

sequence_search(cislo,zoznam)
binary_search(cislo,zoznam)



