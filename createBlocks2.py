# this script will create 8 blocks from the master list of the experiment, with the following constraints:
# -each block will have the same number of items
#-each block will contain the same number of items from each group (e.g. 'furniture')
#-each block will contain no repetitions of the same noun within the same condition


from collections import defaultdict
import csv
import pandas

# set the number of desired blocks
blocks = 8

# read in the master list

master_list = pandas.read_csv('/Users/masha/Dropbox/Dissertation Proposal/all_items_withvalues.csv')

for row in master_list:
	print row