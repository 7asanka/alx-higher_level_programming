#!/usr/bin/python3
"""
finds a peak in a list of unordered integers
"""


def find_peak(list_of_integers):
    """Finds a peak element in a list of unsorted integers."""
    if not list_of_integers:
        return None

    def find_peak_recursive(nums, left, right):
        """Helper function to find a peak using divide-and-conquer."""
        mid = (left + right) // 2

        if (mid == 0 or nums[mid] >= nums[mid - 1]) and \
           (mid == len(nums) - 1 or nums[mid] >= nums[mid + 1]):
            return nums[mid]

        if mid > 0 and nums[mid - 1] > nums[mid]:
            return find_peak_recursive(nums, left, mid - 1)

        return find_peak_recursive(nums, mid + 1, right)

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)
