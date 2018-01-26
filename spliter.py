#!/usr/bin/python

import os
import sys
import csv

# encoding
reload(sys)
sys.setdefaultencoding('utf-8')

source_path = 'mdata'
source_file = 'datam.csv'
target_path = 'mdata'
target_prefix = 'datam'
 
# read local csv file
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),source_path,source_file)
csv_reader = csv.reader(open(csv_path,'rb'))
csv_reader.next()
i=j=1
for row in csv_reader:
	if i%160000==0:
		print u"datam-%s success" % j
		j+=1
	# write csv
	csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),target_path,target_prefix+'-'+str(j)+'.csv')
	csv_file = file(csv_path, 'ab+')
	csv_write = csv.writer(csv_file)
	# header	
	#if os.path.getsize(csv_path)==0:
		#csv_write.writerow(['mobile'])
	# write
	csv_write.writerow([row[0]])
	csv_file.close()
	i+=1
# close