"""
# TPcit0: una galería de _gapminder_
"""

import streamlit as st
import matplotlib.pyplot as plt
import seaborn.objects as so
import importlib
import plotters
from pkgutil import iter_modules


def submodulos(modulo):
    return [submodule.name for submodule in iter_modules(modulo.__path__)]

# st.set_page_config(layout="wide")
st.write("# TPcit0: una galería de _gapminder_")


opcion = st.selectbox("¿Qué gráfico desea ver?", submodulos(plotters))

fig = plt.figure(figsize=(11,6))
data = importlib.import_module(f"plotters.{opcion}").plot()

if isinstance(data, so.Plot):
    data = dict(autor="N/A", descripcion="No disponible", figura=data)

data["figura"].on(fig).show()
st.write("### Descripción\n", data["descripcion"])
st.write("#### Autor(es)\n", data["autor"])
st.pyplot(fig)
