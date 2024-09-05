# StruckGen

StruckGen es una herramienta de línea de comandos escrita en Python que genera estructuras de directorios y archivos basadas en un archivo Markdown. Es ideal para iniciar rápidamente nuevos proyectos con una estructura predefinida.

## Características

- Lee un archivo Markdown y genera una estructura de directorios y archivos correspondiente.
- Crea una carpeta principal con el nombre del proyecto especificado por el usuario.
- Genera carpetas basadas en los encabezados del Markdown (# ## ###).
- Crea archivos basados en los elementos de lista (- ) en el Markdown.
- Interfaz gráfica simple para seleccionar el archivo Markdown y nombrar el proyecto.
- Compatible con Windows.

## Requisitos

- Python 3.6 o superior
- Biblioteca tkinter (generalmente viene preinstalada con Python)

## Instalación

1. Clona este repositorio o descarga el archivo `struckgen.py`.
2. Asegúrate de tener Python instalado en tu sistema.

## Uso

1. Ejecuta el script desde la línea de comandos o haciendo doble clic en él:

   ```
   python struckgen.py
   ```

2. Se abrirá una ventana de diálogo para seleccionar el archivo Markdown con la estructura deseada.

3. Introduce el nombre del proyecto cuando se te solicite.

4. StruckGen creará la estructura de carpetas y archivos en el mismo directorio donde se encuentra el archivo Markdown seleccionado.

## Formato del archivo Markdown

El archivo Markdown debe seguir este formato:

- Usa encabezados (#, ##, ###, etc.) para representar carpetas.
- Usa elementos de lista (- ) para representar archivos.

Ejemplo:

```markdown
# proyecto
## src
- main.py
## docs
- README.md
## tests
- test_main.py
```

Este Markdown generará la siguiente estructura:

```
proyecto/
├── src/
│   └── main.py
├── docs/
│   └── README.md
└── tests/
    └── test_main.py
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de enviar un pull request.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)