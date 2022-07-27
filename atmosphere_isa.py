import numpy as np
from collections.abc import Iterable

"""ISA Standard atmosphere to approximate the variation of True Air Speed (TAS) with altitude
Author : Nicolas MONROLIN
Date: 04/12/2020
"""

# All computed data are in SI units
p0 = 101325  # Pa
rho0 = 1.225  # kg/m^3
T0 = 288.15 # Kelvin (equal to 15C)
g = 9.80665 # m/s^2
r = 287.04  # m^2/K.s^2
gamma = 1.4 # specific heat coefficient ratio of air

# SOURCE : http://fisicaatmo.at.fcen.uba.ar/practicas/ISAweb.pdf
def T_ISA(h):
    """Returns ISA temperature (K) versus height (m))"""
    if isinstance(h,Iterable): # check if the input is a list, apply the function to all elements
        return np.array(list(map(T_ISA,h)))
    else:
        if h<=11000: # troposhere
            return T0-6.5*h/1000
        if h>11000: # above tropopause
            return 216.65 # -56.5C

def p_ISA(h):
    """Returns ISA pressure (Pa) versus height (m)"""
    if isinstance(h,Iterable):
        return np.array(list(map(p_ISA,h)))
    else:
        if h<=11000: # troposhere
            return p0*(1-0.0065*h/T0)**5.2561
        if h>11000: # above tropopause
            return 22632*np.exp(-g/(r*216.65)*(h-11000))

def rho_ISA(h):
    """Return ISA density (kg/m^3) versus height (m)"""
    return p_ISA(h)/(r*T_ISA(h))

def a_ISA(h):
    """Return ISA speed of sound (m/s) versus height (m)"""
    return np.sqrt(1.4*r*T_ISA(h))


def kts_ms(speed):
    """Convert m/s to knots"""
    return speed/1852*3600

def ft_m(height):
    """Convert m to feet"""
    return height/0.3048

if __name__=="__main__":
    h=60000*0.3048
    print(p_ISA(h)*1e-2)
    print(rho_ISA(h))
    print(T_ISA(h)-273.15)
    print(kts_ms(a_ISA(h)))

