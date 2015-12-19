'''
--- Day 19: Medicine for Rudolph ---

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

  H => HO
  H => OH
  O => HH
  Given the replacements above and starting with HOH, the following molecules could be generated:

  HOOH (via H => HO on the first H).
  HOHO (via H => HO on the second H).
  OHOH (via H => OH on the first H).
  HOOH (via H => OH on the second H).
  HHHH (via O => HH).
  So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

  The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

  Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?

  Your puzzle answer was 509.

  --- Part Two ---

  Now that the machine is calibrated, you're ready to begin molecule fabrication.

  Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.

  For example, suppose you have the following replacements:

  e => H
  e => O
  H => HO
  H => OH
  O => HH
  If you'd like to make HOH, you start with e, and then make the following replacements:

    e => O to get O
    O => HH to get HH
    H => OH (on the second H) to get HOH
    So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

    How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?

    Your puzzle answer was 195.

    Both parts of this puzzle are complete! They provide two gold stars: **
'''
text =  'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

# Part 1
reps = []
with open('input.txt', 'r') as f:
  for line in f:
    line = line.split('=>')
    reps.append((line[0].strip(), line[1].strip()))
f.close()

new_textecules = set()
for rep in reps:
  index = 0
  while index < len(text):
    index = text.find(rep[0], index)
    if index == -1: break
    new_textecules.add(text[:index] + rep[1] + text[index+len(rep[0]):])
    index += len(rep[0])

print len(new_textecules)


# Part 2
from random import shuffle
target = text
part2 = 0

while target != 'e':
  tmp = target
  for a, b in reps:
    if b not in target:
      continue
    target = target.replace(b, a, 1)
    part2 += 1
  if tmp == target:
    target = text
    part2 = 0
    shuffle(reps)

print part2
