"""
Description: Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it can trap after
raining.
https://leetcode.com/problems/trapping-rain-water/

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105

"""

import typing as t
import logging

""" ! → → → The solution was obtained with outside help ← ← ← ! """

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def trap(height: t.List[int]) -> int:
    logger.debug('trapping is started')
    if not height:
        return 0

    peak_pos = height.index(max(height))
    volume = (half_trap(height[:peak_pos])
              + half_trap(reversed(height[peak_pos + 1:])))

    return volume


def half_trap(height: t.List[int]) -> int:
    small_peak = 0
    volume = 0
    for h in height:
        if h < small_peak:
            volume += small_peak - h
        else:
            small_peak = h
    return volume


def test():
    examples = [
        # [2, 1, 2],
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [1, 3, 1, 2, 1, 4, 3, 2],
        [3, 2, 1, 1, 1, 2, 1],
        [2, 1, 1, 4, 5],
        [3, 2, 1, 2, 1],
        [5, 2, 3, 4, 3, 2, 1],
        [5, 4, 1, 2]
    ]
    answers = [  # 1,
        6, 9, 5, 3, 2, 1, 3, 1]

    for i, example in enumerate(examples):
        assert trap(example) == answers[i], (
            f'expected: {answers[i]}, '
            f'input: {example}, output: {trap(example)}'
        )


if __name__ == '__main__':
    test()
