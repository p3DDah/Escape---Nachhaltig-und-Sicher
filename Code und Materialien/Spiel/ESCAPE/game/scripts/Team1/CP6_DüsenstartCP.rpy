label chapter6_Duesenstart:
    $ InventarCheck_state = False
    $ HinweisCheck_state = True
    $ current_label = "chapter6_Duesenstart"
    $ HideScreen("BackButton")
    $ HideScreen("keyboardNormal")
    $ ShowScreen("keyboardDummy")
    $ HideScreen("App_Duesenstart")
    #Konsequenzen aus voheriger Aufgabe in chapter_3.rpy
    if encryptionChecker == False:
        "Du hast deine Daten nicht ordnungsgemäß verschlüsselt,
        sodass Aliens unsere Nachrichten abhören und auf unsere Systeme zugreifen konnten."
        "Dadurch ist der Strom und Datenverbrauch enorm gestiegen!"
        $ LooseEnergy(40)
        $ LooseData(30)
    $ ShowScreen("Sicherheitsprotokoll")
    #Anzeige der einzelnen Fragen
    if Frage1_state:
        call Frage1 from _call_Frage1
    if Frage2_state:
        call Frage2 from _call_Frage2
    if Frage3_state:
        call Frage3 from _call_Frage3
    if Frage4_state:
        call Frage4 from _call_Frage4
    if Frage5_state:
        call Frage5 from _call_Frage5
    if Frage6_state:
        call Frage6 from _call_Frage6
    if Frage7_state:
        call Frage7 from _call_Frage7
    if Frage8_state:
        call Frage8 from _call_Frage8
    if Frage9_state:
        call Frage9 from _call_Frage9
    if Frage10_state:
        call Frage10 from _call_Frage10
    $ current_label = ""
    $ current_hinweis = ""
    $title = ""
    $ HideScreen("Sicherheitsprotokoll")
    $ HideScreen("keyboardDummy")
    $ ShowScreen("os_title")
    $ password = 1423 * year * month * day /10
    $os_title = "[password]"
    call chapter_7_pw_uebermitteln from _call_chapter_7_pw_uebermitteln
    $ HideScreen("os_title")
    call chapter_7_pw_eingeben from _call_chapter_7_pw_eingeben
    #dient zur Überprüfung, ob die Mindestressourcen eingehalten worden sind
    call CheckRessourcen from _call_CheckRessourcen
    scene KapselFalling
    pause 4.0
    #Entscheidung, welches Ende gewählt wird
    if WinGame:
        jump GoodEnding
    else:
        commander "Oh nein, wir haben zu viel Ressourcen verbraucht! Das ist unser Ende ..."
        jump BadEnding

    $ renpy.pause(hard=True)

#beantworte so lange die Fragen, bis sie richtig sind
label Frage1:
    $ current_hinweis = "CP_Frage1"
    $title = "Frage 1\nWelches Betriebssystem ist datensparsam?"
    menu:
        "Windows":
            commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
            call Frage1 from _call_Frage1_1
        "Linux":
            commander "Sehr gut, Linux ist bekannt für seine Datensparsamkeit!"
        "iOS":
            commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
            call Frage1 from _call_Frage1_2
    $ Frage1_state = False
    return

label Frage2:
    $ current_hinweis = "CP_Frage2"
    $title = "Frage 2\nWas sollte bei einem Browser entfernt werden?"
    $AntwortFrage2 = renpy.input("Gib deine Antwort ein.")
    if AntwortFrage2.lower() != "sslkeylogfile":
        commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
        call Frage2 from _call_Frage2_1
    else:
        commander "Prima, das SSLKEYLOGFILE kann dazu benutzt werden, den Datenverkehr zu entschlüsseln. Das
        sollte um allen Preis vermieden werden."
    $ Frage2_state = False
    return

label Frage3:
    $ current_hinweis = "CP_Frage3"
    $title = "Frage 3\nWomit kann man Videos datensparsam anschauen?"
    $AntwortFrage3 = renpy.input("Gib deine Antwort ein.")
    if AntwortFrage3.lower() != "proxy":
        commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
        call Frage3 from _call_Frage3_1
    $ Frage3_state = False
    return

label Frage4:
    $ current_hinweis = "CP_Frage4"
    $title = "Frage 4\nWie lautet eine gängige Verschlüsselung beim Internetsurfen?"
    $AntwortFrage4 = renpy.input("Gib deine Antwort ein.")
    if AntwortFrage4.lower() != "https":
        commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
        call Frage4 from _call_Frage4_1
    $ Frage4_state = False
    return

label Frage5:
    $ current_hinweis = ""
    $title = "Frage 5\nIst HTTP für Verschlüsselung geeignet?"
    menu:
        "Ja":
            commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
            call Frage5 from _call_Frage5_1
        "Nein":
            commander "Richtig"
    $ Frage5_state = False
    return

