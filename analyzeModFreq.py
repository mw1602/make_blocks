# goal of this script is to use the items in my experiment and see whether certain items 
# are more often modified than others. I'll be using my bigrams.csv file that contains all the bigrams for 
# each noun 


import pandas as pd 
import numpy as np 
import sys
from collections import defaultdict

# read in the master list
if sys.platform.startswith('win32'): # for cross-computer compatibility
    filepath = 'C:\Users\dailyuser\Dropbox\Dissertation Proposal\\'
else:
    filepath = '/Users/masha/Dropbox/Dissertation Proposal/'

all_bigrams = pandas.read_csv(filepath + 'bigrams_finalnouns.csv')