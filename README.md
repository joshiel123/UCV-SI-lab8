# Laboratorio ADK UCV

## Descripción

`laboratorio-adk-ucv` es un paquete Python diseñado para ofrecer un asistente académico en español utilizando la librería `google-adk`.
El proyecto contiene un agente simple que responde con explicaciones claras y breves de conceptos básicos a través de una función dedicada.

## Características principales

- Agente académico configurado con `Gemini Flash`.
- Respuestas en español usando lenguaje sencillo.
- Función de herramienta personalizada `explicar_concepto` para retornar resultados estructurados.
- Estructura lista para ampliarse con más conceptos y nuevas herramientas.

## Estructura del proyecto

- `laboratorio-adk-ucv/pyproject.toml` — configuración del paquete y dependencias.
- `laboratorio-adk-ucv/laboratorio-adk-ucv/agente_ucv/agent.py` — definición del agente y lógica de explicación de conceptos.
- `laboratorio-adk-ucv/laboratorio-adk-ucv/agente_ucv/__init__.py` — inicializador del paquete.
- `laboratorio-adk-ucv/laboratorio-adk-ucv/tests/test_agent.py` — punto para pruebas unitarias.

## Dependencias

- Python 3.14 o superior
- `google-adk >=2.1.0,<3.0.0`
- `python-dotenv >=1.2.2,<2.0.0`

> Nota: el `pyproject.toml` actual declara `requires-python = ">=3.14"`, por lo que es importante utilizar una versión de Python compatible.

## Instalación

Se recomienda usar Poetry para instalar las dependencias:

```bash
cd c:\Users\famil\Downloads\Ucv-ate-si-lab-08
poetry install
```

## Uso básico

Importa el agente y la función de explicación desde el módulo principal:

```python
from laboratorio_adk_ucv.agente_ucv.agent import explicar_concepto

resultado = explicar_concepto("api")
print(resultado)
```

Salida esperada:

```python
{'status': 'success', 'explicacion': 'Una API permite comunicación entre sistemas.'}
```

## Diseño del agente

El agente se define en `laboratorio-adk-ucv/agente_ucv/agent.py` y utiliza:

- `model="gemini-flash-latest"`
- `name="agente_ucv"`
- `description="Agente académico UCV"`
- instrucciones en español con lenguaje simple
- herramienta `explicar_concepto` para generar respuestas estructuradas

La función `explicar_concepto` mapea conceptos comunes a explicaciones predefinidas, y devuelve un diccionario con `status` y `explicacion`.

## Desarrollo y pruebas

Actualmente la carpeta `tests/` existe pero el archivo `test_agent.py` está vacío.
Para comenzar a desarrollar pruebas, crea casos que verifiquen:

- respuestas válidas para conceptos registrados
- manejo de conceptos no registrados
- formato de salida esperado

Ejecuta las pruebas con:

```bash
poetry run pytest
```

## Recomendaciones futuras

- Agregar más conceptos y respuestas en `explicar_concepto`.
- Implementar tests unitarios en `laboratorio-adk-ucv/tests/test_agent.py`.
- Añadir documentación de API y ejemplos de uso reales.
- Considerar un archivo `README.md` dentro del paquete para documentación interna.
