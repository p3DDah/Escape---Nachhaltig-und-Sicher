define control = Character("Mission Control", image="erde")
define commander = Character("Commander", image="commander") #commander
define robot = Character("Roboter", image="robot")
define KI = Character("KI", image="KI")

define config.rollback_enabled = True
define config.allow_skipping = False
define config.main_menu_music = "audio/cockpit.mp3" #main music

define currentScreensList = []

default currentep = 50
default maxep = 50
default game_time = 3600 #60 Minuten Spielzeit

default inventory = []
default selected_item = None

init python:
    #Funktion, um die Energie zu regeln
    def LooseEnergy(energy):
        store.currentep -= energy
        if store.currentep <= 0:
            store.currentep = 0
            renpy.jump("BadEnding")
        return

    #Funktion, um das Datenvolumen zu regeln
    def LooseData(data):
        store.currentdp -= data
        if store.currentdp <= 0:
            store.currentdp = 0
            renpy.jump("BadEnding")
        return

    def HideCurrentScreens(currentScreensList):
        for item in currentScreensList:
            renpy.hide_screen(item)

    def ShowScreen(item):
        currentScreensList.append(item)
        renpy.show_screen(item)

    def HideScreen(item):
        try:
            currentScreensList.remove(item)
        except ValueError:
            pass
        renpy.hide_screen(item)

label start:
    jump GameLoop
    return
