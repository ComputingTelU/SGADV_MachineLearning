import xlrd
xls = xlrd.open_workbook("name.xlsx")
s = xls.sheet_by_index(0)

def getData(datake):
	list1 = []
	for rows in range(s.nrows):
		list1.append(s.cell(rows, datake).value)
	return list1

#print getData(0)
#print getData(1)
#print getData(2)
#print getData(3)
#print getData(4)

YesxYes = 1
YesxNo = 1
NoxYes = 1
NoxNo = 1
MorningxYes = 1
MorningxNo = 1
EveningxYes = 1
EveningxNo = 1
AfternoonxYes = 1
AfternoonxNo = 1
DawnxYes = 1
DawnxNo = 1
ClearxYes = 1
ClearxNo = 1
RainyxYes = 1
RainyxNo = 1
CloudyxYes = 1
CloudyxNo = 1
WeakxYes = 1
WeakxNo = 1
StrongxYes = 1
StrongxNo = 1
ModeratexYes = 1
ModeratexNo = 1
i = 1


for i in range(len(getData(0))):
	if(getData(0)[i] == 'Yes' and getData(4)[i] == 'Yes'):
		YesxYes = YesxYes + 1
	elif(getData(0)[i] == 'Yes' and getData(4)[i] == 'No'):
		YesxNo = YesxNo + 1
	if(getData(0)[i] == 'No' and getData(4)[i] == 'Yes'):
		NoxYes = NoxYes + 1
	elif(getData(0)[i] == 'No' and getData(4)[i] == 'No'):
		NoxNo = NoxNo + 1

for i in range(len(getData(1))):
	if(getData(1)[i] == 'Morning' and getData(4)[i] == 'Yes'):
		MorningxYes = MorningxYes + 1
	elif(getData(1)[i] == 'Morning' and getData(4)[i] == 'No'):
		MorningxNo = MorningxNo + 1
	if(getData(1)[i] == 'Evening' and getData(4)[i] == 'Yes'):
		EveningxYes = EveningxYes + 1
	elif(getData(1)[i] == 'Evening' and getData(4)[i] == 'No'):
		EveningxNo = EveningxNo + 1
	if(getData(1)[i] == 'Afternoon' and getData(4)[i] == 'Yes'):
		AfternoonxYes = AfternoonxYes + 1
	elif(getData(1)[i] == 'Afternoon' and getData(4)[i] == 'No'):
		AfternoonxNo = AfternoonxNo + 1
	if(getData(1)[i] == 'Dawn' and getData(4)[i] == 'Yes'):
		DawnxYes = DawnxYes + 1
	elif(getData(1)[i] == 'Dawn' and getData(4)[i] == 'No'):
		DawnxNo = DawnxNo + 1

for i in range(len(getData(2))):
	if(getData(2)[i] == 'Clear' and getData(4)[i] == 'Yes'):
		ClearxYes = ClearxYes + 1
	elif(getData(2)[i] == 'Clear' and getData(4)[i] == 'No'):
		ClearxNo = ClearxNo + 1
	if(getData(2)[i] == 'Rainy' and getData(4)[i] == 'Yes'):
		RainyxYes = RainyxYes + 1
	elif(getData(2)[i] == 'Rainy' and getData(4)[i] == 'No'):
		RainyxNo = RainyxNo + 1
	if(getData(2)[i] == 'Cloudy' and getData(4)[i] == 'Yes'):
		CloudyxYes = CloudyxYes + 1
	elif(getData(2)[i] == 'Cloudy' and getData(4)[i] == 'No'):
		CloudyxNo = CloudyxNo + 1

for i in range(len(getData(3))):
	if(getData(3)[i] == 'Weak' and getData(4)[i] == 'Yes'):
		WeakxYes = WeakxYes + 1
	elif(getData(3)[i] == 'Weak' and getData(4)[i] == 'Yes'):
		WeakxNo = WeakxNo + 1
	if(getData(3)[i] == 'Strong' and getData(4)[i] == 'Yes'):
		StrongxYes = StrongxYes + 1
	elif(getData(3)[i] == 'Strong' and getData(4)[i] == 'No'):
		StrongxNo = StrongxNo + 1
	if(getData(3)[i] == 'Moderate' and getData(4)[i] == 'Yes'):
		ModeratexYes = ModeratexYes + 1
	elif(getData(3)[i] == 'Moderate' and getData(4)[i] == 'No'):
		ModeratexNo = ModeratexNo + 1

