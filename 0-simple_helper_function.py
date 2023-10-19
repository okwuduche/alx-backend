#!/usr/bin/env python3
''' Simple helper function '''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
        function should return a tuple of size two
        containing a start index and an end index
        corresponding to the range of indexes to return in a
        list for those particular pagination parameters
    '''
    start_index = page * page_size - page_size
    stop_index = page * page_size
    return (start_index, stop_index)
