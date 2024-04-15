# TPcit0 - Una galería gráfica colaborativa con Gapminder
Trabajo Práctico: Consigna Integradora Temática Nro. 0, AKA "tepecito"

Un acercamiento amigable al TP #1

## Intro

[Streamlit](https://streamlit.io/) es un _framework_ de Python para crear aplicaciones web de manera rápida y sencilla (para quienes lo conocen, piensen en Shiny, de R). En este TP0, crearemos colaborativamente una galería de visualizaciones del dataset de Gapminder.

## Consigna


1. _Forkee_ este repositorio a su cuenta personal de GitHub.
2. Comience una rama con el mismo nombre que su usuario de dicha plataforma.
3. En la carpeta `plotters`, cree un nuevo archivo de Python.
4. Copie los contenidos de la plantilla `paisesPorContinente.py` o `lifeExpOceania.py` al archivo recién creado. 
   Este archivo debe contener una única función sin argumentos, de nombre `plot`, y que devuelva:
  - un objeto seaborn.objects.Plot con el gráfico realizado, o (preferentemente)
  - un diccionario (`dict`) con tres claves: `figura, descripcion autor` con la información relevante.
5. En el nuevo archivo, a partir del dataset `gapminder` en el paquete homónimo, y usando la interfaz `objects` del paquete `seaborn`, genere una 
visualización que resalte algún aspecto de interés del dataset. Asegúrese de seguir buenas prácticas: dé nombre a los ejes y 
título al gráfico, no codifique información innecesaria en canales superfluos, et cetera. Escriba un sucinto párrafo descriptivo para la visualización.
6. Vaya _commiteando_ los cambios que realiza a su rama, hasta estar satisfecha con el resultado.
7. Publique la rama en su _fork_ del repositorio actual, y cree un Pull Request contra el repositorio original.
  - Ponga como revisor a un compañero de confianza, y atienda a sus indicaciones hasta que se dé por aprobado.
  - Ponga como segundo revisor a un miembro de la cátedra (`slap, nz-angel, capitantoto`) y repita.

Con los PRs mergeados, levantaremos una app pública para compartir con los compañerxs de ambos turnos y el resto de la comunidad educativa.

## Desarrollo local

Técnicamente, el desarrollo del TP se puede realizar en cualquier plataforma, y finalmente "venir al repositorio" sólo para crear el `plotter` relevante y publicar su rama en GitHub. Sin embargo, les recomiendo ampliamente que intenten desarrollar _desde el repositorio_, para que vean cómo se va construyendo la app en vivo.

### Creación del entorno virtual de desarrollo
En la consola, desde la raíz del repo (cf.: comando `cd` para `c`ambiar de `d`irectorio, y `pwd` para ver el _present working directory_):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Con esto, quedará creado un entorno virtual con las librerías necesarias
- para crear la visualizacion (`seaborn, pandas, gapminder`),
- para correr la aplicación (`streamlit, watchdog`) y
- (opcionalmente) para usar el entorno virtual creado (`.venv`) como _kernel_ de Jupyter

### Levantar la aplicación localmente

_Con el entorno activado_, lo único que hay que hacer es usar `streamlit run app.py` y navegar a `http://localhost:8501/`

```bash
source .venv/bin/activate
streamlit run app.py
```

Si no lo hace solo, abrir el navegador e ir a http://localhost:8501/

Cada vez que guarde los archivos, los cambios se verán reflejados en la _app_ automágicamente. Basta con refrescar el sitio (Ctrl+R, F5) para ver los cambios más recientes.