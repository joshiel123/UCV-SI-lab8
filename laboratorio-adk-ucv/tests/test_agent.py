import pytest
from agente_ucv.agent import explicar_concepto, root_agent
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


def test_configuracion_agente():
    """Prueba que el agente root_agent esté correctamente configurado con google-adk."""
    assert isinstance(root_agent, Agent)
    assert root_agent.name == "agente_ucv"
    assert root_agent.model == "gemini-flash-latest"
    assert "Eres un asistente académico" in root_agent.instruction
