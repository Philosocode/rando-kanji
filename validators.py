#!/usr/bin/python
from constants import TOTAL_KANJI

def has_valid_indices(indices):
    if _has_out_of_range_indices(indices): return False



def _has_out_of_range_indices(indices):
    """ Check if  """
    for idx in indices:
        if idx < 0 or idx > TOTAL_KANJI:
            return True
    
    return False