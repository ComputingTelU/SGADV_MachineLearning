import xlrd
import numpy as np

def getData(filename,index_sheet=0):
	# ---------penjelasan parameter 
	# filename : nama file beserta ekstensi
	# index_sheet : dimulai dari 0 -> sheet index
	# ---------pemanggilan
	# data = getData("dummy.xls",0)
	# sheet_row = data.nrows
	# sheet_column = data.ncols

	data = xlrd.open_workbook(filename)
	sheet = data.sheet_by_index(index_sheet)
	return sheet

def getUnique(sheet, col):
	# for preprocessing purpose
	uL = []
	for a in sheet.col(col):
		uL.append(a.value)
	del uL[0]
	return np.unique(uL)

def getLikeliHood(sheet, column, fValue, tValue):
	# get likelihood in feature(column) with feature value(fValue) that has target value=tValue 
	sumFValue = 0.0
	sumTValue = 0.0
	uT = getUnique(sheet,column)
	for x in range(1, sheet.nrows):
		if tValue == sheet.col(sheet.ncols-1)[x].value:
			sumTValue+=1
			if fValue == sheet.col(column)[x].value:
				sumFValue+=1
	# have added the laplace technique
	return (sumFValue+1)/(sumTValue+len(uT))

def getPriorPro(sheet, tValue):
	# get prior probability
	sumTValue = 1.0
	for x in range(0, sheet.nrows):
		if tValue == sheet.col(sheet.ncols-1)[x].value:
			sumTValue+=1
	return sumTValue/(sheet.nrows+1)

def postProb(tValue, iValue, tiValue, weValue, wiValue):
	# get the posterior probability
	sheet = getData("dummy.xls",0)
	
	lHI = getLikeliHood(sheet,0,iValue,tValue)
	lHTi = getLikeliHood(sheet,1,tiValue,tValue)
	lHWe = getLikeliHood(sheet,2,weValue,tValue)
	lHWi = getLikeliHood(sheet,3,wiValue,tValue)
	pr = getPriorPro(sheet, tValue)

	return lHI*lHTi*lHWe*lHWi*pr

def testing(iValue, tiValue, weValue, wiValue):
	yes = postProb("Yes", iValue, tiValue, weValue, wiValue)
	no = postProb("No", iValue, tiValue, weValue, wiValue)

	if yes>no:
		return "Yes"
	else:
		return "No"
# ===========================================================================================
# =================================Testing===================================================
print "Delayed pada testing 1 adalah ", testing("Yes", "Dawn", "Cloudy", "Strong")
print "Delayed pada testing 2 adalah ", testing("No", "Evening", "Clear", "Weak")