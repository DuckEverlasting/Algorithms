#!/usr/bin/python

import math

# recipe and ingredients are both dicts
def recipe_batches(recipe, ingredients):
    count = None
    for i in recipe:
        try:
            if not count or count > ingredients[i] // recipe[i]:
                count = ingredients[i] // recipe[i]
        except:
            return 0
    return count


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )
