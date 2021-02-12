"""
===========================================================================================================

# objective:
# 1: select n pizza for n-person team
# 2: no pizza is repeated
# 3: minimal repetition of ingredients
# 4: calculate score   ~~ this code is biased towards score
# 5: sort pizza in w.r.t ingredients (more to less)

===========================================================================================================
"""
# Code
import random as rm


# objective 1:
def select_pizza_for(n: int) -> list[int]:
    _ = [n]
    for i in range(n):
        _ += [choice()]
    if len(_) - 1 == n:
        return _  # format: [n-person team, pizza1, pizza2...]
    else:
        # if pizza count is less then n-person team
        # the team wont get any pizza
        for i in _[1:]:
            visited.remove(i)


# objective 2:
def choice() -> int:
    _________ = rm.choice(available)
    if _________ not in visited:
        visited.add(_________)
        return _________
    return choice()


# objective 3:
def check_minimal_repetition(ingredients: list[int]) -> list[int]:
    pass


# objective 4:
def calculate_score(delivery: list[int]) -> int:
    ingredients = set()
    for i in delivery[1:]:
        ingredients.union(set(pizza[i]))
    return len(ingredients) ** 2  # score of each delivery


# objective 5:
def sort_pizza():
    temp_set = set()
    for i in pizza.keys():



# input
pizza_count, team_of_two, team_of_three, team_of_four = map(int, input().split())
pizza = {i: input().split() for i in range(pizza_count)}

visited = set()  # to check if pizza is repeated or not
available = list(pizza.keys())

# driver code
if __name__ == '__main__':
    pass
