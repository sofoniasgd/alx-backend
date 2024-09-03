#!/usr/bin/env python3
""" 0. Simple helper function """


def index_range(page, page_size):
    """ a function named index_range that takes two integer arguments
        and returns a tuple of size two containing a start index and
        an end index corresponding to the range of indexes to return
        in a list for those particular pagination parameters.
        Args:
            page (int)
            page_size (int)
        Returns:
            tuple
        Note:
            Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start_index = (page - 1) * page_size
    end_index = (start_index + page_size)
    return (start_index, end_index)