#print StrongxNo

def likelihood (x):
	if (x == 'YesxYes'):
		return float(YesxYes) / float(YesxYes + NoxYes)
	elif (x == 'YesxNo'):
		return float(YesxNo) / float(YesxNo + NoxNo)
	elif (x == 'NoxYes'):
		return float(NoxYes) / float(YesxYes + NoxYes)
	elif (x == 'NoxNo'):
		return float(NoxNo) / float(YesxNo + NoxNo)
	elif (x == 'MorningxYes'):
		return float(MorningxYes) / float(MorningxYes + EveningxYes + AfternoonxYes + DawnxYes)
	elif (x == 'EveningxYes'):
		return float(EveningxYes) / float(MorningxYes + EveningxYes + AfternoonxYes + DawnxYes)
	elif (x == 'AfternoonxYes'):
		return float(AfternoonxYes) / float(MorningxYes + EveningxYes + AfternoonxYes + DawnxYes)
	elif (x == 'DawnxYes'):
		return float(DawnxYes) / float(MorningxYes + EveningxYes + AfternoonxYes + DawnxYes)
	elif (x == 'MorningxNo'):
		return float(MorningxNo) / float(MorningxNo + EveningxNo + AfternoonxNo + DawnxNo)
	elif (x == 'EveningxNo'):
		return float(EveningxNo) / float(MorningxNo + EveningxNo + AfternoonxNo + DawnxNo)
	elif (x == 'AfternoonxNo'):
		return float(AfternoonxNo) / float(MorningxNo + EveningxNo + AfternoonxNo + DawnxNo)
	elif (x == 'DawnxNo'):
		return float(DawnxNo) / float(MorningxNo + EveningxNo + AfternoonxNo + DawnxNo)
	elif (x == 'ClearxYes'):
		return float(ClearxYes) / float(ClearxYes + RainyxYes + CloudyxYes)
	elif (x == 'RainyxYes'):
		return float(RainyxYes) / float(ClearxYes + RainyxYes + CloudyxYes)
	elif (x == 'CloudyxYes'):
		return float(CloudyxYes) / float(ClearxYes + RainyxYes + CloudyxYes)
	elif (x == 'ClearxNo'):
		return float(ClearxNo) / float(ClearxNo + RainyxNo + CloudyxNo)
	elif (x == 'RainyxNo'):
		return float(RainyxNo) / float(ClearxNo + RainyxNo + CloudyxNo)
	elif (x == 'CloudyxNo'):
		return float(CloudyxNo) / float(ClearxNo + RainyxNo + CloudyxNo)
	elif (x == 'WeakxYes'):
		return float(WeakxYes) / float(WeakxYes + StrongxYes + ModeratexYes)
	elif (x == 'StrongxYes'):
		return float(StrongxYes) / float(WeakxYes + StrongxYes + ModeratexYes)
	elif (x == 'ModeratexYes'):
		return float(ModeratexYes) / float(WeakxYes + StrongxYes + ModeratexYes)
	elif (x == 'WeakxNo'):
		return float(WeakxNo) / float(WeakxNo + StrongxNo + ModeratexNo)
	elif (x == 'StrongxNo'):
		return float(StrongxNo) / float(WeakxNo + StrongxNo + ModeratexNo)
	elif (x == 'ModeratexNo'):
		return float(ModeratexNo) / float(WeakxNo + StrongxNo + ModeratexNo)
	
def prior (pilihan):
	if (pilihan == 'Yes'):
		return float(1 +getData(4).count('Yes')) / float(1 +len(getData(4)))
	elif (pilihan == 'No'):
		return float(1+getData(4).count('No')) / float(1+len(getData(4)))

#print prior ('Yes')
#print prior ('No')

def posterior (l1,l2,l3,l4,p):
	return float(likelihood(l1)*likelihood(l2)*likelihood(l3)*likelihood(l4)*prior(p))


print posterior ('YesxYes', 'DawnxYes', 'CloudyxYes', 'WeakxYes', 'Yes')
print posterior ('YesxNo', 'DawnxNo', 'CloudyxNo', 'WeakxNo', 'No')

print posterior ('NoxYes', 'EveningxYes', 'ClearxYes', 'WeakxYes', 'Yes')
print posterior ('NoxNo', 'EveningxNo', 'ClearxNo', 'WeakxNo', 'No')