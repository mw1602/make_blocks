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

# let's create a multindex to reflect our hierarchically organized data, using the relevant columns

all_bigrams.set_index(['Level', 'Words'], inplace = True)

print all_bigrams.head() # woo so cool it works!
