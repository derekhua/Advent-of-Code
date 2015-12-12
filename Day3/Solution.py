'''
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

  > delivers presents to 2 houses: one at the starting location, and one to the east.
  ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
  ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
  Your puzzle answer was 2081.

  --- Part Two ---

  The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

  Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

  This year, how many houses receive at least one present?

  For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
    Your puzzle answer was 2341.

    Both parts of this puzzle are complete! They provide two gold stars: **
'''
f = open('input.txt', 'r')
positions = set()
positions.add('0,0')
x = 0
y = 0
positions2 = set()
x1 = 0
y1 = 0
x2 = 0
y2 = 0
positions2.add('0,0')
santas_turn = True
for c in f.read():
  if c == '<':
    x -= 1
    if santas_turn: x1 -= 1
    else: x2 -= 1
  elif c == '^':
    y += 1
    if santas_turn: y1 += 1
    else: y2 += 1
  elif c == '>':
    x += 1
    if santas_turn: x1 += 1
    else: x2 += 1
  elif c == 'v':
    y -= 1
    if santas_turn: y1 -= 1
    else: y2 -= 1
  positions.add(str(x) + ',' + str(y))
  if santas_turn: positions2.add(str(x1) + ',' + str(y1))
  else: positions2.add(str(x2) + ',' + str(y2))
  santas_turn = not santas_turn
f.close()
print 'positions visited: ' + str(len(positions))
print 'next year positions visited: ' + str(len(positions2))
