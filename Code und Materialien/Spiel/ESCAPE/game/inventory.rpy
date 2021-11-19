init python:

    class InventoryItem:
        def __init__(self, img, title, text):
            self.img = img
            self.title = title
            self.text = text

    class UsableItem(InventoryItem):
        def __init__(self, img, title, text, label):
            InventoryItem.__init__(self, img, title, text)
            self.label = label

        def use(self):
            inventory.remove(self)
            renpy.call(self.label)

