'''
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

  London to Dublin = 464
  London to Belfast = 518
  Dublin to Belfast = 141
  The possible routes are therefore:

    Dublin -> London -> Belfast = 982
    London -> Dublin -> Belfast = 605
    London -> Belfast -> Dublin = 659
    Dublin -> Belfast -> London = 659
    Belfast -> Dublin -> London = 605
    Belfast -> London -> Dublin = 982
    The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

    What is the distance of the shortest route?

    Your puzzle answer was 251.

    --- Part Two ---

    The next year, just to show off, Santa decides to take the route with the longest distance instead.

    He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

    For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

    What is the distance of the longest route?

    Your puzzle answer was 898.

    Both parts of this puzzle are complete! They provide two gold stars: **
'''
from collections import defaultdict
import sys

# graph is 2d dict
# visited is set
# city_num is int
# current_city is string
# distance is int
# returns int
def shortest_path(graph, visited, city_num, current_city, distance):
  visited.add(current_city)
  if len(visited) == city_num:
    visited.discard(current_city)
    return distance
  part_distance = sys.maxint
  for city in graph[current_city]:
    if city not in visited:
      num = shortest_path(graph, visited, city_num, city, distance+graph[current_city][city])
      if num != -1:
        part_distance = min(part_distance, num)
  visited.discard(current_city)
  return part_distance if part_distance != sys.maxint else -1

# graph is 2d dict
# visited is set
# city_num is int
# current_city is string
# distance is int
# returns int
def longest_path(graph, visited, city_num, current_city, distance):
  visited.add(current_city)
  if len(visited) == city_num:
    visited.discard(current_city)
    return distance
  part_distance = 0
  for city in graph[current_city]:
    if city not in visited:
      num = longest_path(graph, visited, city_num, city, distance+graph[current_city][city])
      if num != -1:
        part_distance = max(part_distance, num)
  visited.discard(current_city)
  return part_distance if part_distance != 0 else -1

# Create graph
with open('input.txt', 'r') as f:
  graph = defaultdict(dict)
  for line in f:
    left = line.split('=')[0].strip()
    right = int(line.split('=')[1].strip())
    leftcity = left.split('to')[0].strip()
    rightcity = left.split('to')[1].strip()
    graph[leftcity][rightcity] = right
    graph[rightcity][leftcity] = right
f.close()
smallest = sys.maxint
for city in graph:
  smallest = min(smallest, shortest_path(graph, set(), len(graph), city, 0))
print 'smallest distance: ' + str(smallest)
largest = 0
for city in graph:
  largest = max(largest, longest_path(graph, set(), len(graph), city, 0))
print 'largest distance: ' + str(largest)
