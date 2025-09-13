# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 10:42:56 2025

@author: Hpwin11
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# =========================
# Parámetros del modelo
# =========================
mu_max = 0.4     # h^-1 (velocidad máxima de crecimiento)
Ks = 0.1         # g/L (constante de saturación)
Yxs = 0.5        # g biomasa / g sustrato

# =========================
# Ecuaciones diferenciales
# =========================
def monod_model(vars, t):
    X, S = vars
    mu = mu_max * S / (Ks + S)
    dXdt = mu * X
    dSdt = -(1/Yxs) * mu * X
    return [dXdt, dSdt]

# =========================
# Condiciones iniciales
# =========================
X0 = 0.1   # g/L biomasa inicial
S0 = 10.0  # g/L sustrato inicial
t = np.linspace(0, 50, 500)  # tiempo (h)

# Resolver ODEs
sol = odeint(monod_model, [X0, S0], t)
X, S = sol.T

# =========================
# Visualización
# =========================
plt.figure(figsize=(10,5))

plt.plot(t, X, label="Biomasa (X)", linewidth=2)
plt.plot(t, S, label="Sustrato (S)", linewidth=2, linestyle="--")

plt.title("Crecimiento microbiano - Modelo de Monod")
plt.xlabel("Tiempo (h)")
plt.ylabel("Concentración (g/L)")
plt.legend()
plt.grid()
plt.show()
