from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the model
        self.hand = Actor("4hz0a00fhmm8-FreeRealisticHand")

        # Reparent the model to the rendering scene
        self.hand.reparentTo(self.render)

        # Set position and scale
        self.hand.setScale(0.5, 0.5, 0.5)
        self.hand.setPos(Point3(0, 0, 0))

app = MyApp()
app.run()
