import pytest
from agente_ucv.agent import explicar_concepto, calcular_promedio, root_agent
from google.adk.agents.llm_agent import Agent

def test_explicar_concepto_existente():
    """Prueba que el agente explique conceptos que sí existen en su base de conocimiento."""
    resultado_api = explicar_concepto("api")
    assert resultado_api["status"] == "success"
    assert "comunicación entre sistemas" in resultado_api["explicacion"]

    resultado_algoritmo = explicar_concepto("algoritmo")
    assert resultado_algoritmo["status"] == "success"
    assert "secuencia de pasos" in resultado_algoritmo["explicacion"]

    resultado_bd = explicar_concepto("base de datos")
    assert resultado_bd["status"] == "success"
    assert "almacena información" in resultado_bd["explicacion"]


def test_explicar_concepto_nuevos():
    """Prueba los 5 nuevos conceptos técnicos agregados al agente."""
    conceptos_nuevos = ["git", "docker", "frontend", "backend", "cloud computing"]
    for concepto in conceptos_nuevos:
        resultado = explicar_concepto(concepto)
        assert resultado["status"] == "success"
        assert len(resultado["explicacion"]) > 0


def test_explicar_concepto_no_existente():
    """Prueba el comportamiento cuando un concepto no está registrado."""
    resultado = explicar_concepto("computación cuántica")
    assert resultado["status"] == "not_found"
    assert resultado["explicacion"] == "Concepto no registrado."


def test_explicar_concepto_normalizacion():
    """Prueba que la función maneje mayúsculas y espacios innecesarios."""
    resultado = explicar_concepto("   API   ")
    assert resultado["status"] == "success"
    assert "comunicación entre sistemas" in resultado["explicacion"]


def test_explicar_concepto_validacion():
    """Prueba que la función de explicar conceptos valide correctamente la entrada."""
    # Entrada vacía
    resultado_vacio = explicar_concepto("   ")
    assert resultado_vacio["status"] == "validation_error"
    assert "debe ser un texto no vacío" in resultado_vacio["explicacion"]

    # Entrada de tipo incorrecto (None)
    resultado_invalido = explicar_concepto(None)
    assert resultado_invalido["status"] == "validation_error"
    assert "debe ser un texto no vacío" in resultado_invalido["explicacion"]


def test_calcular_promedio_exitoso():
    """Prueba el cálculo de promedio en casos de éxito con diferentes tipos de números."""
    # Lista de enteros
    resultado_enteros = calcular_promedio([10, 15, 20])
    assert resultado_enteros["status"] == "success"
    assert resultado_enteros["promedio"] == 15.0
    assert resultado_enteros["cantidad"] == 3

    # Lista con flotantes
    resultado_flotantes = calcular_promedio([12.5, 14.8, 11.2])
    assert resultado_flotantes["status"] == "success"
    assert resultado_flotantes["promedio"] == 12.83  # (12.5 + 14.8 + 11.2) / 3 = 12.8333...

    # Lista con strings numéricos convertibles
    resultado_strings = calcular_promedio(["10", 15, "18.5"])
    assert resultado_strings["status"] == "success"
    assert resultado_strings["promedio"] == 14.5


def test_calcular_promedio_validacion():
    """Prueba la validación exhaustiva de entradas de la herramienta calcular_promedio."""
    # Parámetro principal no es una lista
    res_no_lista = calcular_promedio("no_soy_lista")
    assert res_no_lista["status"] == "validation_error"
    assert "debe ser una lista de números" in res_no_lista["error"]

    # Lista vacía
    res_vacio = calcular_promedio([])
    assert res_vacio["status"] == "validation_error"
    assert "no puede estar vacía" in res_vacio["error"]

    # Elemento no numérico
    res_no_num = calcular_promedio([10, "aprobado", 15])
    assert res_no_num["status"] == "validation_error"
    assert "no es un número válido" in res_no_num["error"]

    # Valor inferior al rango permitido (<0)
    res_bajo = calcular_promedio([12, -1, 15])
    assert res_bajo["status"] == "validation_error"
    assert "fuera del rango permitido (0 a 20)" in res_bajo["error"]

    # Valor superior al rango permitido (>20)
    res_alto = calcular_promedio([14, 21, 18])
    assert res_alto["status"] == "validation_error"
    assert "fuera del rango permitido (0 a 20)" in res_alto["error"]


def test_configuracion_agente():
    """Prueba que el agente root_agent esté correctamente configurado con google-adk."""
    assert isinstance(root_agent, Agent)
    assert root_agent.name == "agente_ucv"
    assert root_agent.model == "gemini-flash-latest"
    assert "Eres un asistente académico" in root_agent.instruction
    assert explicar_concepto in root_agent.tools
    assert calcular_promedio in root_agent.tools
