def factorial(n):
   return 1 if n == 0 else n * factorial(n - 1)

def sqrt(x):
    """
    Approximate the square root of x using a Taylor expansion.

    Parameters
    ----------
    x : float
        Input value, must be between 0 and 2.5
    tol : float
        Convergence tolerance for 8+ significant figures.
    max_terms : int
        Safety cap on number of terms.

    Returns
    -------
    y : float
        Approximation of sqrt(x).
    """
    if x < 0 or x > 2.5:
        raise ValueError("x must be between 0 and 2.5")
    if x == 0:
        return 0.0
    elif x == 1:
        return 1.0
    elif 0 < x <= 0.75:
        a = 0.5  # Choose expansion point a
    elif 0.75 < x <= 1.25:
        a = 1.0  # Choose expansion point a
    elif 1.25 < x <= 1.75:
        a = 1.5  # Choose expansion point a
    elif 1.75 < x <= 2.25:
        a = 2.0
    elif 2.25 < x <= 2.5:
        a = 2.5
    # Choose expansion point a
    # closest basepoint to x

    result = a**0.5  # first term of Taylor expansion to account for offset
    term = 1.0
    n = 1
    cond = 1e-9  # condition for 8 significant figures

    while abs(term) > cond:
       
        coeff = 1.0
        for j in range(1, n):
            coeff *= (-0.5 * (2*j - 1))
        coeff = coeff * 0.5 
        # denominator n! * (a^0.5)^(2n-1)
        denom = factorial(n) * (a**((2*n - 1)/2))

        term = coeff * ((x - a)**n) / denom
        result += term
        n += 1

    return result
def arcsin(a):
    if a<0 or a>1:
        raise ValueError('Input number from 0-1')

    term = a #first term
    result = 0
    old_result = float('inf') #force entry into while loop 
    n = 1 
    max_terms = 1000 #safety cap on number of terms
    cond = 1e-9 #condition for 8 significant figures

    while abs(result - old_result) > cond and n < max_terms:

        denom = (n**2) * (factorial(2*n) / ((factorial(n))**2))
        term = ((2*a)**(2*n)) / denom
        old_result = result 
        result += term
        n += 1
        # implementation of arcsin
        # (using the series from Borwein and Chamberlain 2007)
        y = (result*0.5)**0.5
    return y
def launch_angle_range(ve_v0, alpha, tol_alpha):
# """Description of function.
# Parameters
# ----------
# Returns
# -------
# """
# ...
# your implementation here should call on your
# functions implementing Equations (17) and (18)
# ...
    sin_phi = (1 + alpha) * sqrt(1 - (alpha / (1 + alpha)) * (ve_v0**2))
    if sin_phi > 1 or sin_phi < -1:
        raise ValueError('No valid launch angle exists for these parameters')
    phi = arcsin(sin_phi)
    phi_range = (phi - tol_alpha, phi + tol_alpha)
    return phi_range






