import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Configuración de la página
st.set_page_config(
    page_title="Modelo de Monod",
    page_icon="🧪"
)

# Título y descripción de la app
st.title("Simulación del Crecimiento Microbiano (Modelo de Monod)")
st.markdown("Ajusta los parámetros del modelo usando los controles de la barra lateral para ver cómo cambia la biomasa y el sustrato a lo largo del tiempo.")

# =========================
# Parámetros del modelo con widgets de Streamlit
# =========================
st.sidebar.header("Parámetros del Modelo")
mu_max = st.sidebar.slider("Velocidad máx. (μ_max, h⁻¹)", min_value=0.1, max_value=1.0, value=0.4, step=0.01)
Ks = st.sidebar.slider("Constante de saturación (Ks, g/L)", min_value=0.01, max_value=1.0, value=0.1, step=0.01)
Yxs = st.sidebar.slider("Rendimiento (Yxs, g/g)", min_value=0.1, max_value=1.0, value=0.5, step=0.01)

st.sidebar.header("Condiciones Iniciales")
X0 = st.sidebar.number_input("Biomasa inicial (X₀, g/L)", min_value=0.01, value=0.1, step=0.01)
S0 = st.sidebar.number_input("Sustrato inicial (S₀, g/L)", min_value=1.0, value=10.0, step=0.1)
t_fin = st.sidebar.number_input("Tiempo de simulación (h)", min_value=10, max_value=200, value=50)

# Ecuaciones diferenciales (la función ahora toma los parámetros como argumentos)
def monod_model(vars, t, mu_max, Ks, Yxs):
    X, S = vars
    mu = mu_max * S / (Ks + S)
    dXdt = mu * X
    dSdt = -(1/Yxs) * mu * X
    return [dXdt, dSdt]

# Resolver ODEs con los parámetros ajustables
t = np.linspace(0, t_fin, 500)
sol = odeint(monod_model, [X0, S0], t, args=(mu_max, Ks, Yxs))
X, S = sol.T

# =========================
# Visualización
# =========================
st.header("Resultados de la Simulación")

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(t, X, label="Biomasa (X)", linewidth=2)
ax.plot(t, S, label="Sustrato (S)", linewidth=2, linestyle="--")
ax.set_title("Crecimiento microbiano - Modelo de Monod")
ax.set_xlabel("Tiempo (h)")
ax.set_ylabel("Concentración (g/L)")
ax.legend()
ax.grid()

# Muestra el gráfico en la aplicación de Streamlit
st.pyplot(fig)
