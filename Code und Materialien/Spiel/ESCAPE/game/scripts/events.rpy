#start of the game

label GameLoop:
    #constant background music
    play music "audio/cockpit.mp3" fadeout 1.0 fadein 1.0
    scene space_1
    #intro text
    "Der Weltraum, unendliche Weiten. Wir schreiben das Jahr 3196."
    "Du befindest dich in einer Raumstation. Ihr seid auf dem Weg zur Erde."
    "Doch was ist das?"
    scene space_2
    pause 1.0
    scene space_3
    #just a short, not constant sound
    play sound "explosion.mp3"
    play music "audio/background (10).mp3" fadeout 1.0 fadein 1.0
    pause 1.0
    #just a short, not constant sound
    play sound "alarm.mp3"
    scene space_4
    commander "Mission Control, können Sie mich hören?"
    control "Mission Control hört."
    commander "Wir senden vom Cockpit des Raumschiffes NCC-1701-D. Hier gibt es ein gravierendes Problem!"
    control "Was ist passiert?"
    commander "Ein Asteroid hat unser Raumschiff getroffen! Alle Systeme sind ausgefallen! Der Zusammenstoß hat unseren Kurs zur Erde verändert!"
    commander "Es besteht keine Kontrolle mehr über das Schiff!"
    commander "Ebenso wurden einige Teile der NCC-1701-D stark beschädigt, sodass kein Kontakt mehr zum Maschinenraum existiert! Ein Zugang dorthin ist unmöglich! Wir benötigen dringend Hilfe!"
    control "Mission Control hat verstanden. Eine externe Steuerung des Schiffes ist nicht möglich!"
    control "Aber es gibt einen Weg, dass Sie wieder auf den richtigen Kurs gelangen."
    control "Sie müssen dazu ..."
    "skrrrrzzzzzzzz skrrrrzzzzzzzz skrrrrzzzzzzzz"
    commander "Mist, der Empfang zur Mission Control ist abgebrochen."
    commander "Nun müssen wir es wohl alleine angehen!"
    "Gib deinem Astronauten-Team einen Namen!"
    #name input
    $ spieler = renpy.input("Wie lautet der Name?")
    commander "Auf gehts! Zurück zur Erde, Team [spieler]!"
    menu:
        "Bist du startklar?"
        "Ja":
            jump choose_team
        "Nein":
            jump BadEnding

label choose_team:
    #init variables
    call Variables from _call_Variables
    "Wichtige Spielehinweise!"
    "Bevor du mit dem Spielen beginnst, lies dir bitte die Spielehinweise.pdf durch."
    "Alle benötigten Materialien für den jeweiligen Raum findest du in dem gleichnamigen Ordner."
    "Das Spiel dient zum Erlernen und Verbessern des Nachhaltigkeitsempfindens. Ebenso werden wichtige Sicherheitsaspekte vermittelt."
    "\"Escape\" beruht auf dem Kompass der digitalen Selbstverteidigung (Kompass-Digitalisierung.pdf).
    Bitte lese dir diesen aufmerksam durch, um alle Aufgaben absolvieren zu können."
    "Insgesamt besitzt du für das Spiel 3 Hinweise, wähle sie also weise!"
    "Wenn du deinen Raum gewählt hast, dann startet der Countdown."
    "Klicke bitte {b}gleichzeitig{/b} mit deinem/r Spielpartner/in auf je einen Raum, sodass der Countdown synchron ablaufen kann!"
    menu:
        "Bist du bereit zu Spielen?"
        "Bereit!":
            pass
        "Hinweise wiederholen!":
            jump choose_team
    $ music_pieces = ["audio/cockpit.mp3",
    "audio/background (3).mp3",
    "audio/background (4).mp3",
    "audio/background (6).mp3",
    "audio/background (7).mp3",
    "audio/background (9).mp3",
    "audio/background (10).mp3",
    "audio/background (11).mp3",
    "audio/background (13).mp3",
    "audio/background (14).mp3",
    "audio/background (15).mp3",
    "audio/background (16).mp3",
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15)),
    "<silence {0}>".format(renpy.random.randint(10,15))
    ]

    python:
        sound_pieces = ["audio/sounds (1).mp3",
        "audio/sounds (2).mp3",
        "audio/sounds (3).mp3",
        "audio/sounds (4).mp3",
        "audio/sounds (5).mp3",
        "audio/sounds (6).mp3",
        "audio/sounds (7).mp3",
        "audio/sounds (8).mp3",
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15)),
        "<silence {0}>".format(renpy.random.randint(10,15))
        ]

    $ renpy.random.shuffle(music_pieces)
    $ renpy.random.shuffle(sound_pieces)

    menu:
        "Wähle deinen Raum. \n Mindestens ein Spieler pro Raum ist erforderlich!"
        "Cockpit":
            play music music_pieces fadeout 3.0 fadein 3.0
            play audio sound_pieces loop fadeout .5 fadein .5 volume .3
            $ ShowScreen("game_countdown")
            #jump to Eingangstür.rpy in folder Team1
            jump start_team_1
        "Maschinenraum":
            play music music_pieces fadeout 2.0 fadein 2.0
            play audio sound_pieces loop fadeout .5 fadein .5 volume .3
            $ ShowScreen("game_countdown")
            #jump to CP1_Notstrom.rpy in folder Team2
            jump start_team_2
        "Hinweise wiederholen!":
            #jump to label BadEnding -> end game
            jump choose_team
    return

label Variables:
    #init variables
    $ currentep = 50
    $ maxep = 50
    $ currentdp = 100
    $ maxdp = 100
    $ tookKeycard = False
    $ doorLocked = True
    $ game_running = True
    return

label GoodEnding:
    $ game_running = False
    $ HideScreen("monitorBroken")
    call HideObejects from _call_HideObejectsGoodEnd
    call HideMRoomObejcts from _call_HideMRoomObejctsGood
    #Endscreen good zeigen
    scene EndGood Animated
    commander "Herzlich Willkommen zurück auf der Erde. Wir haben es geschafft! Bald werden wir gerettet!"
    $renpy.pause(hard=True)

label BadEnding:
    $ game_running = False
    $ HideCurrentScreens(currentScreensList)
    $ HideScreen("monitorBroken")
    $ HideScreen("computerWand")
    call HideObejects from _call_HideObejectsBadEnd
    call HideMRoomObejcts from _call_HideMRoomObejctsBad
    #Endscreen bad zeigen
    scene EndBad Animated
    pause 5.0
    jump gameover
    $renpy.pause(hard=True)

label gameover:
    $ game_running = False
    $ HideScreen("monitorBroken")
    call HideObejects from _call_HideObejectsGameOver
    call HideMRoomObejcts from _call_HideMRoomObejctsGO
    $ HideCurrentScreens(currentScreensList)
    scene space_1
    show screen game_over
    play sound "audio/game_over.mp3"

    $renpy.pause(hard=True)

label OpenInventory:
    #definded in game_screens.rpy
    $ HideScreen("inventory_button")
    $ ShowScreen("inventory_screen")
    $renpy.pause(hard=True)

label CloseInventory:
    $ ShowScreen("inventory_button")
    $ HideScreen("inventory_screen")
    $renpy.pause(hard=True)
