#Zusatzaufgabe Robotersprache

label RobotSpricht:
    "Beep Bop Biiiiiip"
    robot "Hllao Mcehesnn, sied gegrßüt! Der Alridsnhafaoecutesg muss mineen Sooenozpsrsdur zsuetgezt haben.
    Ich hfofe, dsas ihr mich tztedrom vhseeertn knnöt."
    "krrrrz ssszzzhhh"
    robot "Stzee mien Ssyetm zcruük!"
    commander "Wenn wir Glück haben, dann könnte uns vielleicht der Roboter noch helfen!"
    $ randint = renpy.random.randint(1, 7)
    if randint == 1:
        robot "Zurücksetzen erfolgreich! \nStarte Morsekommunikation"
        play sound "audio/morse_robot.mp3"
        "Speichere dir den Morse Code ab und füge ihn bei {a=https://morsecode.world/international/translator.html}Übersetzer{/a} ein!"
        $ txt = "-.- . .. -. / ... -.-- ... - . -- / .. ... - / ... .. -.-. .... . .-. / .... .- .... .- .... .- -.-.-- -.-.-- -.-.-- / .-.-.- .-.-.- .-.-.- / .- -... . .-. / .. -.-. .... / --. . -... . / . ..- -.-. .... / . .. -. . -. / --. ..- - . -. / .-. .- - ---... / .-- . -. -. / .. .... .-. / . ..- -.-. .... / --- .--. - .. -- .- .-.. / ... -.-. .... ..-- - --.. - --..-- / -.. .- -. -. / -- .- -.-. .... - / .. .... .-. / . ... / .- -. --. .-. . .. ..-. . .-. -. / .-- .. . / -- .. -.-. .... / -.. . ..- - .-.. .. -.-. .... / ... -.-. .... .-- .. . .-. .. --. . .-. / .... .- .... .- .... .- -.-.-- -.-.-- -.-.--"
        $ ShowScreen("clipboard")
        "Lasse dir den Morse Code übersetzen."
        $ HideScreen("clipboard")
        commander "Urgh, ich glaube der Roboter hat das falsche Programm gestartet!"
        "skkrrrzzzzz skkrrrzzzzz miiimööööp"
        robot "System fehlhreaft, Ssytem fehlahreft, shlcate auf Nudotmos!"
        stop sound fadeout 4.0
        commander "Puhh Glück gehabt! Lass uns weitermachen!"
    else:
        robot "Zczueüretksn ist feeshellghcgan!"

    window hide
    $ renpy.pause(hard=True)
