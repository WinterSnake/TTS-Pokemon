#!/usr/bin/python
##-------------------------------##
## Tabletop Simulator            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Object                        ##
##-------------------------------##

## Imports
from typing import Any

## Constants
Vector3 = tuple[float, float, float]
Transform = tuple[Vector3, Vector3, Vector3]


## Classes
class Object:
    """Tabletop Simulator Base Object"""

    # -Constructor
    def __init__(
        self, type_: str, *, name: str = "", description: str = "",
        notes: str = "", ui: str = "", lua: str = "", lua_state: str = "",
        hand_object: bool = False, hidden_when_face_down: bool = False
    ) -> None:
        # -Object Meta-Data
        self.id: int = Object.id
        Object.id += 1
        self.type: str = type_
        self.sort: int = 0
        # -Object World Data
        self.transform: Transform = ((0, 0, 0), (0, 0, 0), (1, 1, 1))
        self.color: Vector3 = (1, 1, 1)
        self.locked: bool = False
        self.grid: bool = False
        self.snap: bool = False
        self.measure: bool = False
        self.auto_raise: bool = False
        self.hidden: bool = False
        self.sideways: bool = False
        # -Object String Data
        self.name: str = name
        self.description: str = description
        self.notes: str = notes
        self.ui: str = ui
        self.lua: str = lua
        self.lua_state: str = lua_state
        # -Object Data
        self.sticky: bool = True
        self.ignore_fow: bool = False
        self.drag_select: bool = True
        self.tooltip: bool = True
        self.projection: bool = False
        self.hand_object: bool = hand_object
        self.hidden_when_face_down: bool = hidden_when_face_down

    # -Instance Methods
    def to_dict(self) -> dict[str, Any]:
        '''Output TTS Object to python dictionary'''
        return {
            "GUID": f"{self.id:06X}",
            "Name": self.type,
            "Nickname": self.name,
            "Description": self.description,
            "GMNotes": self.notes,
            "XmlUI": self.ui,
            "LuaScript": self.lua,
            "LuaScriptState": self.lua_state,
            "Transform": {
                f"{label}{axis}": value
                for label, vec in zip(("pos", "rot", "scale"), self.transform)
                for axis, value in zip(("X", "Y", "Z"), vec)
            },
            "ColorDiffuse": {
                color: value for color, value in zip(("r", "g", "b"), self.color)
            },
            "LayoutGroupSortIndex": self.sort,
            "Locked": self.locked,
            "Grid": self.grid,
            "Snap": self.snap,
            "IgnoreFoW": self.ignore_fow,
            "MeasureMovement": self.measure,
            "DragSelectable": self.drag_select,
            "Autoraise": self.auto_raise,
            "Sticky": self.sticky,
            "Tooltip": self.tooltip,
            "GridProjection": self.projection,
            "HideWhenFaceDown": self.hidden,
            "Hands": self.hand_object,
            "SidewaysCard": self.sideways,
            "HideWhenFaceDown": self.hidden_when_face_down,
        }

    # -Class Properties
    id: int = 1
