'''
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

  123 -> x means that the signal 123 is provided to wire x.
  x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
  p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
  NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
  Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

  For example, here is a simple circuit:

    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i
    After it is run, these are the signals on the wires:

      d: 72
      e: 507
      f: 492
      g: 114
      h: 65412
      i: 65079
      x: 123
      y: 456
      In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

      Your puzzle answer was 16076.

      --- Part Two ---

      Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

      Your puzzle answer was 2797.

      Both parts of this puzzle are complete! They provide two gold stars: **
'''

# values is dict
# lines is file lines
# target is string
# returns int
def find_value(values, lines, target):
  if target.isdigit():
    return int(target)
  if target in values:
    return values[target]
  for line in lines:
    splitted = line.split('->')
    # Found target
    if splitted[1].strip() == target:
      left = splitted[0].strip()  # Left side of equation
      if left.isdigit():
        values[target] = int(left)
        return int(left)
      else:
        leftlist = left.split()
        if 'NOT' in left:
          values[target] = ~find_value(values, lines, leftlist[1])
        elif 'OR' in left:
          values[target] = find_value(values, lines, leftlist[0]) | find_value(values, lines, leftlist[2])
        elif 'AND' in left:
          values[target] = find_value(values, lines, leftlist[0]) & find_value(values, lines, leftlist[2])
        elif 'LSHIFT' in left:
          values[target] = find_value(values, lines, leftlist[0]) << find_value(values, lines, leftlist[2])
        elif 'RSHIFT' in left:
          values[target] = find_value(values, lines, leftlist[0]) >> find_value(values, lines, leftlist[2])
        else:
          values[target] = find_value(values, lines, leftlist[0])
        return values[target]

f = open('input.txt', 'r')
lines = f.readlines()
values = dict()
a = find_value(values, lines, 'a')
print a
values = dict()
values['b'] = a
print find_value(values, lines, 'a')
f.close()
