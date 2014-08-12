# this script will create 8 blocks from the master list of the experiment, with the following constraints:
# -each block will have the same number of items
#-each block will contain the same number of items from each group (e.g. 'furniture')
#-each block will contain no repetitions of the same noun within the same condition


from collections import defaultdict
import pandas
import numpy as np
import sys

# set the number of desired blocks
blocks = 8
# initialize a default dict that will contain 8 nested dictionaries (that contain lists)

block_dict = defaultdict(lambda : defaultdict(list))

# initialize list dictionaries for each block, just so everything is clear right away

for x in xrange(blocks):
	block_dict["block{0}".format(x)]

# read in the master list
if sys.platform.startswith('win32'): # for cross-computer compatibility
    filepath = 'C:\Users\dailyuser\Dropbox\Dissertation Proposal\Experiment Script\\'
else:
    filepath = '/Users/masha/Dropbox/Dissertation Proposal/Experiment Script/'
    

master_list = pandas.read_csv(filepath + 'all_items_withvalues.csv')
rows = len(master_list.index)
#first subset the master list for only the columns I want
sub_list = master_list[['Adj', 'Noun', 'Words', 'Group', 'Item', 'Level', 'Task1', 'Task2', 'Correct_Task', 'Correct_Task_Num', 'Adj_Trigger', 'Target_Trigger', 'Task_Trigger']]

#randomly shuffle the sub_list so that you're randomly selecting an item to fit in the block

shuffled_rows = np.random.permutation(range(0,rows))

shuffled_sub = sub_list.iloc[shuffled_rows,:]

#then go through the list item by item and fit it into a block, based on constraints

for i in xrange(rows):
	single_row = shuffled_sub.iloc[i,:] # now we have a single item from the list
	#if i <= 1: print single_row
	#go through each block and check the constraints

	for j in xrange(blocks): #go through all the blocks
		#check each block for conditions 
		if len(block_dict["block{0}".format(j)]['item_list']) <= (rows/8): #don't want any of the blocks to be bigger than any other
		    group_indices = [k for k, x in enumerate(block_dict["block{0}".format(j)]['group']) if x == int(single_row.loc['Group'])] # find whether the block already contains items from that group
		    if len(group_indices) < 2 and \
		    not( block_dict["block{0}".format(j)]['noun'] == single_row.loc['Noun'] and block_dict["block{0}".format(j)]['adj'] == single_row.loc['Adj']): #don't want to repeat the same adj/noun pair

			

			block_dict["block{0}".format(j)]['item_list'].append(int(single_row.loc['Item'])) #append the item to the item list
			block_dict["block{0}".format(j)]['group'].append(int(single_row.loc['Group']))   #append the group to the group list
			block_dict["block{0}".format(j)]['noun'].append(single_row.loc['Noun'])# append the noun
			block_dict["block{0}".format(j)]['adj'].append(single_row.loc['Adj']) # append the adj
			break
		
                    else: continue
		else: continue



# now that the blocks are created, need to subset the original data frame according to the block indices (in 'item') and write out
#
for j in xrange(blocks):
#    

#
    index = [x-1 for x in block_dict["block{0}".format(j)]['item_list']]

    
    block = sub_list.iloc[index]
    block.to_csv(filepath + "block_{0}.csv".format(j+1), sep = ";", header = False, index = False)








