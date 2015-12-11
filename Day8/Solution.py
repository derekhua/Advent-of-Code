def main():
  f = open('input.txt', 'r')
  literal_count = 0
  memory_count = 0
  for line in f:
    stripped = line.strip('\n')
    literal_count += len(stripped) + 2
    memory_count += len(stripped.decode('unicode_escape'))
  f.close()
  print literal_count - memory_count


if __name__ == '__main__':
  main()
