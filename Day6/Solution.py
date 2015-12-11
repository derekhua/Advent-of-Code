'''
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

  turn on 0,0 through 999,999 would turn on (or leave on) every light.
  toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
  turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
  After following the instructions, how many lights are lit?
'''

def main():
  f = open('input.txt', 'r')
  lights = [[0 for x in range(1000)] for x in range(1000)] 
  
  for line in f:
    splitted = line.split()
    if 'toggle' in line:
      pair1 = splitted[1]
      pair2 = splitted[3]
    else:
      pair1 = splitted[2]
      pair2 = splitted[4]
    
    x1 = int(pair1.split(',')[0])
    y1 = int(pair1.split(',')[1])
    x2 = int(pair2.split(',')[0])
    y2 = int(pair2.split(',')[1])

    if 'toggle' in line:
      for x in xrange(x1, x2+1):
        for y in xrange(y1, y2+1):
          lights[y][x] = lights[y][x] ^ 1

    elif 'turn on' in line:
      for x in xrange(x1, x2+1):
        for y in xrange(y1, y2+1):
          lights[y][x] = 1

    elif 'turn off' in line:
      for x in xrange(x1, x2+1):
        for y in xrange(y1, y2+1):
          lights[y][x] = 0

  count = 0
  for arr in lights:
    for i in arr:
      if i == 1:
        count += 1

  print count

if __name__ == '__main__':
  main()
