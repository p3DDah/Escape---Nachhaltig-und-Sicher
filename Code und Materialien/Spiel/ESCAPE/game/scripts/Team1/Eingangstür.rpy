label start_team_1:
    #init variables for this chapter
    call InitVars from _call_InitVars
    scene door_cockpit
    $ ShowScreen("bars")
    $ ShowScreen("cockpitKeycard")
    $ ShowScreen("inventory_button")
    $ ShowScreen("Hinweis_button")
    $ ShowScreen("cockpitDoorPinpad")
    $ ShowScreen("gotoCockpitDoor")
    $ renpy.pause(hard=True)

#Vorraum
label cockpitDoorClicked: #door functionality
    if doorLocked == True:
        play sound "audio/door_denied.mp3"
        $ renpy.notify("Verschlossen")
    else:
        play sound "audio/door_open.mp3"
        pause 3.0
        #jump to cockpit_room.rpy
        jump Cockpit_Standard
    $ renpy.pause(hard=True)

label cockpitPinpadClicked: #pinpad functionality
    if tookKeycard == False:
        play sound "audio/door_denied.mp3"
        $ renpy.notify("Schlüsselkarte benötigt")
    else:
        $ doorLocked = False
        play sound "audio/code_accept.mp3"
        $ renpy.notify("Zugang gewährt!")
    $ renpy.pause(hard=True)

label InitVars:
    #init variables
    $ foundMonitors = False
    $ repairedKeyboard = False
    $ foundAllKeys = False
    #amout of electricity, max 300
    $ currentep = 300
    $ maxep = 300
    #amount of data volume, max 300
    $ currentdp = 300
    $ maxdp = 300
    return
