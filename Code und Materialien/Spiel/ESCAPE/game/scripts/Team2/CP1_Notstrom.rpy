label start_team_2:
    #initalisiere Variablen
    call InitMRoomVars from _call_InitMRoomVars
    #wähle Hintergrundbild
    scene door_machineroom
    #zeige bestimmte Objekte an
    $ ShowScreen("bars")
    $ ShowScreen("inventory_button")
    $ ShowScreen("Hinweis_button")
    $ ShowScreen("machineroomKeycard")
    $ ShowScreen("machineRoomPinpad")
    $ ShowScreen("gotoMachineRoomDoor")
    $ renpy.pause(hard=True)

label InitMRoomVars:
    #Strom 200 Einheiten
    $ currentep = 200
    $ maxep = 200
    #Datenvolumen 200 Einheiten
    $ currentdp = 200
    $ maxdp = 200
    return

label InitMRoomObejcts:
    $ ShowScreen("Figur_Hildegart")
    $ ShowScreen("Figur_Detlef")
    $ ShowScreen("Figur_Dobby")
    $ ShowScreen("Figur_Gudrun")
    $ ShowScreen("Figur_Ludwig")
    $ ShowScreen("Whiteboard")
    $ ShowScreen("Tresor")
    return

label HideMRoomObejcts:
    $ HideScreen("Figur_Hildegart")
    $ HideScreen("Figur_Detlef")
    $ HideScreen("Figur_Dobby")
    $ HideScreen("Figur_Gudrun")
    $ HideScreen("Figur_Ludwig")
    $ HideScreen("Whiteboard")
    $ HideScreen("Tresor")
    $ HideScreen("computerWand")
    return

#Startsequnze zum Öffnen der Tür
label machineRoomDoorClicked:
    if doorLocked == True:
        #temporärer Sound
        play sound "audio/door_denied.mp3"
        "Verschlossen"
    else:
        play sound "audio/door_open.mp3"
        pause 3.0
        jump machine_room
    window hide
    $ renpy.pause(hard=True)

label machineRoomPinpadClicked:
    if tookKeycard == False:
        play sound "audio/door_denied.mp3"
        "Schlüsselkarte benötigt"
    else:
        $ doorLocked = False
        play sound "audio/code_accept.mp3"
        "Zugang gewährt"
    window hide
    $ renpy.pause(hard=True)

default tookWA40 = False
default tookWA80 = False
default chooseWA40 = False
default isResistorInserted = False
default finishWebBrowser = False
default finishSystemcheck = False
default finishKursberechnung = False
default finishReparieren = False

#Hauptszene Maschienraum
label machine_room:
    $ HinweisCheck_state = True
    $ current_label = ""
    $ current_hinweis = ""
    $ InventarCheck_state = True
    scene machine_room
    $ HideScreen("gotoMachineRoomDoor")
    $ HideScreen("machineRoomPinpad")
    $ ShowScreen("sicherung_40A")
    $ ShowScreen("sicherung_80A")
    $ ShowScreen("generatorCover")
    call InitMRoomObejcts from _call_InitMRoomObejectsStart
    #initialisiere Bild
    image enterprise = Image("Objekte/Maschinenraum/EnterprisePoster_per.png", xalign=0.09, yalign=0.38)
    show enterprise
    $ renpy.notify("Maschinenraum")
    window hide
    $ renpy.pause(hard=True)

