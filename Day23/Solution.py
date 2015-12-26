'''
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

  hlf r sets register r to half its current value, then continues with the next instruction.
  tpl r sets register r to triple its current value, then continues with the next instruction.
  inc r increments register r, adding 1 to it, then continues with the next instruction.
  jmp offset is a jump; it continues with the instruction offset away relative to itself.
  jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
  jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
  All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

  The program exits when it tries to run an instruction beyond the ones defined.

  For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

    inc a
    jio a, +2
    tpl a
    inc a
    What is the value in register b when the program in your puzzle input is finished executing?

    Your puzzle answer was 307.

    --- Part Two ---

    The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer. Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?

    Your puzzle answer was 160.

    Both parts of this puzzle are complete! They provide two gold stars: **
'''
instructions = []
with open('input.txt', 'r') as f:
  instructions = f.readlines()
f.close()

# Registers
a = 1
b = 0

i = 0
while i < len(instructions):
  s = [x.strip() for x in instructions[i].split()]
  print '[' + str(i) + '] ' + str(s)
  if 'hlf' == s[0]:
    if 'a' in s[1]:
      a /= 2
    else:
      b /= 2
    i += 1
  elif 'tpl' == s[0]:
    if 'a' in s[1]:
      a *= 3
    else:
      b *= 3
    i += 1
  elif 'inc' == s[0]:
    if 'a' in s[1]:
      a += 1
    else:
      b += 1
    i += 1
  elif 'jmp' == s[0]:
    if '+' in s[1]:
      s[1] = s[1].replace('+', '')
      i += int(s[1])
    else:
      s[1] = s[1].replace('-', '')
      i -= int(s[1])
  elif 'jie' == s[0]:
    if 'a' in s[1]:
      if a % 2 == 0:
        if '+' in s[2]:
          s[2] = s[2].replace('+', '')
          i += int(s[2])
        else:
          s[2] = s[2].replace('-', '')
          i -= int(s[2])
      else:
        i += 1
    elif 'b' in s[1]:
      if b % 2 == 0:
        if '+' in s[2]:
          s[2] = s[2].replace('+', '')
          i += int(s[2])
        else:
          s[2] = s[2].replace('-', '')
          i -= int(s[2])
      else:
        i += 1
  elif 'jio' == s[0]:
    if 'a' in s[1]:
      if a == 1:
        if '+' in s[2]:
          s[2] = s[2].replace('+', '')
          i += int(s[2])
        else:
          s[2] = s[2].replace('-', '')
          i -= int(s[2])
      else:
        i += 1
    elif 'b' in s[1]:
      if b == 1:
        if '+' in s[2]:
          s[2] = s[2].replace('+', '')
          i += int(s[2])
        else:
          s[2] = s[2].replace('-', '')
          i -= int(s[2])
      else:
        i += 1
  print 'a:' + str(a) + ' b:' + str(b)
print b
