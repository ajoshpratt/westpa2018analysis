#! /bin/bash -l

# Edit this to load up the proper anaconda version that you're using.  Remember that WESTPA needs python2, right now.
module load python/anaconda2.7-4.2.0

# So, we needed to push some last minute fixes, which aren't in the conda install...
cd ~/
git clone https://github.com/westpa/westpa.git
cd westpa
./setup.sh
chmod +x westpa.sh
