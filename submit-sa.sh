#!/bin/csh
#
# This simple SGE batch script shows how to run a python script
# Below are SGE options embedded in comments
# 

# specify number of jobs to run (1-N)
# eg run 4 subjects  -t 1-4

#$ -t 1-165

# join stdout and stderr
# this may make debugging easier, but output may become less 
# readable. 

#$ -j y

# redefine output file
# this saves the output from your cluster jobs to your home directory
# and names the files <scriptname>_<node=cn1-cn15>_<jobnumber>
#    eg. python_wrapper.sh_cn12.7535

#$ -o $HOME/logs/$JOB_NAME_$HOSTNAME.$JOB_ID

# Shell to use: Specifies the interpreting shell for the job 

#$ -S /bin/bash

# Specifies that all environment variables active within the  qsub
#     utility be exported to the context of the job.
#$ -V

# Tells SGE to send a mail to the job owner when 
#   the job begins (b), ends (e), aborted (a), and suspended(s).
# -m eas (NOTE THIS IS COMMENTED OUT)

# Tells SGE to send mail about this job to the given email address
# -M youremailaddress@berkeley.edu (ALSO COMMENTED OUT)

# Specifies the home for your scripts
# you need to make a scripts directory in your home directory 
#  and save scripts there
#SCRIPT_DIR=$HOME/

# Run python program (include path to script)
python calc_sa.py
