def cakes(recipe, available):
  return min(available.get(ingredients,0)//amount for ingredients, amount in recipe.items())
import codewars_test as test
from solution import cakes

@test.it('Testing Pete, the Baker')
def _():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    test.assert_equals(cakes(recipe, available), 2, 'example #1')
    
    recipe = {"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000}
    test.assert_equals(cakes(recipe, available), 11, 'example #2')

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    test.assert_equals(cakes(recipe, available), 0, 'example #3')