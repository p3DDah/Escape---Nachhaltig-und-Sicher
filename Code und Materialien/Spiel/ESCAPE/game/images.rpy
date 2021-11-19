#SideImages
image side erde = "SideImages/erde.png"
image side commander = "SideImages/astronaut.png"
image side robot:
    "Objekte/Cockpit/Roboter.png"
    zoom 5
image side KI:
    "SideImages/KI_Auge.png"
    zoom 10000 / renpy.random.randint(10000, 10100)
#Szenen
image space_1:
    "Szenen/bg1.jpg"

image space_2:
    "Szenen/bg2.jpg"

image space_3:
    "Szenen/bg3.jpg"

image space_4:
    "Szenen/bg4.jpg"

image cockpit:
    "Szenen/cockpit.jpg"

image machine_room:
    "Szenen/machineroom.jpg"

image KI_Galaxie:
    "Szenen/KI_Galaxie.jpg"
    zoom 4.8

image door_cockpit:
    "Szenen/door_cockpit.jpg"

image door_machineroom:
    "Szenen/door_machineroom.jpg"

image EndGood Animated:
    "Szenen/EndGood1.jpg"
    pause 1.0
    "Szenen/EndGood2.jpg"
    pause 1.0
    "Szenen/EndGood3.jpg"
    pause 1.0
    "Szenen/EndGood4.jpg"
    pause 1.0
    repeat

image EndBad Animated:
    "Szenen/EndBad1.jpg"
    pause 0.5
    "Szenen/EndBad2.jpg"
    pause 0.5
    repeat

image KapselFalling:
    "Szenen/kapselfalling.jpg"
    size(1920,1080)

#Inventar
image inv_keycard:
    "Inventar/inv_keycard.png"
    size(80,80)

image white = "#fff"
image bg keyitem = "#0ac"
