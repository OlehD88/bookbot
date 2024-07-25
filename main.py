def main():
  path = "books/frankenstein.txt"
  document = get_document_str(path)
  words_count = count_words(document)
  characters_count = get_characters_count(document)
  characters_list = get_characters_list(characters_count)

  print_report(words_count, characters_list)

def count_words(str):
  return len(str.split())

def get_characters_count(str):
  characters = {}
  lowered = str.lower()

  for char in lowered:
    if char in characters:
      characters[char] += 1
    else:
      characters[char] = 1

  return characters

def get_document_str(path_to_book):
  with open(path_to_book) as f:
    file_contents = f.read()
    return file_contents

def get_characters_list(characters_count):
  characters_list = []

  def sort_on(dict):
    return dict["count"]

  for char in characters_count:
    new_item = {}
    if char.isalpha():
      new_item["char"] = char
      new_item["count"] = characters_count[char]
      characters_list.append(new_item)

  characters_list.sort(reverse = True, key=sort_on)
  return characters_list

def print_report(words_count, characters_list):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{words_count} words found in the document")

  for item in characters_list:
    char_name = item["char"]
    char_count = item["count"]
    print(f"The '{char_name}' character was found {char_count} times")

main()