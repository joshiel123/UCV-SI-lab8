# Laboratorio ADK UCV

## Descripción

`laboratorio-adk-ucv` es un paquete Python que implementa un asistente académico basado en Google ADK. El agente está diseñado para responder en español con explicaciones simples y accesibles sobre conceptos básicos.

## Estructura del proyecto

- `agente_ucv/agent.py` - Define el agente y las funciones de explicación de conceptos.
- `agente_ucv/__init__.py` - Inicializa el paquete Python.
- `tests/` - Carpeta para pruebas unitarias.
- `pyproject.toml` - Configuración del proyecto y dependencias.

## Dependencias

- Python 3.12 o superior
- `google-adk >=2.1.0,<3.0.0`
- `python-dotenv >=1.2.2,<2.0.0`

## Instalación

Recomendado usar Poetry:

```bash
cd laboratorio-adk-ucv
poetry install
```

## Uso básico

El agente principal se define en `agente_ucv/agent.py` y puede importarse directamente:

```python
from agente_ucv.agent import root_agent, explicar_concepto

resultado = explicar_concepto("api")
print(resultado)
```

Ejemplo de salida esperada:

```python
{'status': 'success', 'explicacion': 'Una API permite comunicación entre sistemas.'}
```

## Diseño del agente

El agente está configurado con:

- `model="gemini-flash-latest"`
- nombre `agente_ucv`
- descripción `Agente académico UCV`
- instrucciones en español y con un enfoque de lenguaje simple
- herramienta personalizada `explicar_concepto` para ofrecer respuestas estructuradas

## Desarrollo y pruebas

Aunque la carpeta `tests/` está disponible, actualmente no hay pruebas definidas. Puedes ejecutar un entorno de desarrollo con:

```bash
poetry shell
pytest
```

## Notas

- Actualiza el archivo `pyproject.toml` con una descripción más detallada si el proyecto evoluciona.
- La dependencia `python-dotenv` permite el uso de variables de entorno para configuraciones futuras.
