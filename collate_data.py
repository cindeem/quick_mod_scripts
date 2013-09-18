import os
import re
from glob import glob
import numpy as np
import pandas


################### USER INPUT ################
## User sets these parameters
## location of data
basedir = '/home/jagust/graph/data/PIB/TXTfiles/results/spectral'
## COST
cost = 0.1
#what your glob should match to grab subjects individual mod vals
filepattern = 'B*_modularity_cost%2.2f.txt'%cost
##where to put results
outfilename = 'cohort_modularity_cost%2.2f.xls'%cost
outfile = os.path.join(basedir, outfilename)

##################### END USER INPUT #############


globstr = os.path.join(basedir, filepattern)
allsub = sorted(glob(globstr))

allids = []
finaldata = np.empty((len(allsub)))
for val, sub in enumerate(allsub):
    _, fname = os.path.split(sub)
    subid = fname.split('_')[0] # first part of filename is subid
    try:
        mod = np.loadtxt(sub) 
        finaldata[val] = mod
    except:
        finaldata[val] = np.nan
    allids.append(subid)

df = pandas.DataFrame(finaldata, index = allids, 
        columns = ('modularity',))
