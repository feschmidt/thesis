"""
Demonstration of beta_L on supercurrent modulation for magnetic flux
"""
#%%
import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
from scipy.constants import e, h
from scipy.optimize import fsolve
Phi_0 = h / (2 * e)

#%%
phi_ext = np.linspace(0, 2 * Phi_0, 101)
l = np.linspace(0, )


#%%
def equations(p):
    x, y = p
    return (x + y**2 - 4, np.exp(x) + x * y - 3)


#%%
x, y = fsolve(equations, (-0.1e3, 10))
print(x, y)
print(equations((x, y)))


# %%
def max_Is(phi1, Phi, Ic, Phi0):
    return 2 * Ic * cos(pi * Phi / Phi0) * cos(phi1 + pi * Phi / Phi0)


def null_flux(phi1, Phie, Phi, L, Ic, Phi0):
    return Phi - Phie + L * Ic / 2 * sin(
        pi * Phi / Phi0) * cos(phi1 + pi * Phi / Phi0)


def SQUID_eqs(pars, L=0, Ic=1, Phi0=1):
    phi1, Phie, Phi = pars
    return (max_Is(phi1, Phi, Ic, Phi0), null_flux(phi1, Phie, Phi, L, Ic,
                                                   Phi0))


# %%
p0 = (0, 0, 0)
phi1, Phie, Phi = fsolve(SQUID_eqs, p0)

print(phi1, Phie, Phi)

# %%
