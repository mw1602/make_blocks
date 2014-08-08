# this script will create 8 blocks from the master list of the experiment, with the following constraints:
# -each block will have the same number of items
#-each block will contain the same number of items from each group (e.g. 'furniture')
#-each block will contain no repetitions of the same noun within the same condition


from collections import defaultdict
import csv
import pandas
import numpy as np

# set the number of desired blocks
blocks = 8
# intiialize a default dict that will contain 8 nested dictionaries (that contain lists)

block_dict = defaultdict(lambda : defaultdict(list))

# initialize list dictionaries for each block, just so everything is clear right away

for x in range(1,9):
	block_dict["block{0}".format(x)]



# block_dict['block1']['item_list'].append('testing')
# block_dict['block1']['item_list'].append('one...two...three')

# print block_dict['block1']['item_list']
# read in the master list

master_list = pandas.read_csv('/Users/masha/Dropbox/Dissertation Proposal/Experiment Script/all_items_withvalues.csv')
rows = len(master_list.index)

#first subset the master list for only the columns I want
sub_list = master_list[['Adj', 'Noun', 'Words', 'Group', 'Item', 'Level', 'Task1', 'Task2', 'Correct_Task', 'Adj_Trigger', 'Target_Trigger', 'Task_Trigger']]

#randomly shuffle the sub_list so that you're randomly selecting an item to fit in the block

shuffled_rows = np.random.permutation(range(1,rows))

shuffled_sub = sub_list.iloc[shuffled_rows,:]

#then go through the list item by item and fit it into a block, based on constraints

