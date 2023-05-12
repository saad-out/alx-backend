#!/usr/bin/env python3
"""
This module contains the class Server that manages API calls to a database
of popular baby names using pagination.
"""
import csv
import math
from typing import List, Tuple, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start index and an end index for a particular
    pagination page.

    Args:
        page (int): page number
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: tuple containing a start index and an end index
    """
    if page <= 0 or page_size < 0:
        return (-1, -1)

    return (page_size * (page - 1), page_size * page)


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
        """
        Gets the correct page from the dataset

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): number of items per page.
                                        Defaults to 10.

        Returns:
            List[List]: list of rows of the dataset
        """
        assert type(page) == type(page_size) == int
        assert page > 0 and page_size > 0

        start: int
        end: int
        start, end = index_range(page, page_size)
        dataset: List[List] = self.dataset()
        if start < 0 or start >= len(dataset) or end >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Gets the correct page from the dataset and returns a dictionary

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): number of items per page.

        Returns:
            Dict: dictionary of the following format:
            {
                "page_size": <page_size>,
                "page": <page>,
                "data": <page of the dataset>,
                "next_page": <page of the next page>,
                "prev_page": <page of the previous page>,
                "total_pages": <total pages in the dataset>
            }
        """
        data: List[List] = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.dataset()) / page_size)
        prev_page: Optional[int] = (page - 1) if page > 1 else None
        next_page: Optional[int] = (page + 1) if page < total_pages else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
