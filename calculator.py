import math


class Calculator:
    """A simple Calculator class used to demonstrate Git and Github features
    """

    def add(self, x, y):
        """Adds x and y together and returns the sum
        """

        return x + y

    def subtract(self, x, y):
        """Subtracts y from x and returns the difference
        """

        return x - y

    def multiply(self, x, y):
        """Multiples x by y and returns the product
        """

        return (x * y)


    def divide(self, x, y):
        """Divides x by y and returns the quotient.
        Note, that this uses Integer division.
        """
        return x//y


    def tan(self, x):
        """Returns the tangent value of x
        """

        return math.tan(x)

    def sin(self, x):
        """Returns the sine value of x
        """

        return math.sin(x)

    def log(self, x, y):

        return math.log(x,y)

    def square(self, x):
        """ Returns the square of x.
        """

        return (x * x)
    
    def cube(self, x):
        """Returns the cubed value of x.
        """
    
        return (x * x * x)
