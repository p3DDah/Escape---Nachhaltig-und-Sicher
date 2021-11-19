#Zusatzaufgabe Tresor

label Tresor:
    $ ImageButtonActivate_state = False
    if not EX_Tresor_state:
        $ HinweisCheck_state = True
        $ current_label = "Tresor"
        $ current_hinweis = "EX_Tresor_Hinweis"
        commander "Scheint als benötigen wir hierfür ein 4-stelliges Passwort!"
        $ tmp_passwort = ""
        while tmp_passwort != "1392":
            $ tmp_passwort = renpy.input("Wie lautet der Code?")
            if tmp_passwort != "1392":
                $ renpy.notify("Falsches Passwort!")
                menu:
                    "Zurück zum Maschinenraum?"
                    "Ja":
                        $ HinweisCheck_state = False
                        $ current_label = ""
                        $ current_hinweis = ""
                        $ ImageButtonActivate_state = True
                        window hide
                        $ renpy.pause(hard=True)
                    "Nein":
                        pass
        $ HinweisCheck_state = False
        $ current_label = ""
        $ current_hinweis = ""
        $ EX_Tresor_state = True
        $ renpy.notify("Passwort korrekt!")
        commander "Sehr schön, lass uns nachschauen, was drin ist!"
        play sound "audio/door_open.mp3"
        pause 3
        $ store.currentep += 10
        commander "Cool, eine kleine Akkuzelle. Hiermit können wir etwas unseren Strom wieder auffüllen!"
        $ ImageButtonActivate_state = True
    else:
        $ renpy.notify("Tresor geöffnet!")
        pause 1
        $ renpy.notify("Tresor ist leer!")

    $ renpy.pause(hard=True)
