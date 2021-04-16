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

import logging
import typing as t

""" ! → → → timing failure on test 319/320 (LeetCode) ← ← ← ! """

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def trap(height: t.List[int]) -> int:
    logger.debug('trapping is started')
    volume = 0
    puddle = []
    for h in height:
        vol = 0
        if len(puddle) == 0:
            puddle.append(h)
        elif h <= puddle[-1]:
            puddle.append(h)
        elif puddle[-1] < h < max(puddle):
            puddle.append(h)
            puddle.reverse()
            for i, n in enumerate(puddle):
                while n < max(puddle):
                    if (h - n) > 0:
                        vol += h - n
                    else:
                        vol = 0
                    puddle[i] += vol
                    volume += vol
                    vol = 0
                    break
            puddle.reverse()
        elif h >= max(puddle):
            if len(puddle) < 2:
                puddle = [h]
            else:
                puddle.append(h)
                last = []
                for i, n in enumerate(puddle):
                    h = puddle[0]
                    if (h - n) > 0:
                        vol += h - n
                    else:
                        vol = 0
                    puddle[i] += vol
                    volume += vol
                    vol = 0
                    last = n
                puddle = [last]
    return volume


def test():
    examples = [
        [2, 1, 2],
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [1, 3, 1, 2, 1, 4, 3, 2],
        [3, 2, 1, 1, 1, 2, 1],
        [2, 1, 1, 4, 5],
        [3, 2, 1, 2, 1],
        [5, 2, 3, 4, 3, 2, 1],
        [5, 4, 1, 2]
    ]
    answers = [1, 6, 9, 5, 3, 2, 1, 3, 1]

    for i, example in enumerate(examples):
        assert trap(example) == answers[i], (
            f'expected: {answers[i]}, '
            f'input: {example}, output: {trap(example)}'
        )

    logger.error(
        f'timing failure on test 319/320 (LeetCode)\n'
        f'    (huge example)'
    )


if __name__ == '__main__':
    test()
