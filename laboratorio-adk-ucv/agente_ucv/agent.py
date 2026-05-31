from google.adk.agents.llm_agent import Agent

def explicar_concepto(concepto: str) -> dict:
    """Explica un concepto de informática de forma estructurada con validación de entrada."""
    # Validación de entrada
    if not isinstance(concepto, str) or not concepto.strip():
        return {
            "status": "validation_error",
            "explicacion": "El concepto proporcionado debe ser un texto no vacío."
        }

    conceptos = {
        "api": "Una API permite comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos.",
        "base de datos": "Una base de datos almacena información.",
        "git": "Un sistema de control de versiones distribuido para rastrear cambios en el código fuente.",
        "docker": "Una plataforma para desarrollar, enviar y ejecutar aplicaciones dentro de contenedores ligeros.",
        "frontend": "La parte de un sitio web o aplicación con la que el usuario interactúa directamente.",
        "backend": "La parte del servidor que procesa los datos, la lógica del negocio y se comunica con la base de datos.",
        "cloud computing": "El suministro de servicios informáticos (servidores, almacenamiento, redes) a través de Internet."
    }
    
    concepto_limpio = concepto.lower().strip()
    if concepto_limpio in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto_limpio]
        }
    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado."
    }

def calcular_promedio(notas: list) -> dict:
    """Calcula el promedio de una lista de notas con validación exhaustiva de tipo, valor y rango (0-20)."""
    # Validación de entrada: tipo de dato principal
    if not isinstance(notas, list):
        return {
            "status": "validation_error",
            "error": "El parámetro 'notas' debe ser una lista de números."
        }
    
    # Validación de entrada: lista vacía
    if len(notas) == 0:
        return {
            "status": "validation_error",
            "error": "La lista de notas no puede estar vacía."
        }
    
    valores_numericos = []
    # Validación de entrada: elementos numéricos y límites de nota
    for i, nota in enumerate(notas):
        # Evitar booleanos ya que heredan de int en Python
        if isinstance(nota, bool) or not isinstance(nota, (int, float)):
            try:
                # Intentar conversión si es posible
                nota_num = float(nota)
            except (ValueError, TypeError):
                return {
                    "status": "validation_error",
                    "error": f"El valor '{nota}' en el índice {i} no es un número válido."
                }
        else:
            nota_num = float(nota)
        
        # Validación de rango académico UCV (0 a 20)
        if nota_num < 0 or nota_num > 20:
            return {
                "status": "validation_error",
                "error": f"La nota {nota_num} en el índice {i} está fuera del rango permitido (0 a 20)."
            }
            
        valores_numericos.append(nota_num)
        
    promedio = sum(valores_numericos) / len(valores_numericos)
    return {
        "status": "success",
        "cantidad": len(valores_numericos),
        "notas_procesadas": valores_numericos,
        "promedio": round(promedio, 2)
    }

root_agent = Agent(
    model="gemini-flash-latest",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico.
    Responde en español.
    Usa lenguaje simple.
    """,
    tools=[explicar_concepto, calcular_promedio],
)