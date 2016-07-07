import csv
from datetime import datetime,timedelta


users =["GlennCosby","Elli_Eats"]
#list of alltopic from user
L = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
A = {}
A['GlennCosby']={}
A['Elli_Eats']={}
for user in users:

	a = []
        #modify this to get dates of corresponding user optimally
	with open('EEGC/%s.csv'%user,'r') as g:
		reader = csv.reader(g)
		for row in reader:
                        s = row[0][0:10]
			a.append(s)

	days = set(a)
	
	for d in days:
		
		A[user][d]=L
	
		with open('EEGC/output_csv/TopicsInDocsDates.csv') as g2:
			reader = csv.reader(g2)
			for row in reader:
				if d==row[0][0:10] and row[1]==user:	 
					print d
					for col in range(4,(len(row)-1)):
						if row[col]=='':
							break;
						if col%2==1:
							print row[col]
							c = str(row[col])
							A[user][d][c]=A[user][d][c]+float(row[col+1])
							print A[user][d][c]
							col = col + 1

	for d in days:	
		print d
		print user,A[user][d] 













