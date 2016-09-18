from pairsort import pairsort, is_sorted
import unittest

SORTED_LIST = [1, 2, 3, 4, 5, 6]

class TestSort(unittest.TestCase):


    def test_sotrable_list1(self):
        self.assertEqual(pairsort([1, 2, 5, 6, 3, 4]), SORTED_LIST)

    def test_sotrable_list2(self):
        self.assertEqual(pairsort([1, 5, 6, 4, 2, 3]), SORTED_LIST)

    def test_unsortable_list1(self):
        lst = [6, 2, 1, 4, 5, 3]
        self.assertEqual(pairsort(lst), lst)

    def test_unsortable_list2(self):
        lst = [2, 1, 3, 4, 5, 6]
        self.assertEqual(pairsort(lst), lst)

    def test_sort_sorted_list(self):
        self.assertEqual(pairsort(SORTED_LIST), SORTED_LIST)


class TestIsSorted(unittest.TestCase):

    def test_sorted_list(self):
        self.assertTrue(is_sorted(SORTED_LIST))

    def test_unsorted_list1(self):
        self.assertFalse(is_sorted([1,2,3,4,6,5]))

    def test_unsorted_list2(self):
        self.assertFalse(is_sorted([2,1,3,4,5,6]))