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

# v tomto pripade sa jedna o poziciach na sachovnici 
sach = [i for i in range(64)]
#print_chessboard(sach)

sachovnica[9] = 9
print_chessboard(sachovnica)

print(" ")
	

sachovnica[9+8] = 9
sachovnica[9] = 0
print_chessboard(sachovnica)

