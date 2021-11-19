#Zusatzaufgabe Figuren

label Hildegart:
    $ renpy.notify("Hildegart")
    "Namensschild: Hildegart\n
    Baujahr: 1024\n
    Seriennummer: 12 - 3 - 36 - 9 - 324 - ?" #9
    $ randint = renpy.random.randint(1, 10)
    if randint == 1:
        commander "Hm vielleicht können wir die Informationen für irgendwas gebrauchen."
    $ renpy.pause(hard=True)

label Detlef:
    $ renpy.notify("Detlef")
    "Namensschild: Detlef\n
    Baujahr: 2048\n
    Seriennummer: 5 - 10 - 11 - 13 - 17 - ?" #25
    $ randint = renpy.random.randint(1, 10)
    if randint == 1:
        commander "Hm vielleicht können wir die Informationen für irgendwas gebrauchen."
    $ renpy.pause(hard=True)

label Gudrun:
    $ renpy.notify("Gudrun")
    "Namensschild: Gudrun\n
    Baujahr: 512\n
    Seriennummer: 4 - 3 - 6 - 8 - 13 - ?" #20
    $ randint = renpy.random.randint(1, 10)
    if randint == 1:
        commander "Hm vielleicht können wir die Informationen für irgendwas gebrauchen."
    $ renpy.pause(hard=True)

label Dobby:
    $ renpy.notify("Dobby")
    "Namensschild: Dobby\n
    Baujahr: 32\n
    Seriennummer: 12 - 36 - 32 - 16 - 11 - ?" #22
    $ randint = renpy.random.randint(1, 10)
    if randint == 1:
        commander "Hm vielleicht können wir die Informationen für irgendwas gebrauchen."
    $ renpy.pause(hard=True)

label Ludwig:
    $ renpy.notify("Ludwig")
    "Namensschild: Ludwig\n
    Baujahr: 128\n
    Seriennummer: 121 - 11 - 16 - 4 - 9 - ?" #3
    $ randint = renpy.random.randint(1, 10)
    if randint == 1:
        commander "Hm vielleicht können wir die Informationen für irgendwas gebrauchen."
    $ renpy.pause(hard=True)
