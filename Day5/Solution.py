'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

  It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
  It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
  It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
  For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.
    How many strings are nice?
'''
# input is a string
# returns boolean
def has_three_vowels(s):
  count = 0
  for c in s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
      count += 1
    if count >= 3:
      return True
  return False

# input is a string
# returns a boolean
def has_double_letter(s):
  for index, c in enumerate(s[:-1]):
    if c == s[index+1]:
      return True
  return False

# input is a string
# returns a boolean
def not_contains_strings(s):
  return 'ab' not in s and 'cd' not in s and 'pq' not in s and 'xy' not in s

def main():
  f = open('input.txt', 'r')
  nice = 0
  for line in f:
    if has_three_vowels(line) and has_double_letter(line) and not_contains_strings(line):
      nice += 1
  print nice

if __name__ == '__main__':
  main()
