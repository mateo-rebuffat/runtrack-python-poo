class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("x :", self.x, "y :", self.y)

    def afficherX(self):
        print("x :", self.x)

    def afficherY(self):
        print("y :", self.y)

    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur

    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur


point1 = Point(10, 20)


point1.afficherLesPoints()


point1.afficherX()


point1.afficherY()


point1.changerX(50)
point1.changerY(60)

point1.afficherLesPoints()

