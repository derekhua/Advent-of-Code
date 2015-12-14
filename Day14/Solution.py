'''
s year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

  Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
  Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
  After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

  In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

  Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

  Your puzzle answer was 2640.

  --- Part Two ---

  Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

  Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

  Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

  After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

  Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

  Your puzzle answer was 1102.

  Both parts of this puzzle are complete! They provide two gold stars: **
'''
class Reindeer:
  name = ''
  kmps = 0
  travel_time = 0
  rest_time = 0
  distance_traveled = 0
  curr_rest = 0
  curr_travel = 0
  travel = True
  part2points = 0
  def __init__(self, line):
    words = line.split()
    self.name = words[0]
    self.kmps = int(words[3])
    self.travel_time = int(words[6])
    self.rest_time = int(words[-2])

  def __str__(self):
    return self.name + ' ' + str(self.kmps) + ' ' + str(self.travel_time) + ' ' + str(self.rest_time) + ' ' + str(self.distance_traveled)

  def inc(self):
    if self.travel:
      self.distance_traveled += self.kmps
      self.curr_travel += 1
    else:
      self.curr_rest += 1
    if self.curr_travel > self.travel_time - 1:
      self.curr_travel = 0
      self.travel = False
    elif self.curr_rest > self.rest_time - 1:
      self.curr_rest = 0
      self.travel = True


seconds = 2503
deer = list()
with open('input.txt', 'r') as f:
  deer = [Reindeer(line) for line in f]
f.close()

for x in xrange(seconds):
  for d in deer:
    d.inc()
  deer = sorted(deer, reverse=True, key=lambda x: x.distance_traveled)
  maxnum = deer[0].distance_traveled
  for d in deer:
    if d.distance_traveled == maxnum:
      d.part2points += 1
print str(max(deer, key=lambda x: x.distance_traveled))
print max(deer, key = lambda x: x.part2points).part2points


