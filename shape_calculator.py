class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        return (f"{'*' * self.width}\n" * self.height) if self.width <=50 and self.height <=50 else 'Too big for picture.'
    def get_amount_inside(self, shape):
        #fix this function
        if shape.width < self.width or shape.height < self.height:
            return 0
        if shape.width == self.width and shape.height == self.height:
            return 1
                    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
    def __repr__(self):
        return f"Square(side={self.width})"
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
