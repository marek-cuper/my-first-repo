#!/usr/bin/python3

# vypise pole v tvare sachovnice 
def print_chessboard(board):
	for i in range(64):

		print(board[i], end=" ")
		if i%8 == 7:
			print("")



# v tomto pripade sa jedna o cistu sachovnicu
sachovnica = [0 for i in range(64)]
#print_chessboard(sachovnica)
print(" ")
# v tomto pripade sa jedna o poziciach na sachovnici 
sach = [i for i in range(64)]
#print_chessboard(sach)

sachovnica[9] = 9
#print_chessboard(sachovnica)

def print_chessboard2(height, width):
	for i in range(height * width):
		print(board[i], end=" ")
		if i%width == (width - 1):
			print("")
x = 5
t = 5
print_chessboard2(x,t)
