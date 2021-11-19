init python:
    import datetime
    import pygame.scrap
    def copytext(t):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, t.encode("utf-8"))

screen clipboard():

    frame:
        has vbox
        spacing 20
        text "Text:\n\"[txt]\""
        text "Klicke den Knopf, um den Text in deine Zwischenablage zu speichern"
        textbutton "In Zwischenablage speichern" action Function(copytext, t=txt)
        # textbutton "Schließen" action Hide("clipboard")

screen bars:
    bar value currentep range maxep xalign 0.949 yalign 0.015 xmaximum 145 xysize(145,16) left_bar "#ffd535"  right_bar "#ffffff00"
    bar:
        value currentdp
        range maxdp
        xalign 0.95
        yalign 0.031
        xmaximum 130
        xysize(130,16)
        left_bar "#ffffffaa"  right_bar "#ffffff00"

    add "Inventar/bars.png" xalign 1.0 yalign 0

    label "[currentep]/[maxep]" xalign 0.87 yalign 0.015 text_color "#192638" text_size 16

    label "[currentdp]/[maxdp]" xalign 0.878 yalign 0.033 text_color "#192638" text_size 16

screen inventory_button:
    imagebutton:
        idle "Inventar/bagpack.png"
        hover "Inventar/bagpack_hover.png"
        action If(InventarCheck_state, true=[Call("OpenInventory")], false=[Notify("Momentan nicht verfügbar!")])
        xalign 0.985
        yalign 0.01
        at transform:
            zoom 0.8

screen Hinweis_button:
    imagebutton:
        idle "Hinweise/Notizen.png"
        hover "Hinweise/Notizen_Hover.png"
        action If(HinweisCheck_state, true=[Call("Hinweismenu")], false=[Notify("Momentan nicht verfügbar!")])
        xalign 0.99
        yalign 0.98
        at transform:
            zoom 0.83

style inventory_label:
    xalign 0.2

style slot:
    background Frame("square", 0,0)
    minimum(80,80)
    maximum(80,80)
    xalign 0.5
    yalign 0.5

style info:
    background None
    xalign 0.5
    yalign 0.5

screen inventory_screen:
    modal True
    zorder 10

    add "Inventar/background.png"

    frame:
        style "info"
        xalign 0.03
        yalign 0.33
        vbox:
            label "Allgemeine Infos" xalign 0.5 text_color "#767a88"
            label "Energie: [currentep]/[maxep]" xalign 0.5 text_color "#767a88"
            label "Daten: [currentdp]/[maxdp]" xalign 0.5 text_color "#767a88"

    #inventory grid
    vbox:
        xalign 0.5
        yalign 0.5
        grid 14 5:
            spacing 5
            for item in inventory:
                frame:
                    style "slot"
                    imagebutton idle item.img action SetVariable("selected_item", item)

            for i in range(len(inventory), 70):
                frame:
                    style "slot"
                    imagebutton idle "square" action SetVariable("selected_item", None)


    textbutton "Schließen":
        action [Call("CloseInventory"), SetVariable("selected_item", None)]
        xalign 0.5
        yalign 0.804

    #item details
    if selected_item != None:
        add selected_item.img xalign 0.9345 yalign 0.306

        frame:
            style "info"
            xalign 0.993
            yalign 0.445
            xminimum 300
            yminimum 149
            vbox:
                xalign 0.5
                label "[selected_item.title]" xalign 0.5 text_color "#5d616c"
                label "[selected_item.text]" xalign 0.5 text_color "#767a88"

        if isinstance(selected_item, UsableItem):
            textbutton "Benutzen" xalign 0.993 yalign 0.505 action [SetVariable("selected_item", None), Function(selected_item.use)]

#Spiel Timer
screen game_countdown:
    add "Inventar/clock.png" xalign 0 yalign 0
    if game_running:
        timer 1 repeat True action If(game_time > 0, true=SetScreenVariable('game_time', game_time - 1), false=[Hide('game_countdown'), Jump("gameover")])
    label str(datetime.timedelta(seconds=game_time)) xalign 0.015 yalign 0.012 text_color "#fff"

screen game_over:
    label "GAME\nOVER" xalign 0.5 yalign 0.5 text_color "#aa1948" text_size 200
