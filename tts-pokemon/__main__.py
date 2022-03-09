#!/usr/bin/python
##-------------------------------##
## [Tabletop Simulator]Pokemon   ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
from tts import Card, Deck


## Functions
def generate_pokemon_card(name: str, image: str) -> Card:
    '''Generate TTS pokemon card'''
    # url: str = "https://pkmncards.com/wp-content/uploads/"
    return Card(
        name=name, front_image=image,
        back_image=("http://cloud-3.steamusercontent.com/ugc/1768195981648309989/"
                    "9ABD9158841F1167D295FD1295D7A597E03A7487/")
    )

## Body
