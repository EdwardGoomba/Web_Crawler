index = []

def add_to_index(index, keyword, url):
  for entry in index:
    if entry[0] == keyword:
      if not url in entry[1]:
        entry[1].append(url)
      return
  index.append([keyword, [url]])
  
def lookup(index, word):
    for entry in index:
      if entry[0] == keyword:
        return entry[1]
    return []

def add_page_to_index(index, url, content):
  words = content.split()
  for word in words:
    add_to_index(index, word, url)
