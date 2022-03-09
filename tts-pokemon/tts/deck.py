#!/usr/bin/python
##-------------------------------##
## Tabletop Simulator            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Deck                          ##
##-------------------------------##

## Imports
from typing import Any

from .object import Object
from .card import Card



## Classes
class Deck(Object):
    """Tabletop Simulator Deck Object"""

    # -Constructor
    def __init__(self, *cards: Card, **kwargs) -> None:
        super().__init__("Deck", **kwargs)
        self.cards: list[Card] = [*cards]

    # -Instance Methods
    def to_dict(self) -> dict[str, Any]:
        '''Output TTS Deck to python dictionary'''
        dict_: dict[str, Any] = super().to_dict()
        dict_['DeckIDS'] = []
        dict_['ContainedObjects'] = []
        dict_['CustomDeck'] = {}
        for card in self.cards:
            cdict: dict = card.to_dict()
            dict_['DeckIDS'].append(card.id * 100)
            dict_['ContainedObjects'].append(cdict)
            dict_['CustomDeck'].update(cdict['CustomDeck'])
        return dict_
