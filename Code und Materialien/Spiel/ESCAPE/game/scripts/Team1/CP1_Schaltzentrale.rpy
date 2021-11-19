label chapter1_Schaltzentrale:
    #label to unlock door pinpad
    label lockerDoorPinpadClicked: #look at team_1_screens.rpy at lockerDoorPinpad()
        #Variable, sodass der Countdown nicht übersprungen werden kann
        $ HinweisCheck_state = False
        if mussWarten:
            $ renpy.notify("Bitte warten")
        else:
            $ HinweisCheck_state = True
            $ current_label = "lockerDoorPinpadClicked"
            $ current_hinweis = "CP1_lockerDoorPinpadClicked_Hinweis"
            $ renpy.notify("Verschlossen!")
            $ pin = renpy.input("6-stellige PIN eingeben")
            #fixed password 130578 -> birthday of door cabinet manager
            if pin == "130578":
                $ renpy.notify("PIN korrekt")
                $ HinweisCheck_state = False
                $ current_label = ""
                $ current_hinweis = ""
                #Überprüfe, ob die Monitore schon aus dem Schrank entnommen worden sind
                if CP2_LockerdoorEmpty_state:
                    $ ShowScreen("lockerDoorOpenEmpty")
                else:
                    $ ShowScreen("lockerDoorOpen")
                    commander "Ein Klassiker! Ich würde {b}nie{/b} persönliche Daten in eines meiner Passwörter integrieren!"
                $ HideScreen("lockerDoorPinpad")
                #Überprüfe, ob Schrank offen oder geschlossen ist
                $ Lockerdoor_state = True
                window hide
                $ renpy.pause(hard=True)
            else:
                $ renpy.notify("Falsche PIN")
                $ mussWarten = True
                #Bestrafungstimer von 10s, um einfaches Durchprobieren zu vermeiden
                $ set_time = 10
                #Wie der Titel des Countdowns heißen soll
                $ countdown_title ="Bitte warten..."
                #springe zum Label PinFalschEnde
                $ timer_jump = "PinFalschEnde"
                window hide
                #zeige den Countdwon an
                show screen countdown
                $ renpy.pause(hard=True)
        $ renpy.pause(hard=True)

#Label für den Countdown
label PinFalschEnde:
    $ mussWarten = False
    jump lockerDoorPinpadClicked
    return

    #label to unlock the broken monitor
    label brokenMonitorClicked:
        $ HinweisCheck_state = False
        $ InventarCheck_state = False   #Variable, um das Inventar zu deaktivieren,
                                        #sodass ein ungewolltes Verschwinden von Menüs vermieden werden kann
        #Abfrage, ob die Monitore aus dem Schrank genommen wurden
        if foundMonitors:
            menu:
                "Monitor reparieren"
                "Farbbild-Monitor":
                    $ LooseEnergy(20) #Funktion um 20 Einheiten Strom abzuziehen
                    $ ShowScreen("monitorColor") #zeige Farbbildschirm an (zu finden bei team_1_screens.rpy)
                    $ MonitorColor_state = True #State-Variable, sodass Farbmonitor ausgewählt wurde
                    $ inventory.remove(monitor_color) #Funktion, um den Farbbildschirm aus dem Inventar zu entfernen
                    commander "Ein Farbbildschirm? Ein Monochrombildschirm wäre eindeutig sparsamer gewesen!"
                "Schwarz-Weiß-Monitor":
                    $ LooseEnergy(10)
                    $ ShowScreen("monitorSW")
                    $ MonitorBW_state = True
                    $ inventory.remove(monitor_sw)
                    commander "Gute Wahl! Auch in Schwarz-Weiß werden wir alles erkennen können und sparen dabei noch Strom!"
            $ renpy.notify("Monitor repariert")
            $ InventarCheck_state = True #Variable, um das Inventar wieder zu aktivieren
            $ HideScreen("monitorBroken") #Verstecke den kaputten Monitor
        else:
            $ renpy.notify("Defekt")
        window hide
        $ renpy.pause(hard=True)

    label MonitorsFound:
        $ShowScreen("lockerDoorPinpad")
        $HinweisCheck_state = True
        $Lockerdoor_state = False
        #Abfrage, sodass die Monitore nur einmal ausgewählt werden können
        if not CP2_LockerdoorEmpty_state:
            $foundMonitors = True
            $inventory.append(monitor_sw)
            $inventory.append(monitor_color)
            $CP2_LockerdoorEmpty_state = True
        $renpy.pause(hard=True)
