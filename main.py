import nltk

# Check if the wordnet package has been downloaded
try:
  nltk.data.find("corpora/wordnet")
except LookupError:
  nltk.download("wordnet")

from nltk.corpus import wordnet

def get_synonyms(word):
  synonyms = []
  for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
      # Only include single-word vocabulary that is different from the original word
      if " " not in lemma.name() and lemma.name() != word:
        synonyms.append(lemma.name())
  return synonyms[:5]

def main():
  # Prompt the user for a word
  word = input("Type in a word: ")

  # Get synonyms
  synonyms = get_synonyms(word)

  if not synonyms:
    # No synonyms found
    print("No synonyms were found.")
  else:
    # Print the synonyms, 1 per line
    for s in synonyms:
      print(s)

if __name__ == "__main__":
  main()