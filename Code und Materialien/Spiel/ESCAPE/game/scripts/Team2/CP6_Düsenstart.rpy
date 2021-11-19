label startDuesen:
    $ current_label = ""
    $ current_hinweis = ""
    $ ImageButtonActivate_state = False
    $renpy.notify("Tür ist verschlossen")
    $ startDuesenDoorPasswort = ""
    $ InventarCheck_state = False

    label startDuesenDoorPasswort_label:
        $ HinweisCheck_state = True
        $ current_label = "startDuesenDoorPasswort_label"
        python:
            try:
                startDuesenDoorPasswort = int(renpy.input("Bitte geben Sie das Passwort aus dem Cockpit ein"))
            except:
                fail = True
        if fail:
            $ fail = False
            "Bitte nur Zahlen eingeben!"
            jump startDuesenDoorPasswort_label

        $ startDuesenDoorPasswort = startDuesenDoorPasswort*10/(year*month*day)

        if startDuesenDoorPasswort != "2134":
            menu:
                "Erneut versuchen":
                    jump startDuesenDoorPasswort_label
                "Zurück":
                    window hide
                    $ renpy.pause(hard=True)
        else:
            pass

    $ HideScreen("endDoor_mr")
    $ ShowScreen("Sicherheitsprotokoll")
    if Frage1_state:
        call MR_Frage1 from _call_MR_Frage1
    if Frage2_state:
        call MR_Frage2 from _call_MR_Frage2
    if Frage3_state:
        call MR_Frage3 from _call_MR_Frage3
    if Frage4_state:
        call MR_Frage4 from _call_MR_Frage4
    if Frage5_state:
        call MR_Frage5 from _call_MR_Frage5
    if Frage6_state:
        call MR_Frage6 from _call_MR_Frage6
    if Frage7_state:
        call MR_Frage7 from _call_MR_Frage7
    if Frage8_state:
        call MR_Frage8 from _call_MR_Frage8
    if Frage9_state:
        call MR_Frage9 from _call_MR_Frage9
    if Frage10_state:
        call MR_Frage10 from _call_MR_Frage10
    $ current_label = ""
    $ current_hinweis = ""
    $title = ""
    $ HideScreen("Sicherheitsprotokoll")
    call MR_CheckAntworten from _call_MR_CheckAntworten
    $ HinweisCheck_state = False
    label MR_allesRichtig:
    "Alle Fragen wurden richtig beantwortet!"
    "Notiere und übermittle den Schlüssel an das Cockpit"
    $ ShowScreen("os_title")
    $ password = 3214 * year * month * day /10
    $os_title = "[password]"
    call startDuesen_pw_uebermitteln from _call_startDuesen_pw_uebermitteln
    $ HideScreen("os_title")
    call startDuesen_pw_eingeben from _call_startDuesen_pw_eingeben
    commander "Wir haben alles geschafft! Hoffentlich reichen unsere Ressourcen noch für die Landung aus!"
    $ HideScreen("computerWand")
    scene KapselFalling
    pause 4.0
    #Strom min 80 und Datenvolumen min 80, um zu gewinnen
    if currentep >= 80 and currentdp >= 80:
        jump GoodEnding
    else:
        commander "Ohhhhh nein, wir werden es nicht schaffen! Es war schön euch kennengelernt zu haben!"
        jump BadEnding
    $ renpy.pause(hard=True)

label MR_Frage1:
    $ current_hinweis = "MRFrage1"
    $title = "Frage 1\nWie sollten Apps konfiguriert werden? (12)"
    $AntwortMR_Frage1 = renpy.input("Gib deine Antwort ein.")
    return

label MR_Frage2:
    $ current_hinweis = "MRFrage2"
    $title = "Frage 2\nWelche Apps werden bevorzugt? (6)"
    $AntwortMR_Frage2 = renpy.input("Gib deine Antwort ein.")
    return

label MR_Frage3:
    $ current_hinweis = "MRFrage3"
    $title = "Frage 3\nNenne eine deutsche, datensparsame Suchmaschine! (7)"
    $AntwortMR_Frage3 = renpy.input("Gib deine Antwort ein.")
    return

label MR_Frage4:
    $ current_hinweis = "MRFrage4"
    $title = "Frage 4\nWelchen Messenger sollte man vermeiden? (8)"
    $AntwortMR_Frage4 = renpy.input("Gib deine Antwort ein.")
    return

label MR_Frage5:
    $ current_hinweis = "MRFrage5"
    $title = "Frage 5\nZu was dienen Firewalls? (9)"
    $AntwortMR_Frage5 = renpy.input("Gib deine Antwort ein.")
    return

