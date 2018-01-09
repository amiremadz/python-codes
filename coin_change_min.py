#!/usr/bin/python3

#from nose.tools import assert_equal

class TestCoins(object):
    
    def check(self, solution):
        coins = [1,5,10,25]
        assert_equal(solution(coins, 45), 3)
        assert_equal(solution(coins, 23), 5)
        assert_equal(solution(coins, 74), 8)
        print('Passed all tests.')

class Solution_rc(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = [0] * (amount + 1)
        res = self.helper(coins, amount, cache)
        #print(cache)
        return res
    
    def helper(self, coins, amount, cache):
        res = amount

        if amount in coins:
            cache[amount] = 1
            return 1
        
        if cache[amount] > 0:
            return cache[amount]

        for item in [c for c in coins if c <= amount]:
            count = 1 + self.helper(coins, amount - item, cache)
            if(count < res):
                res = count
                cache[amount] = res
                
        return res    


class Solution_dp(object):
    def coinChange(self, coins, amount):
        maxval = amount + 1
        coin_count = [maxval] * maxval
        coin_used  = [0] * maxval
        self.helper(coins, amount, coin_count, coin_used)
        
        print(coin_count)
        print(coin_used)

        print("coins used: ", end=" ")

        value = amount
        while(value and coin_used[value]):
            print(coin_used[value], end=" ")
            value = value - coin_used[value]
        print("\nmin number of coins: ", end=" ")    

        if(coin_count[-1] > amount):
            return -1
        return coin_count[-1]

    def helper(self, coins, amount, coin_count, coin_used):
        coin_count[0] = 0
        for val in range(1, amount + 1):
            for coin in [c for c in coins if c <= val]:
                prev = val - coin
                count = 1 + coin_count[prev]
                if count < coin_count[val]:
                    coin_count[val] = count
                    coin_used[val] = coin



def main():
    
    sol_rc = Solution_rc()
    sol_dp = Solution_dp()

    coins = [2]
    amount = 3
    #print(sol_rc.coinChange(coins, amount))
    print("DP: ")
    print(sol_dp.coinChange(coins, amount))
    print("\n")

    coins = [1]
    amount = 0
    #print(sol_rc.coinChange(coins, amount))
    print("DP: ")
    print(sol_dp.coinChange(coins, amount))
    print("\n")

    coins = [1]
    amount = 1
    #print(sol_rc.coinChange(coins, amount))
    print("DP: ")
    print(sol_dp.coinChange(coins, amount))
    print("\n")

    coins = [2]
    amount = 4
    #print(sol_rc.coinChange(coins, amount))
    print("DP: ")
    print(sol_dp.coinChange(coins, amount))
    print("\n")

    coins = [1, 5, 10]
    amount = 15
    #print(sol_rc.coinChange(coins, amount))
    print("DP) ")
    print(sol_dp.coinChange(coins, amount))

    #test = TestCoins()
    #test.check(rec_coin_dyn)

if __name__ == "__main__":
    main()        