label Frage6:
    $ current_hinweis = ""
    $title = "Frage 6\nWie viele Zeichen sollte ein Passwort mindestens haben?"
    menu:
        "1":
            commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
            call Frage6 from _call_Frage6_1
        "16":
            commander "Sehr gut. Für ein sicheres (Sonderzeichen, Ziffern, Groß- und
            Kleinbuchstaben enthalten sowie kein persönlicher Zusammenhang), 16 Zeichen langes Passwort würde ein
            herkömmlicher PC laut \"checkdeinpasswort.de\" über 100 Billionen Jahre benötigen, dieses zu knacken."
            commander "Klar wäre ein 42 Zeichen langes Passwort besser, nur wer kann sich solch ein Passwort ohne Passwortmanager merken?"
        "42":
            commander "Auch wenn 42 die Antwort auf alle Fragen ist, so ist sie hier doch leider falsch. Bitte denke noch einmal nach."
            call Frage6 from _call_Frage6_2
    $ Frage6_state = False
    return

label Frage7:
    $ current_hinweis = ""
    $title = "Frage 7\nWie oft sollte man ein Passwort wiederverwenden?"
    menu:
        "Einmal":
            commander "Sehr gut. Passwörter sollten nicht wiederverwendet werden, da sonst alle deine Daten mit nur einem Passwort zugänglich sind."
        "Beliebig oft":
            commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
            call Frage7 from _call_Frage7_1
        "Egal":
            commander "Das sollte dir nicht egal sein. Bitte denke noch einmal nach."
            call Frage7 from _call_Frage7_2
    $ Frage7_state = False
    return

label Frage8:
    $ current_hinweis = ""
    $title = "Frage 8\nWelche sozialen Netzwerke sollte man besser vermeiden?"
    menu:
        "Whatsapp":
            $AntwortFrage8 = "Whatsapp"
            call Frage8 from _call_Frage8_1
        "Facebook":
            $AntwortFrage8 = "Facebook"
            call Frage8 from _call_Frage8_2
        "Twitter":
            $AntwortFrage8 = "Twitter"
            call Frage8 from _call_Frage8_3
        "Alle":
            commander "Korrekt, alle Dienste sammeln Daten von dir und verkaufen diese wiederum an Drittanbieter."
    $ Frage8_state = False
    return

label Frage9:
    $ current_hinweis = ""
    $title = "Frage 9\nWelche Suchmaschine ist datensparsam?"
    menu:
        "Lite.qwant.com":
            commander "Sehr gut. Schaue es dir doch einmal bei Gelegenheit an!"
        "Google.com":
            commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
            call Frage9 from _call_Frage9_1
        "Yahoo.com":
            commander "Die Antwort ist leider nicht korrekt. Bitte denke noch einmal nach."
            call Frage9 from _call_Frage9_2
        "DuckDuckGo.com":
            commander "Prima. Schaue es dir doch einmal bei Gelegenheit an!"
    $ Frage9_state = False
    return

label Frage10:
    $ current_hinweis = ""
    $title = "Frage 10\nFindest du, dass du nun ein besseres Gespür für mehr Sicherheit\nund Nachhaltigkeit aufbauen konntest?"
    menu:
        "Ja":
            $AntwortFrage10 = "Ja"
            commander "Sehr schön! Zum Auffrischen des Gelernten lese dir noch einmal den
            Kompass der digitalen Selbstverteidgung durch oder spiele erneut das Escape-Spiel."
        "Nein":
            $AntwortFrage10 = "Nein"
            commander "Schade, lese dir unbedingt noch einmal den Kompass der digitalen Selbstverteidgung durch und
            versuche dann erneut das Spiel."
    $ Frage10_state = False
    return

label CheckRessourcen:
    #min 90 Strom und 90 Datenvolumen nötig, um zu gewinnen
    if currentep >= 90 and currentdp >= 90:
        $WinGame = True
    else:
        $WinGame = False
    return

label chapter_7_pw_uebermitteln:
    "Übermittle das Passwort für den Fragebogen an den Maschinenraum."
    menu:
        "Hast du das Passwort übermittelt?"
        "Ja":
            $ HideScreen("os_title")
        "Nein":
            call chapter_7_pw_uebermitteln from _call_chapter_7_pw_uebermitteln_1
    return

label chapter_7_pw_eingeben:
    "Zum Abgleich der Startsequenz muss das Passwort aus dem Maschinenraum eingegeben werden."
    python:
        try:
            mr_pw = int(renpy.input("Schlüssel eingeben"))
        except:
            fail = True
    if fail:
        $ fail = False
        "Bitte nur Zahlen eingeben!"
        jump kursberechnungPasswort_label
    $mr_pw = mr_pw*10/(year*month*day)
    if mr_pw == "3214":
        $renpy.notify("Startsequenz freigegeben")
        return
    else:
        jump chapter_7_ErrorCountdown
    return

label chapter_7_ErrorCountdown:
    $renpy.notify("Falscher Schlüssel")
    $ set_time = 10
    $ countdown_title ="Bitte warten..."
    $ timer_jump = "chapter_7_pw_eingeben"
    show screen countdown
    $ renpy.pause(hard=True)