label MR_Frage6:
    $ current_hinweis = "MRFrage6"
    $title = "Frage 6\nVor was wird man durch Intrusion Prevention Systeme geschützt? (9)"
    $AntwortMR_Frage6 = renpy.input("Gib deine Antwort ein.")
    return

label MR_Frage7:
    $ current_hinweis = "MRFrage7"
    $title = "Frage 7\nNicht benötigte Zugriffe einer App sollten ... werden! (9)"
    $AntwortMR_Frage7 = renpy.input("Gib deine Antwort ein.")
    return

label MR_Frage8:
    $ current_hinweis = "MRFrage8"
    $title = "Frage 8\nNenne einen datensparsamen Messenger! (6)"
    $AntwortMR_Frage8 = renpy.input("Gib deine Antwort ein.")
    return

label MR_Frage9:
    $ current_hinweis = "MRFrage9"
    $title = "Frage 9\nWelche Konsequenzen können sich durch die unkontrollierte Datenpreisgebung ergeben? (13)"
    $AntwortMR_Frage9 = renpy.input("Gib deine Antwort ein.")
    return

label MR_Frage10:
    $ current_hinweis = ""
    $title = "Frage 10\nFindest du, dass du nun ein besseres Gespür für mehr Sicherheit\nund Nachhaltigkeit aufbauen konntest?"
    menu:
        "Ja":
            $AntwortMR_Frage10 = "Ja"
        "Nein":
            $AntwortMR_Frage10 = "Nein"
    return

label MR_CheckAntworten:
    $ MR_CheckFragen = True
    if AntwortMR_Frage1.lower() == "datensparsam":
        $ Frage1_state = False
        "1. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "1. Frage falsch"

    if AntwortMR_Frage2.lower() == "lokale":
        $ Frage2_state = False
        "2. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "2. Frage falsch"

    if AntwortMR_Frage3.lower() == "metager":
        $ Frage3_state = False
        "3. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "3. Frage falsch"

    if AntwortMR_Frage4.lower() == "whatsapp":
        $ Frage4_state = False
        "4. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "4. Frage falsch"

    if AntwortMR_Frage5.lower() == "filterung":
        $ Frage5_state = False
        "5. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "5. Frage falsch"

    if AntwortMR_Frage6.lower() == "schadcode":
        $ Frage6_state = False
        "6. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "6. Frage falsch"

    if AntwortMR_Frage7.lower() == "blockiert":
        $ Frage7_state = False
        "7. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "7. Frage falsch"

    if AntwortMR_Frage8.lower() == "signal":
        $ Frage8_state = False
        "8. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "8. Frage falsch"

    if AntwortMR_Frage9.lower() == "profilbildung":
        $ Frage9_state = False
        "9. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "9. Frage falsch"

    if AntwortMR_Frage10.lower() == "ja":
        $ Frage10_state = False
        "10. Frage richtig"
    else:
        $ MR_CheckFragen = False
        "10. Frage falsch"

    if MR_CheckFragen:
        jump MR_allesRichtig
    else:
        jump startDuesen_ErrorCountdown_Fragen

label startDuesen_pw_uebermitteln:
    "Übermittle das Passwort für den Fragebogen an das Cockpit."
    menu:
        "Hast du das Passwort übermittelt?"
        "Ja":
            $ HideScreen("os_title")
        "Nein":
            call startDuesen_pw_uebermitteln from _call_startDuesen_pw_uebermitteln_1
    return

label startDuesen_pw_eingeben:
    "Zum Abgleich der Startsequenz muss das Passwort aus dem Cockpit eingegeben werden."
    python:
        try:
            cockpit_pw = int(renpy.input("Schlüssel eingeben"))
        except:
            fail = True
    if fail:
        $ fail = False
        "Bitte nur Zahlen eingeben!"
        jump kursberechnungPasswort_label
    $ cockpit_pw = cockpit_pw *10 / (year*month*day)
    if cockpit_pw == "1423":#"Tyz36Scx":
        $renpy.notify("Startsequenz freigegeben")
        return
    else:
        jump startDuesen_ErrorCountdown
    return

label startDuesen_ErrorCountdown_Fragen:
    $renpy.notify("Nicht alle Fragen richtig")
    $ set_time = 10
    $ countdown_title ="Bitte warten..."
    $ timer_jump = "startDuesen"
    show screen countdown
    $ renpy.pause(hard=True)

label startDuesen_ErrorCountdown:
    $renpy.notify("Falscher Schlüssel")
    $ set_time = 10
    $ countdown_title ="Bitte warten..."
    $ timer_jump = "startDuesen_pw_eingeben"
    show screen countdown
    $ renpy.pause(hard=True)
