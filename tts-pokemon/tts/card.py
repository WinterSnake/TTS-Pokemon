#!/usr/bin/python
##-------------------------------##
## Tabletop Simulator            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Card                          ##
##-------------------------------##

## Imports
from typing import Any

from .object import Object


## Classes
class Card(Object):
    """Tabletop Simulator Card Object"""

    # -Constructor
    def __init__(self, front_image: str, back_image: str, **kwargs) -> None:
        super().__init__(
            "CardCustom", hand_object=True, hidden_when_face_down=True, **kwargs
        )
        self.card_type: int = 0
        self.size: tuple[float, float] = (1, 1)  # Vector2
        self.images: tuple[str, str] = (front_image, back_image)
        self.back_image_as_hidden: bool = True
        self.unique_back: bool = False

    # -Instance Methods
    def to_dict(self) -> dict[str, Any]:
        '''Output TTS Card to python dictionary'''
        dict_: dict[str, Any] = super().to_dict()
        dict_['CardID'] = self.id * 100
        dict_['CustomDeck'] = {
            self.id: {
                'FaceURL': self.front_image,
                'BackURL': self.back_image,
                'NumWidth': self.size[0],
                'NumHeight': self.size[1],
                'BackIsHidden': self.back_image_as_hidden,
                'UniqueBack': self.unique_back,
                'Type': self.card_type,
            }
        }
        return dict_

    # -Properties
    @property
    def front_image(self) -> str:
        return self.images[0]

    @property
    def back_image(self) -> str:
        return self.images[1]
