"""
🍳 Problem: Validate Recipes with Ingredients

You are given two lists:

ingredients: a list of strings representing available ingredients, in a fixed order.

recipes: a list of recipe strings to validate.

A recipe is valid if it can be formed by concatenating the first k ingredients from the list (where k ≥ 0).

You must respect the order of the ingredients.

You cannot skip any ingredient.

You cannot cut an ingredient in the middle.

Return a list of booleans, one for each recipe, indicating whether the recipe is valid.

Example 1
ingredients = ["flour", "sugar"]
recipes = ["floursugar", "random"]

Output: [True, False]


Explanation:

"floursugar" = "flour" + "sugar" → valid.

"random" does not match → invalid.

Example 2
ingredients = ["egg","milk","sugar"]
recipes = ["eggmilksugar","eggmilk","eggsugar"]

Output: [True, True, False]


Explanation:

"eggmilksugar" = "egg" + "milk" + "sugar" → valid.

"eggmilk" = "egg" + "milk" (prefix) → valid.

"eggsugar" skips "milk" → invalid.

Constraints

0 <= len(ingredients), len(recipes) <= 1000

Each ingredient and recipe consists only of lowercase English letters.

The total length of all strings will not exceed 10⁵.

Python Solution
"""
from typing import List

class Solution:
    def canMakeRecipes(self, ingredients: List[str], recipes: List[str]) -> List[bool]:
        """
        A recipe is valid if it equals the concatenation of the first k ingredients
        (k >= 0), without skipping or cutting any ingredient.
        """
        results = []
        for recipe in recipes:
            pos = 0
            valid = True
            for ing in ingredients:
                if pos == len(recipe):
                    break
                end = pos + len(ing)
                if end <= len(recipe) and recipe[pos:end] == ing:
                    pos = end
                else:
                    valid = False
                    break
            results.append(valid and pos == len(recipe))
        return results

s = Solution()

# Example 1
print(s.canMakeRecipes(["flour","sugar"], ["floursugar", "random"]))
# [True, False]

# Example 2
print(s.canMakeRecipes(["egg","milk","sugar"], ["eggmilksugar","eggmilk","eggsugar"]))
# [True, True, False]

# Edge case: cannot cut ingredient in the middle
print(s.canMakeRecipes(["milk"], ["mi", "milk", "milks"]))
# [False, True, False]
