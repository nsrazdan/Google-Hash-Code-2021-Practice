# Google Hash Code 2021 Practice
# Authors
- Nikhil Razdan
- Harshit Joshi
# Greedy Solution
## Algorithm
- alg solution: O(m^2 * n)
- start with random team with largest size
- find best set of pizzas for that team
  - from first pizza:
  - if pizza is all unique ingredients, take it
  - if not, assign value to index (dictionary)
  - if no unique pizza found, add best to pizzas
  - repeat for all pizzas
- move on to next biggest team
- repeat until all teams done

# Score
- A – Example: 49 points
- B – A little bit of everything: 5,420 points
- C – Many ingredients: 90,964,440 points
- D – Many pizzas: 791,376 points
- E – Many teams: 6,628,821 points