'''
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

  Alice would gain 54 happiness units by sitting next to Bob.
  Alice would lose 79 happiness units by sitting next to Carol.
  Alice would lose 2 happiness units by sitting next to David.
  Bob would gain 83 happiness units by sitting next to Alice.
  Bob would lose 7 happiness units by sitting next to Carol.
  Bob would lose 63 happiness units by sitting next to David.
  Carol would lose 62 happiness units by sitting next to Alice.
  Carol would gain 60 happiness units by sitting next to Bob.
  Carol would gain 55 happiness units by sitting next to David.
  David would gain 46 happiness units by sitting next to Alice.
  David would lose 7 happiness units by sitting next to Bob.
  David would gain 41 happiness units by sitting next to Carol.
  Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

  If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

         +41 +46
         +55   David    -2
         Carol       Alice
         +60    Bob    +54
              -7  +83
              After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

              What is the total change in happiness for the optimal seating arrangement of the actual guest list?

              Your puzzle answer was 618.

              --- Part Two ---

              In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

              So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

              What is the total change in happiness for the optimal seating arrangement that actually includes yourself?

              Your puzzle answer was 601.

              Both parts of this puzzle are complete! They provide two gold stars: **
'''
from collections import defaultdict
from itertools import permutations

# arragement is a collection
# happiness_map is a 2d dict
# returns an int as the happiness level from the arrangement
def happiness_calc(arrangement, happiness_map):
  return sum([happiness_map[x][arrangement[(i+1)%len(arrangement)]] + happiness_map[x][arrangement[i-1]] for i, x in enumerate(arrangement)])

# Find all the names of the people
names = set()
happiness_map = defaultdict(dict)
with open('input.txt', 'r') as f:
  list_file = f.readlines()
  for x in list_file:
    splitted = x.split()
    names.add(splitted[0])
    if 'gain' in x:
      happiness_map[splitted[0].replace('.', '')][splitted[10].replace('.','')] = [int(s) for s in splitted if s.isdigit()][0]
    elif 'lose' in x:
      happiness_map[splitted[0].replace('.', '')][splitted[10].replace('.','')] = -1 * [int(s) for s in splitted if s.isdigit()][0]
    # Part 2
    happiness_map[splitted[0]]['Me'] = 0
    happiness_map['Me'][splitted[0]] = 0
f.close()
# Part 1
perm = list(permutations(names))
max_hap = 0
optim = list()
for p in perm:
  num = happiness_calc(p, happiness_map)
  if num > max_hap:
    max_hap = num
    optim = p
print 'max happiness: ' + str(max_hap)
# Part 2
new_hap = 0
for i in xrange(len(optim)):
  temp = list(optim)
  temp.insert(i, 'Me')
  new_hap = max(new_hap, happiness_calc(temp, happiness_map))
print 'happiness w/ me: ' + str(new_hap)
