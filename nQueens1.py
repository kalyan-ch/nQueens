import random
import copy
import time

def generateState(n):
	b_st = []

	for x in range(n):
		temp = [0 for z in range(n)]
		temp[random.randint(0,n-1)] = 1
		b_st.append(temp)
	
	return b_st

def findQueens(board):
	oneArr = []

	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == 1:
				oneArr.append(""+str(i)+","+str(j))
	
	return oneArr

def printBoard(board):
	for x in board:
		for y in x:
			print y,
		print ""

def slopeCal(x,y,x1,y1):
	slope = (y1-y)/(x1-x)
	return slope

def calConflicts(oneArr):
	if len(oneArr) > 0:
		hcnf = 0
		vcnf = 0
		dCnf = 0
		for x in oneArr:
			for y in oneArr:
				coArr = x.split(",")
				oI = float(coArr[0])
				oJ = float(coArr[1])
				coArr = y.split(",")
				otI = float(coArr[0])
				otJ = float(coArr[1])
				if not ((oI == otI) and (oJ == otJ)):
					#horConflts
					if oI == otI:
						hcnf += 1
					#verConflts
					elif slopeCal(oI,oJ,otI,otJ) == 0:
						vcnf += 1
					#diaConflts
					elif (slopeCal(oI,oJ,otI,otJ) == 1) or (slopeCal(oI,oJ,otI,otJ) == -1):
						dCnf += 1

		return (hcnf/2)+(vcnf/2)+(dCnf/2)

def getPsblMvs(crd, n):
	psArr = []
	crdAr = crd.split(",")
	oI = int(crdAr[0])
	oJ = int(crdAr[1])
	
	#horLeft
	oJ = oJ-1
	while (oJ != -1):
		str2 = ""+str(oI)+","+str(oJ)
		if curBoard[oI][oJ] == 0:
			psArr.append(str2)
		elif curBoard[oI][oJ] == 1:
			break
		
		oJ = oJ-1
	
	#horRight
	oI = int(crdAr[0])
	oJ = int(crdAr[1])
	oJ = oJ+1
	while (oJ != n):
		str2 = ""+str(oI)+","+str(oJ)
		if curBoard[oI][oJ] == 0:
			psArr.append(str2)
		elif curBoard[oI][oJ] == 1:
			break
		
		oJ = oJ+1

	#verUp
	oI = int(crdAr[0])
	oJ = int(crdAr[1])
	oI = oI-1
	while (oI != -1 and oI != n):
		str2 = ""+str(oI)+","+str(oJ)
		if curBoard[oI][oJ] == 0:
			psArr.append(str2)
		elif curBoard[oI][oJ] == 1:
			break
		
		oI = oI-1
	#verDown
	oI = int(crdAr[0])
	oJ = int(crdAr[1])
	oI = oI+1
	while (oI != -1 and oI != n):
		str2 = ""+str(oI)+","+str(oJ)
		if curBoard[oI][oJ] == 0:
			psArr.append(str2)
		elif curBoard[oI][oJ] == 1:
			break
		
		oI = oI+1

	#diaMoves
	oI = int(crdAr[0])
	oJ = int(crdAr[1])
	oI = oI-1
	oJ = oJ-1

	while (oI != -1 and oI != n) and (oJ != -1 and oJ != n):
		str2 = ""+str(oI)+","+str(oJ)
		if curBoard[oI][oJ] == 0:
			psArr.append(str2)
		elif curBoard[oI][oJ] == 1:
			break
		oI = oI-1
		oJ = oJ-1

	oI = int(crdAr[0])
	oJ = int(crdAr[1])
	oI = oI+1
	oJ = oJ+1

	while (oI != -1 and oI != n) and (oJ != -1 and oJ != n):
		str2 = ""+str(oI)+","+str(oJ)
		if curBoard[oI][oJ] == 0:
			psArr.append(str2)
		elif curBoard[oI][oJ] == 1:
			break
		oI = oI+1
		oJ = oJ+1

	oI = int(crdAr[0])
	oJ = int(crdAr[1])
	oI = oI+1
	oJ = oJ-1

	while (oI != -1 and oI != n) and (oJ != -1 and oJ != n):
		str2 = ""+str(oI)+","+str(oJ)
		if curBoard[oI][oJ] == 0:
			psArr.append(str2)
		elif curBoard[oI][oJ] == 1:
			break
		oI = oI+1
		oJ = oJ-1

	oI = int(crdAr[0])
	oJ = int(crdAr[1])
	oI = oI-1
	oJ = oJ+1

	while (oI != -1 and oI != n) and (oJ != -1 and oJ != n):
		str2 = ""+str(oI)+","+str(oJ)
		if curBoard[oI][oJ] == 0:
			psArr.append(str2)
		elif curBoard[oI][oJ] == 1:
			break
		oI = oI-1
		oJ = oJ+1

	return psArr

def compareBrds(b1, b2):
	status = True
	for x in range(len(b1)):
		for y in range(len(b1)):
			if b1[x][y] != b2[x][y]:
				status = False
				break;
	return status

def getNextBoard(curBoard):
	nextBoard = []
	psblBrds = []

	oneArr = findQueens(curBoard)
	#iterate through queens
	for crd in oneArr:
		crdAr = crd.split(",")
		oI = int(crdAr[0])
		oJ = int(crdAr[1])
		#get possible moves for a queen
		psblMoves = getPsblMvs(crd, len(curBoard))
		for x in psblMoves:
			crdAr1 = x.split(",")
			tI = int(crdAr1[0])
			tJ = int(crdAr1[1])
			tempBrd = copy.deepcopy(curBoard)
			tempBrd[oI][oJ] = 0
			tempBrd[tI][tJ] = 1
			#store a state in an array
			tempSet = (calConflicts(findQueens(tempBrd)), tempBrd)
			psblBrds.append(tempSet)
	
	
	tempoBoard = list(sorted(psblBrds)[0])[1]
	tempConf = list(sorted(psblBrds)[0])[0]
	currCnf = calConflicts(oneArr)

	#check if reached local maximum
	if tempConf < currCnf:
		if not compareBrds(tempoBoard, curBoard):
			nextBoard = tempoBoard

	#return empty for local max; state for normal steps
	return nextBoard

if __name__ == '__main__':
	n = int(raw_input("Enter number of queens: "))
	board_state = generateState(n)
	print "Initial State: "
	printBoard(board_state)
	print ""
	
	curBoard = board_state
	cntTot = 0
	rstrt = 0
	start = time.time()
	while True:		
		cntTot += 1
		oneArr = findQueens(curBoard)
		if calConflicts(oneArr) == 0:
			break
		
		curBoard = getNextBoard(curBoard)


		#if empty random restart
		if len(curBoard) == 0:
			#print "restart"
			curBoard = generateState(n)
			rstrt += 1
			
	#printing what's required
	print "Time taken: "+str(time.time() - start)
	print "Number of steps It took for hill climbing: "+str(cntTot)+""
	print "number of random restarts: "+str(rstrt)
	print "Final state: "
	printBoard(curBoard)