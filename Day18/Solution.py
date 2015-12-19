'''
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

  1B5...
  234...
  ......
  ..123.
  ..8A4.
  ..765.
  The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    All of the lights update simultaneously; they all consider the same current state before moving to the next.

    Here's a few steps from an example configuration of another 6x6 grid:

      Initial state:
        .#.#.#
        ...##.
#....#
        ..#...
#.#..#
####..

        After 1 step:
          ..##..
          ..##.#
          ...##.
          ......
#.....
#.##..

          After 2 steps:
            ..###.
            ......
            ..###.
            ......
            .#....
            .#....

            After 3 steps:
              ...#..
              ......
              ...#..
              ..##..
              ......
              ......

              After 4 steps:
                ......
                ......
                ..##..
                ..##..
                ......
                ......
                After 4 steps, this example has four lights on.

                In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

                Your puzzle answer was 814.

                --- Part Two ---

                You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

                Initial state:
##.#.#
                ...##.
#....#
                ..#...
#.#..#
####.#

                After 1 step:
#.##.#
####.#
                ...##.
                ......
#...#.
#.####

                After 2 steps:
#..#.#
#....#
                .#.##.
                ...##.
                .#..##
##.###

                After 3 steps:
#...##
####.#
                ..##.#
                ......
##....
####.#

                After 4 steps:
#.####
#....#
                ...#..
                .##...
#.....
#.#..#

                After 5 steps:
##.###
                .##..#
                .##...
                .##...
#.#...
##...#
                After 5 steps, this example now has 17 lights on.

                In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?

                Your puzzle answer was 924.

                Both parts of this puzzle are complete! They provide two gold stars: **
'''
def neighbor_count(grid, x, y):
  count = 0
  if x-1 >= 0 and y-1 >= 0 and grid[y-1][x-1] == '#': count += 1
  if x+1 < 100 and y-1 >= 0 and grid[y-1][x+1] == '#': count += 1
  if x-1 >= 0 and y+1 < 100 and grid[y+1][x-1] == '#': count += 1
  if x+1 < 100 and y+1 < 100 and grid[y+1][x+1] == '#': count += 1
  if y-1 >= 0 and grid[y-1][x] == '#': count += 1
  if x+1 < 100 >= 0 and grid[y][x+1] == '#': count += 1
  if y+1 < 100 and grid[y+1][x] == '#': count += 1
  if x-1 >= 0 and grid[y][x-1] == '#': count += 1
  return count

grid = []
with open('input.txt', 'r') as f:
  grid = [[c for c in line.strip()] for line in f]
f.close()

# Part 2 setup
grid[0][0] = '#'
grid[0][99] = '#'
grid[99][0] = '#'
grid[99][99] = '#'

for i in xrange(100):
  newgrid = [row[:] for row in grid]
  for x in xrange(100):
    for y in xrange(100):
      if (x == 0 and y == 0) or (x == 0 and y == 99) or \
         (x == 99 and y == 0) or (x == 99 and y == 99):
        continue
      elif grid[y][x] == '#':
        count = neighbor_count(grid, x, y)
        if count != 2 and count != 3: newgrid[y][x] = '.'
      else:
        count = neighbor_count(grid, x, y)
        if count == 3: newgrid[y][x] = '#'
  grid = newgrid
print sum([sum([1 for col in row if col == '#']) for row in grid])

