def print_upper_words(list):
  """For a list of words, print out each word on a separate line, but in all uppercase."""
  for each_word in list:
    if each_word[0].lower() == 'e':
      print(each_word.upper())

print_upper_words(["eello", "hey", "eoodbye", "yo", "yes"])

def print_upper_words2(list, must_start_with = {}):
  """you should be able to pass in a set of letters, and it only prints words that start with one of those letters."""
  for each_word in list:
    if each_word[0] in must_start_with:
      print(each_word.upper())
    

print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})