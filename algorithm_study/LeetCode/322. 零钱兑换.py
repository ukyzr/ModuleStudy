# -*- coding: utf-8 -*-
# __file__  : 322. 零钱兑换.py
# __time__  : 2020/6/27 10:43 下午

import typing

from kombu.utils.eventio import epoll

"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

 

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
 

说明:
你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def coinChange(self, coins: typing.List[int], amount: int) -> int:
        memo = dict()

        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 1:
                return -1
            res = float("INF")
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)
            memo[n] = res if res != float("INF") else -1

            return memo[n]

        return dp(amount)


if __name__ == "__main__":
    print(Solution().coinChange([1, 2, 5], 700))
    epoll
