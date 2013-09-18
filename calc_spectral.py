import os, re
import numpy as np
from glob import glob
import tools
import json
import pickle

################### USER INPUT ################
## User sets these parameters
## location of data
basedir = '/home/jagust/graph/data/PIB/TXTfiles'
filepattern = 'B*.txt' #what your glob should match
subid_pattern = 'B[0-9]{2}-[0-9]{3}' # eg B00-000 
## COST
cost = 0.1

##where to put results
outdir = os.path.join(basedir, 'results', 'spectral')
##################### END USER INPUT #############

# make output directory if it doesnt exist
if not os.path.isdir(outdir):
    os.makedirs(outdir) # will make outdir and necessary leaf dirs

## grab sorted adj matrix files
globstr = os.path.join(basedir, filepattern)
mat_files = sorted(glob(globstr))

try:
    task_id = os.environ.get('SGE_TASK_ID')
    task_id = int(task_id) - 1
except:
    # if not SGE job, just run first
    task_id = 0
# choose subject file to run based on task_id
sub = mat_files[task_id]

## Use regular expression to grab subject id
m = re.search(subid_pattern, sub)
try:
    subid = m.group()
except:
    raise ValueError('Could not find subid in %s'%sub)

# load matrix
subf = mat_files[task_id]
submat = np.loadtxt(subf)

# find  partitions at given cost, get true_cost
part, true_cost = tools.calc_spectral_modularity(submat, cost)

mod = part.modularity()
newfile = os.path.join(outdir, 
                       '%s_modularity_cost%2.2f.txt'%(subid,cost))
with open(newfile, 'w+') as fid:
    fid.write('%2.4f'%mod)

true_cost_file = newfile.replace('.txt', '.cost')
with open(true_cost_file, 'w+') as fid:
    fid.write('%2.4f'%true_cost)

index = [list(x) for k, x in part.index.items()]
partfile = newfile.replace('.txt', '.json')
json.dump(index, open(partfile, 'w+'))

pickle_file = partfile.replace('.json', '.pkl')
with open(pickle_file, 'w') as pid:
    pickle.dump(part.index, open(pickle_file, 'w'))
print 'wrote %s, %s, %s'%(newfile, partfile, pickle_file)
