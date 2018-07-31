#! /bin/bash -l

# Assume that we're using Anaconda.  The reason why we're doing this is what we need a pre-2.0 NetworkX

# Edit this to load up the proper anaconda version that you're using.  Remember that WESTPA needs python2, right now.
module load python/anaconda2.7-4.2.0

# Destroy the environment, if it exists
conda env remove -n WESTPA-wipa

# Now, create it.
conda create --name WESTPA-wipa

# Now, install the packages that we need for this, including WESTPA.
conda install -c conda-forge westpa -n WESTPA-wipa
#conda install -c BjornFJohansson networkx=1.9.1 -n WESTPA-wipa
#conda install -c anaconda pandas -n WESTPA-wipa
#conda install -c anaconda cython -n WESTPA-wipa

# Create symlinks that we need to ensure everything imports/starts.
# You'll probably need to run python setup.py within this directory, as well.

source activate WESTPA-wipa
