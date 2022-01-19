from typing import List, Union, Tuple


def x_squared(x):
    """
    A function to return the square of X.

    Args:
        x (float): A float or numpy array

    Returns:
        float: The value of x-squared
    """
    return x*x

def x_cubed(x):
    return x*x*x

class Polynomial:
    """
    Stores data for a polynomial
    Examples:
        >>> poly = Polynomial([1,2,3]) # 1+2*t+t**2
        >>> print(poly)
        >>> print(poly.eval(4)) # 57=4**2*3+4**1*2+4**0*1
    """
    def __init__(self,coeficiants):
        self._coef = coeficiants
    def eval(self,t=0):
        """ evaluates the polinomial at some value """
        return sum([coef * t**n for n,coef in enumerate(self._coef)])
    def __repr__(self):
        ret=''
        for n,coef in enumerate(self._coef):
            ret+=f'{"%+g"%coef}*t**{n}'
        return ret

class Quadratic(Polynomial):
    """
    A quadratic is a polynomial of degree 2
    Examples:
        >>> poly = Quadratic([6,5,1])
        >>> print(poly.roots()) # (x+2)*(x+3) has roots at -2,-3
    """
    def __init__(self,coeficiants):
        assert len(coeficiants) == 3
        Polynomial.__init__(self,coeficiants)
        self.even_function = coeficiants[1]==0

    def roots(self) -> List[Union[float,complex]]:
        """ returns the roots of the polynomial using the quadratic formula """
        c,b,a=self._coef
        return [-b+pm*(b**2-4*a*c)**(1/2)/(2*a) for pm in [-1,1]]
