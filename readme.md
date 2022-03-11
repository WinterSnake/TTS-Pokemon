# Pokemon Deck Generator
## Description
Pokemon Deck Generator is a Python script that reads in text files passed in via command line and generates Tabletop Simulator compatible decks and cards to use in-game.

## How to use
To run the script, you will need one or more text files with links to pokemon cards from https://pkmncards.com/ where every line holds a link.

For instance, if you wanted to have [Leafeon](https://pkmncards.com/card/leafeon-sword-shield-promos-swsh191/), you would have a text file with:
```
https://pkmncards.com/card/leafeon-sword-shield-promos-swsh191/
...
```

Then, to generate a TTS compatible object, you would include the file in the command line:
`python tts-pokemon "my-deck.txt"`
This will output 2 files: `my-deck.json` and `my-deck.png` which is the image of the very first card in your text file (in this example, it would be the Leafeon). You will then move the `json` and `png` file to your [Saved Objects folder](https://steamcommunity.com/app/286160/discussions/0/2860219962100643488/).

## TODO
- [ ] Deck Limits and Checking
- [ ] GUI

## Other resources for building a deck
[Deck Building Introduction](https://www.pokemon.com/us/strategy/designing-a-deck-from-scratch/)
[First Pokemon TCG Deck](https://www.youtube.com/watch?v=1zJLV17NFPg)
