from __future__ import division, print_function; __metaclass__ = type
import os, sys, math, itertools
import numpy
import west
from west import WESTSystem
from westpa.binning import RectilinearBinMapper
import westpa

import logging
log = logging.getLogger(__name__)
log.debug('loading module %r' % __name__)

class System(WESTSystem):
    def initialize(self):
        self.pcoord_ndim = 1
        self.pcoord_len = 11
        self.pcoord_dtype = numpy.float32
        self.dist_binbounds = [0.0,0.2,0.7,1.5,2.2,3.8,5.0,6.0,7.0,8.0,9.0,10.0,11.6,12.0,13,14,15,16,17,18,19,20,21,22,23,24,float('inf')]
        #self.dist_binbounds = [0.0,2.2,2.5,3.8,5.0,6.0,7.0,8.0,9.0,10.0,11.6,12.0,13,14,15,16,17,18,19,20,21,22,23,24,float('inf')]
        #self.dist_binbounds = [0.0,float('inf')]

        self.bin_mapper = RectilinearBinMapper([self.dist_binbounds])
        #self.bin_mapper = RectilinearBinMapper([self.dist_binbounds])
        self.bin_target_counts = numpy.empty((self.bin_mapper.nbins,), numpy.int)
        self.bin_target_counts[...] = 8
    

def coord_loader(fieldname, coord_file, segment, single_point=False):
    coord_raw = numpy.loadtxt(coord_file, dtype=numpy.float32) 
    color_bins = [(0.0,2.2),(24.00,float('inf'))]
    unknown_state = 2
    new_walker = 0
    system = westpa.rc.get_system_driver()
    #print(system.pcoord_ndim)

    try:
        npts = len(coord_raw)
    except(TypeError):
        npts = 1
        new_walker = 1

    coords = numpy.empty((npts), numpy.float32)
    colors = numpy.empty((npts), numpy.float32)
    if new_walker == 1:
        colors[:] = unknown_state
        for istate,state_tuple in enumerate(color_bins):
            if coord_raw >= state_tuple[0] and coord_raw < state_tuple[1]:
                colors[:] = istate
    else:
        colors[:] = segment.pcoord[0][1]
    if new_walker == 1:
        coords[0] = coord_raw
    else:
        coords[:] = coord_raw
    for istate,state_tuple in enumerate(color_bins):
        if coords[-1] >= state_tuple[0] and coords[-1] < state_tuple[1]:
            colors[-1] = istate
    
    if new_walker == 1:
        segment.pcoord = numpy.hstack((coords[:],colors[:]))
    else:
        segment.pcoord = numpy.swapaxes(numpy.vstack((coords[:],colors[:])), 0, 1)



def _2D_coord_loader(fieldname, coord_file, segment, single_point=False):
    coord_raw = numpy.loadtxt(coord_file, dtype=numpy.float32) 
    color_bins = [(0.0,3.00),(11.60,float('inf'))]
    unknown_state = 2
    new_walker = 0
    system = westpa.rc.get_system_driver()
    #print(system.pcoord_ndim)

    if single_point == True:
        npts = 1
        new_walker = 1
    else:
        npts = 11

    coords = numpy.empty((npts,2), numpy.float32)
    colors = numpy.empty((npts), numpy.float32)
    if new_walker == 1:
        colors[:] = unknown_state
        for istate,state_tuple in enumerate(color_bins):
            if coord_raw[0] >= state_tuple[0] and coord_raw[0] < state_tuple[1]:
                colors[:] = istate
    else:
        colors[:] = segment.pcoord[0][2]
    if new_walker == 1:
        coords[:] = coord_raw[...]
    else:
        coords[:] = coord_raw[...]
    for istate,state_tuple in enumerate(color_bins):
        if coords[-1,0] >= state_tuple[0] and coords[-1,0] < state_tuple[1]:
            colors[-1] = istate
    
    if new_walker == 1:
        #print(coords[0,1], coords[0,0])
        #print(coords[0])
        segment.pcoord = numpy.hstack((coords[0,0],coords[0,1],colors[:]))
        #segment.pcoord = numpy.swapaxes(numpy.vstack((coords[0],coords[1],colors[:])), 0, 1)
        #print(segment.pcoord)
    else:
        segment.pcoord = numpy.swapaxes(numpy.vstack((coords[:,0],coords[:,1],colors[:])), 0, 1)
        #print(segment.pcoord)

    
    
    
    
    
