#!/usr/bin/env python3
"""
This module contains the Server class with methods to paginate a dataset
and handle deletion-resilient hypermedia pagination.
"""

import csv
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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cache and return the dataset of baby names."""
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding='utf-8') as f:
                reader = csv.reader(f)
                self.__dataset = list(reader)[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return pagination data that is resilient to deletion of dataset items.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        data = []
        next_index = index

        for _ in range(page_size):
            while next_index not in indexed_data and next_index < len(
                    indexed_data):
                next_index += 1
            if next_index < len(indexed_data):
                data.append(indexed_data[next_index])
                next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