#Generator
label generatorCoverClicked:
    $ ImageButtonActivate_state = False
    #wenn 40A oder 80A Sicherung aufgehoben, dann verfügbar
    $ HinweisCheck_state = False
    $ InventarCheck_state = False
    if tookWA40 or tookWA80:
        $ isResistorInserted = True
        menu:
            commander "Setze bitte die Sicherung in den Generator ein. Schaue im Inventar nach deren eigenschaften nach!"
            "Sicherung 40A" if tookWA40:
                $ LooseEnergy(10)
                $ chooseWA40 = True #Aktion wird ausgeführt in CP3_Systemcheck.rpy
                commander "Puhh, hoffentlich hält die Sicherung!"
            "Sicherung 80A" if tookWA80:
                $ LooseEnergy(20)
                commander "Gut gemacht! Die Sicherung sollte uns keine Probleme bereiten, sie benötigt nur etwas mehr Strom."
            "Zurück":
                $ HinweisCheck_state = True
                $ current_label = ""
                $ current_hinweis = ""
                $ InventarCheck_state = True
                $ ImageButtonActivate_state = True
                window hide
                $ renpy.pause(hard=True)
        $ HideScreen("generatorCover")
        $ HideScreen("sicherung_80A")
        $ HideScreen("sicherung_40A")
        label Generatorpasswort:
            $ ImageButtonActivate_state = False
            $ HinweisCheck_state = True
            $ InventarCheck_state = False
            $ current_label = "Generatorpasswort"
            $ current_hinweis = "CP1_Generatorpasswort_Hinweis"
            $ zahnradPasswort = ''
            commander "Um nun den Strom wieder einzuschalten, benötigen wir ein Passwort! Schau dir doch einmal die Zahnräder auf den Generator an."
            #festes Passwort '54321', findet sich im Zahnradrätsel (analog)
            while zahnradPasswort != '54321':
                $ zahnradPasswort = renpy.input("Wie lautet das Zugangspasswort")
                if zahnradPasswort != '54321':
                    "Es scheint nicht richtig zu sein."
            $ current_label = ""
            $ current_hinweis = ""
            commander "Sehr gut! Der Strom ist nun wieder vollständig eingeschaltet."
            commander "Aber mal im Ernst, das Passwort ist nicht wirklich sicher!"
            $ password = 1234*year*month*day/10
            "Übermittle folgendes Passwort zum Cockpit: \"[password]\""
            #Funktion zur Abfrage, ob Passwort übermittelt wurde
            call machine_pw_uebermitteln from _call_machine_pw_uebermitteln
            $ HinweisCheck_state = True
            $ current_label = ""
            $ current_hinweis = ""
            $ InventarCheck_state = True
            $ ImageButtonActivate_state = True
            window hide
            $ ShowScreen("computerWand")
    else:
        $ renpy.notify("Das passende Teil fehlt!")
    $ ImageButtonActivate_state = True
    window hide
    $ renpy.pause(hard=True)

#Standard-Label zum Anzeigen der Aufgaben
label computerWandClicked:
    $ ImageButtonActivate_state = False
    $ renpy.notify("MaschinenRaumOS")
    menu appChoice:
        "Welche Software soll gestartet werden?"
        #Kursberechnung wurde noch nicht abgeschlossen
        "Kursberechnung" if not finishKursberechnung:
            $renpy.notify("Kursberechnung gestartet")
            #wechsel zu CP4_Kurskorrektur.rpy
            jump computerWandClicked_Kursberechnung

        #Raumschiffinformationen wurden nicht beschafft
        "Web-Browser" if not finishWebBrowser:
            $renpy.notify("Browser gestartet")
            #wechsel zu CP2_Infobeschaffung.rpy
            jump computerWandClicked_Browser

        #Systemcheck wurde noch nicht abgeschlossen
        "Systemcheck" if not finishSystemcheck:
            $renpy.notify("Systemcheck gestartet")
            #wechsel zu CP3_Systemcheck.rpy
            jump computerWandClicked_Systemcheck

        #Reparatur und Systemcheck wurden noch nicht abgeschlossen
        "Komponentenreparatur" if not finishReparieren and finishSystemcheck:
            $renpy.notify("Reparieren gestartet")
            #wechsel zu CP5_Reparatur_Antrieb
            jump computerWandClicked_Reparieren

        "Zurück":
            $ ImageButtonActivate_state = True
            window hide
            $ renpy.pause(hard=True)

    window hide
    $ renpy.pause(hard=True)

label machine_pw_uebermitteln:
    menu:
        "Hast du das Passwort \"[password]\" notiert/übermittelt?"
        "Ja":
            pass
        "Nein":
            call machine_pw_uebermitteln from _call_machine_pw_uebermitteln_1
    return

#Blende Tür zur letzten Aufgabe CP6 ein
label lastScene:
    $ ShowScreen("endDoor_mr")

    window hide
    $ renpy.pause(hard=True)
