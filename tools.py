import os, sys
import numpy as np
## Which version are you running??
sys.path.insert(0, '/home/jagust/graph/scripts/brainx')
from brainx import modularity
from brainx import util
from glob import glob
import networkx as nx
import nibabel

def calc_spectral_modularity(mat, cost):
    """ Use brainx to 
    generate binary matrix theshold based on cost
    run newman spectral modularity
    
    Parameters
    ----------
    mat : numpy matrix
        symmetric adjacency matrix, should not contain nan
    cost: float
        cost used to binarize adjacency matrix
        
    Returns
    -------
    part : GraphPartition
        part.index provides access to found communities
    true_cost : float
        the actual cost associated with thresholded adj matrix
    """
    mask, real_cost = util.threshold_adjacency_matrix(mat, cost)
    true_cost = util.find_true_cost(mask)
    graph = nx.from_numpy_matrix(mask)
    part = modularity.newman_partition(graph)
    return part, true_cost 

def calc_sa_modularity(mat, cost):
    """ Use brainx to 
    generate binary matrix theshold based on cost
    use simulated annealing to find communities
    
    Parameters
    ----------
    mat : numpy matrix
        symmetric adjacency matrix, should not contain nan
    cost: float
        cost used to binarize adjacency matrix
        
    Returns
    -------
    part : GraphPartition
        part.index provides access to found communities
    true_cost : float
        the actual cost associated with thresholded adj matrix
    """

    mask, real_cost = util.threshold_adjacency_matrix(mat, cost)
    true_cost = util.find_true_cost(mask)
    graph = nx.from_numpy_matrix(mask)
    part, mod = modularity.simulated_annealing(graph)
    return part, true_cost
