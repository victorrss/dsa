"""
Currency Trading Challenge
--------------------------

Imagine you are creating an algorithm for currency trading. 
Each day, it can buy one unit of currency, sell one unit of currency, or do nothing.

You are given:
- rates: an array of integers, where rates[i] is the price on day i.
- strategy: an array of -1, 0, 1 representing:
    -1 = buy
     0 = hold (do nothing)
     1 = sell
- k: an even integer

You are allowed to **modify exactly one consecutive subsequence of length k** 
in the following way:
    - the first half of that subsequence becomes 0 (hold)
    - the second half becomes 1 (sell)

Your task:
----------
Return the maximum profit achievable after optimally applying this modification.

Profit is defined as:
    (sum of selling prices) - (sum of buying prices)

It is guaranteed that you always have enough money and inventory to perform any operation.

---------------------------------------------------
Example:

rates    = [2, 4, 1, 5, 10, 6]
strategy = [-1, 1, 0, 1, -1, 0]
k        = 4

Original profit = -3
After optimal modification → maximum profit = 18

---------------------------------------------------
Your task is to implement the function:

    def solution(rates, strategy, k) -> int

and make all test cases pass.

"""

from typing import List


def solution(rates: List[int], strategy: List[int], k: int) -> int:
    """
    Complete this function.

    Approach hint:
    --------------
    1. Compute the base profit from the original strategy.
    2. Try every possible subsequence of length k.
    3. For each subsequence:
        - remove its original effect,
        - apply the new [0...0, 1...1] effect,
        - compute the new profit.
    4. Return the maximum profit found.

    Note: 
    A brute-force approach is fine for practicing,
    but for very large inputs (n up to 10^5), 
    you should think about prefix sums to optimize.
    """
    n = len(rates)

    # Função auxiliar que calcula o lucro total
    # dado um array de estratégia
    def calc_profit(strat):
        profit = 0
        for i in range(n):
            if strat[i] == -1:      # compra
                profit -= rates[i]
            elif strat[i] == 1:     # venda
                profit += rates[i]
            # se for 0, não muda nada
        return profit

    best = float('-inf')  # começa com lucro muito baixo

    # Vamos testar TODAS as janelas possíveis de tamanho k
    print("n - k + 1 : ", n - k + 1)
    for start in range(n - k + 1):
        # Copia a estratégia original
        new_strat = strategy[:]
        # Primeira metade da janela vira "0" (hold)

        for i in range(start, start + k//2):
            new_strat[i] = 0
        # Segunda metade da janela vira "1" (sell)
        for i in range(start + k//2, start + k):
            new_strat[i] = 1

        # Calcula o lucro dessa nova estratégia
        profit = calc_profit(new_strat)

        # Atualiza o melhor lucro encontrado
        best = max(best, profit)

    return best


# ---------------------------------------------------
# Test cases
# ---------------------------------------------------

def run_tests():
    tests = [
        {
            "rates": [2, 4, 1, 5, 10, 6],
            "strategy": [-1, 1, 0, 1, -1, 0],
            "k": 4,
            "expected": 18
        },
        {
            "rates": [5, 5, 5, 5],
            "strategy": [-1, -1, 1, 1],
            "k": 2,
            "expected": 15
        },
        {
            "rates": [3, 8, 2, 6],
            "strategy": [-1, 0, 1, 0],
            "k": 2,
            "expected": 10
        },
    ]

    for i, test in enumerate(tests, 1):
        result = solution(test["rates"], test["strategy"], test["k"])
        print(f"Test {i}: result={result}, expected={test['expected']}")
        assert result == test["expected"], f"❌ Test {i} failed!"
    print("✅ All tests passed!")


if __name__ == "__main__":
    run_tests()
