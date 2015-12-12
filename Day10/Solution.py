'''
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

  1 becomes 11 (1 copy of digit 1).
  11 becomes 21 (2 copies of digit 1).
  21 becomes 1211 (one 2 followed by one 1).
  1211 becomes 111221 (one 1, one 2, and two 1s).
  111221 becomes 312211 (three 1s, two 2s, and one 1).
  Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

  Your puzzle input is 1113122113.
'''
# num_str is a string
# count is a in
# returns a string
def look_and_say(num_str, counts):
  if counts == 0:
    return num_str
  builder = ''
  candidate = num_str[0]
  count = 1
  for c in num_str[1:]:
    if c != candidate:
      builder += str(count) + candidate
      candidate = c
      count = 1
    else:
      count +=1
  builder+= str(count) + candidate
  return look_and_say(builder, counts-1)

def main():
  print len(look_and_say('1113122113', 40))
if __name__ == '__main__':
  main()
