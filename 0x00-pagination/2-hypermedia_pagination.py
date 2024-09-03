#!/usr/bin/env python3
""" Hypermedia pagination """


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ a function that takes two integer arguments and returns a tuple
            of size two containing a start index and an end index corresponding
            to the range of indexes to return in a list for those particular
            pagination parameters.
            Args:
                page (int)
                page_size (int)
            Returns:
                page
            Note:
                Page numbers are 1-indexed, i.e. the first page is page 1.
        """
        self.dataset()
        # assertion to check type of args
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start_index = (page - 1) * page_size
        end_index = (start_index + page_size)

        # return the page specified by start and end index
        if self.__dataset is None or start_index > len(self.__dataset):
            return []
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ returns a dict containing info on the dataset
            Args:
                page (int)
                page_size (int)
            Returns:
                dict
        """
        data = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page > total_pages:
            data_dict = {"page_size": 0, "page": page, "data": []}
        else:
            data_dict = {"page_size": page_size, "page": page, "data": data}
        # next and previous pages
        nextp = None if self.get_page(page + 1, page_size) == [] else page + 1
        data_dict["next_page"] = nextp
        # if page == 1 or self.get_page(page - 1, page_size) == []:
        #     data_dict["prev_page"] = None
        # else:
        #     data_dict["prev_page"] = page - 1
        data_dict["prev_page"] = page - 1
        data_dict["total_pages"] = total_pages

        return data_dict
