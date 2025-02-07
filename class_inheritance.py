class shape:
     def __init__(self, colour, isfilled, shape):
         self.colour = colour
         self.isfilled = isfilled
         self.shape = shape
     def show(self, area, shape):
         print(f"Area of the {self.colour} {self.shape} is {self.area}")

class circle(shape):
    def __init__(self, r, colour, isfilled, shape):
        self.radius = r
        super().__init__(colour, isfilled, shape)

    def area_fun(self):
        self.area = 3.14 * self.radius *self.radius
        super().show(self.area, self.shape)

class rectangle(shape):
    def __init__(self, h, w, colour, isfilled, shape):
        self.h = h
        self.w = w
        super().__init__(colour, isfilled, shape)

    def area_fun(self):
        self.area = self.h * self.w
        super().show(self.area, self.shape)

class square(shape):
    def __init__(self, s , colour, isfilled, shape):
        self.s = s
        super().__init__(colour,isfilled, shape)

    def area_fun(self):
        self.area = self.s * self.s
        super().show(self.area, self.shape)

shape_circle = circle(5, "Yellow", "True", "Circle")
shape_circle.area_fun()
shape_rectangle = rectangle(10,7, "Black", "False", "Rectangle")
shape_rectangle.area_fun()
shape_square = square(6,"White", "True", "Square")
shape_square.area_fun()