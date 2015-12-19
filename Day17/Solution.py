'''
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

  15 and 10
  20 and 5 (the first 5)
  20 and 5 (the second 5)
  15, 5, and 5
  Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

  Your puzzle answer was 654.

  --- Part Two ---

  While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

  Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

  In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

  Your puzzle answer was 57.

  Both parts of this puzzle are complete! They provide two gold stars: **


'''
# Part 1
def combos(index, numbers, current, amount, size_list):
  if current < 0: return 0
  if current == 0:
    size_list.append(amount)
    return 1
  count = 0
  for x in range(index + 1, len(numbers)):
    count += combos(x, numbers, current - numbers[x], amount + 1, size_list)
  return count

# Part 2
def combos2(index, numbers, current, amount, size):
  if current < 0: return 0
  if current == 0 and amount == size:
    return 1
  count = 0
  for x in range(index + 1, len(numbers)):
    count += combos2(x, numbers, current - numbers[x], amount + 1, size)
  return count


numbers = []
with open('input.txt', 'r') as f:
  numbers = [int(num) for num in f]
f.close()
print numbers

size_list = []
count = combos(-1, numbers, 150, 0, size_list)
print count

print min(size_list)

count2 = combos2(-1, numbers, 150, 0, min(size_list))
print count2
