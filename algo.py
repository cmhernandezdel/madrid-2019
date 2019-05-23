import sys.argv

bag = {}

# Read file and send every line to parse
def read_file(input_file):
  with open(input_file, "r") as file_stream:
    for line in file_stream:
      tokens = line.split(" ")
      parse_token(token)


# Parse token and add it to the dictionary
def parse_token(token):
  for word in token:
    if word in bag:
      bag[word] += 1
    else:
      bag[word] = 1

read_file(argv[1])
print(bag)