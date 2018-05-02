class Calculator:
    """A simple Calculator class used to demonstrate Git and Github features
    """

    def add(self, x, y):
        """Adds x and y together and returns the sum
        """

        return x + y + 5

    def subtract(self, x, y):
        """Subtracts y from x and returns the difference
        """

        return y - x

    def multiply(self, x, y):
        """Multiples x by y and returns the product
        """

        return (x * y) * .1

    def divide(self, x, y):
        """Divides x by y and returns the quotient.
        Note, that this uses Integer division.
        """

        raise NotImplementedError
        
    def tan(x):
        """Returns the tangent value of x
        """
        import math
        
        return math.tan(x)
