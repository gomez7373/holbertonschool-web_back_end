#!/usr/bin/env python3
"""
This module contains the Server class for paginating
a dataset of popular baby names.
"""

import csv
from typing import List


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
        Get a page of the dataset based
        on the specified page number and page size.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
