import csv
from datetime import datetime,timedelta



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

	date =datetime.strptime(d , '%Y-%m-%d')


	date= date - timedelta(days=1)
	date=date.strftime('%Y-%m-%d')



print "new_tweet selection"
	
new_tweet= {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}

with open('Elli_Eats/lda_output/output_csv/topics_words_dates.csv') as g3:
		reader = csv.reader(g3)
		line1=reader.next()
		line1 = reader.next()
                for col in range(3,(len(line1)-1)):
					if line1[col]=='':
						break;
					if col%2==1:
                                                print 'tweet1'
						print line1[col]
						print 'end'
						new_tweet[str(line1[col])]=float(row[col+1])
						col = col + 1


loi = 0 
for i in range(1, 10) :
	val =0
 	for d in days :
 		val= val + A[d][str(i)]
                print val
        print 'tweet percent:'
        print new_tweet[str(i)]
 	val=val*new_tweet[str(i)]
 	loi = loi+val
print 'level of interest:'
print loi










