import csv


a = []
with open('Elli_Eats/tweets_dates_seven.csv') as g:
	reader = csv.reader(g)
	for row in reader:
		a.append(row[0][0:10])

days = set(a)
A = {}
for d in days:
	L = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
	A[d]=L
	
	with open('Elli_Eats/lda_output/output_csv/topics_words_dates.csv') as g2:
		reader = csv.reader(g2)
		for row in reader:
			if d==row[0][0:10]:	 
				print d
				for col in range(3,(len(row)-1)):
					if row[col]=='':
						break;
					if col%2==1:
						print row[col]
						c = str(row[col])
						A[d][c]=A[d][c]+float(row[col+1])
						print A[d][c]
						col = col + 1

for d in days:	
	print A[d]
