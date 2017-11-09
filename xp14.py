def remove_dups(L1, L2):
	L3 = L1[:]
	for e in L3:
		if e in L2:
			L1.remove(e)
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]


remove_dups(L1, L2)

print(L1)
