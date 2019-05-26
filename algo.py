import sys

bag = {}
stopwords = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'en',
'entre', 'hacia', 'hasta', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras',
'mediante', 'durante', 'el', 'la', 'lo', 'los', 'las', 'un', 'una', 'uno', 'unos', 'unas',
'y', 'o', 'e', '', 'que', 'se', 'del', 'al', 'como', 'es', 'más', 'su', 'sus',
'suyo', 'suyos', 'más', 'además', 'también', 'no', 'ha', 'han', 'esta', 'este', 'etc']

# Read file and send every line to parse
def read_file(input_file):
  with open(input_file, encoding="latin-1") as file_stream:
    for line in file_stream:
      line = line.strip()
      token = line.split(" ")
      parse_token(token)


# Parse token and add it to the dictionary
def parse_token(token):
  for word in token:
    word = word.replace(',', '')
    word = word.replace('.', '')
    word = word.lower()
    if word in bag and word not in stopwords:
      bag[word] += 1
    else:
      bag[word] = 1

read_file(sys.argv[1])
bag = {k:v for k,v in bag.items() if v > 1}
orderedBag = sorted(bag.items(), key=lambda x: x[1], reverse=True)
print(orderedBag)