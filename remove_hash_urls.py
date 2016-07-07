import re
import csv
import string
with open('EEGC/sevendaystweet.csv','rb') as f:
	reader = csv.reader(f,delimiter=',')
	for row in reader:
		e = str(row)
	
		d = filter(lambda x: x in string.printable, e)	
		print d
		a = ' '.join(re.sub("(RT)|([@|#][A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",d).split())
		b = []
		b.append(a)
		with open('EEGC/tweets_without_urlstags.csv', 'a+') as s:
					writer = csv.writer(s)
					writer.writerow(b)
