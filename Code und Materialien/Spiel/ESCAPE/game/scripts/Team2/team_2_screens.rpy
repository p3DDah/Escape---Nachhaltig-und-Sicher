#alle Bilder die während des Spiels eingeblendet werden
screen Tresor():
    imagebutton:
        xalign 0.03
        yalign 0.2
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/Tresor.png"
        hover "Objekte/Maschinenraum/Tresor_Hover.png"
        action [Notify("Tresor"), Call("Tresor")]
        at transform:
            zoom 0.3

screen Whiteboard():
    imagebutton:
        xalign 0.95
        yalign 0.7
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/Whiteboard.png"
        hover "Objekte/Maschinenraum/Whiteboard_Hover.png"
        action [Notify("Whiteboard")]
        at transform:
            zoom 1

screen Figur_Hildegart():
    imagebutton:
        xalign 0.22
        yalign 0.44
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/Figur1_W.png"
        hover "Objekte/Maschinenraum/Figur1_W_Hover.png"
        action [Call("Hildegart")]
        at transform:
            zoom 0.3

screen Figur_Detlef():
    imagebutton:
        xalign 0.26
        yalign 0.38
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/Figur2_M.png"
        hover "Objekte/Maschinenraum/Figur2_M_Hover.png"
        action [Call("Detlef")]
        at transform:
            zoom 0.27

screen Figur_Dobby():
    imagebutton:
        xalign 0.37
        yalign 0.37
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/Figur3_M.png"
        hover "Objekte/Maschinenraum/Figur3_M_Hover.png"
        action [Call("Dobby")]
        at transform:
            zoom 0.27

screen Figur_Gudrun():
    imagebutton:
        xalign 0.31
        yalign 0.365
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/Figur4_W.png"
        hover "Objekte/Maschinenraum/Figur4_W_Hover.png"
        action [Call("Gudrun")]
        at transform:
            zoom 0.26

screen Figur_Ludwig():
    imagebutton:
        xalign 0.42
        yalign 0.4
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/Figur5_M.png"
        hover "Objekte/Maschinenraum/Figur5_M_Hover.png"
        action [Call("Ludwig")]
        at transform:
            zoom 0.28

screen gotoMachineRoomDoor():
    imagebutton:
        xalign 0.5
        yalign 0.4172
        sensitive ImageButtonActivate_state
        idle "Objekte/door.png"
        hover "Objekte/door_hover.png"
        action Call("machineRoomDoorClicked")

screen machineroomKeycard():
    imagebutton:
        xalign 0.1
        yalign 0.9
        sensitive ImageButtonActivate_state
        idle "Objekte/keycard.png"
        action [Hide("machineroomKeycard"), Play("sound", "audio/item_found.mp3"),
                SetVariable("tookKeycard", True), AddToSet(inventory, keycard)]
        at keycardSize

screen machineRoomPinpad():
    imagebutton:
        xalign 0.68
        yalign 0.4
        sensitive ImageButtonActivate_state
        idle "Objekte/pinpad.png"
        hover "Objekte/pinpad_hover.png"
        action Call("machineRoomPinpadClicked")

screen sicherung_40A():
    imagebutton:
        xalign 0.85
        yalign 0.81
        at transform:
            zoom 0.8
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/sicherung_40_A.png"
        action [Hide("sicherung_40A"), Play("sound", "audio/item_found.mp3"),
                AddToSet(inventory, sicherung_40A), SetVariable("tookWA40", True)]

screen sicherung_80A():
    imagebutton:
        xalign 0.632
        yalign 0.4
        at transform:
            zoom 0.6
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/Sicherung_80_A.png"
        action [Hide("sicherung_80A"), Play("sound", "audio/item_found.mp3"),
                AddToSet(inventory, sicherung_80A), SetVariable("tookWA80", True)]

screen generatorCover():
    imagebutton:
        xalign 0.512
        yalign 0.787
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/generatorCover.png"
        hover "Objekte/Maschinenraum/generatorCover_hover.png"
        action Call("generatorCoverClicked")

screen computerWand():
    imagebutton:
        xalign 0.7115
        yalign 0.392
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/computerWand.png"
        hover "Objekte/Maschinenraum/computerWand_hover.png"
        action Call("computerWandClicked")

screen endDoor_mr():
    imagebutton:
        xalign 0.571
        yalign 0.36
        sensitive ImageButtonActivate_state
        idle "Objekte/Maschinenraum/endDoor.png"
        hover "Objekte/Maschinenraum/endDoor_hover.png"
        action Call("startDuesen")
