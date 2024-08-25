# pylint: disable=C0103
"""
This module contains the Server class with methods to paginate a dataset
and return hypermedia pagination information.
"""

import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server with an empty dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache and return the dataset of baby names."""
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding='utf-8') as f:
                reader = csv.reader(f)
                self.__dataset = list(reader)[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset based on the
        specified page number and page size.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return pagination information with metadata, including page size,
        current page, dataset page, and total pages.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
