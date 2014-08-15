# goal of this script is to use the items in my experiment and see whether certain items 
# are more often modified than others. I'll be using my bigrams.csv file that contains all the bigrams for 
# each noun 


import pandas as pd 
import numpy as np 
import sys
from collections import defaultdict

# set the file path
if sys.platform.startswith('win32'): # for cross-computer compatibility
    filepath = 'C:\Users\dailyuser\Dropbox\Dissertation Proposal\\'
else:
    filepath = '/Users/masha/Dropbox/Dissertation Proposal/'

all_bigrams = pd.read_csv(filepath + 'bigrams_finalnouns.csv')


# gonna use pandas groupby and multiindexing to figure out how they work, yay! 

#first let's group by word and condition (across two levels)

grouped = all_bigrams.groupby(['Level', 'Words', 'Noun'])
# grouped['count'] = grouped['Occ'].count()
new_df =  grouped.aggregate({'Occ': np.sum, 'LogFreq': np.mean} )
new_df['count'] = grouped['Occ'].count()

# new_df['MP'] = grouped.apply(lambda x: new_df['Occ'] / new_df['LogFreq'])
new_df['MP'] = new_df['Occ'] / new_df['LogFreq'].apply(lambda x: np.power(10,x))
print new_df[['Occ', 'MP','count']]
# print grouped['Occ'].count()





