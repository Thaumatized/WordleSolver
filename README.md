Word filter, useful for solving wordles, such as https://www.nytimes.com/games/wordle/index.html

dictionary.txt is words_alpha.txt from: https://github.com/dwyl/english-words
it may not be perfect for this purpose, as it contains a lot of abbreviations and such. It also contains way too many words, which different wordle implementations do not accept as valid answers. The one currently in use is also kind of inconsistent, containing some names but not nearly all (eg. it has allie but not ellie, neither of which are accepted as answers by the new york times wordle)

supports different length words. A good place to play 4-11 length words is https://wordlegame.org/9-letter-words-wordle

TODO
- Generate all still possible letter combinations if the word is not found.
- Smarter srategy for finding the correct words, where we take "guesses" which can't be the correct one, but reveal information about other letters, stripping down possibilities further.
- (possibly) look for a dictionary, which better matches most wordle implementations.
