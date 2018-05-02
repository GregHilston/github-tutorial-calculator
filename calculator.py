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
        return (x /y)

    #make sure to import math as math
    def log(self,x,y):
        return math.log(x,y)
    
    def square(self, x):
        """ Returns the square of x.
        """
        return ( x * x)