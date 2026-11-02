import csv
from pathlib import Path

import pytest

from src.inscripcion import (
    AnticipoInsuficiente,
    Inscripcion,
    SaldoPendiente,
    evaluar_elegibilidad,
)

RUTA_CSV = Path(__file__).parent / "data" / "reglas_edutech.csv"
EXCEPCIONES = {
    "AnticipoInsuficiente": AnticipoInsuficiente,
    "SaldoPendiente": SaldoPendiente,
}


def cargar_casos(regla):
    with open(RUTA_CSV, newline="", encoding="utf-8") as archivo:
        filas = [f for f in csv.DictReader(archivo) if f["regla"] == regla]
    return [pytest.param(f, id=f["id_caso"]) for f in filas]


def test_matriz_cubre_minimo_de_casos():
    with open(RUTA_CSV, newline="", encoding="utf-8") as archivo:
        filas = list(csv.DictReader(archivo))
    assert len(filas) >= 9
    for regla in ("RN-01", "RN-02", "RN-03"):
        tipos = {f["tipo"] for f in filas if f["regla"] == regla}
        assert {"exito", "error", "limite"} <= tipos


@pytest.mark.parametrize("caso", cargar_casos("RN-01"))
def test_rn01_anticipo_minimo(caso):
    insc = Inscripcion(float(caso["costo_curso"]))
    if caso["esperado"] in EXCEPCIONES:
        with pytest.raises(EXCEPCIONES[caso["esperado"]]):
            insc.confirmar_pago(float(caso["monto"]))
        assert insc.estado == "PREINSCRITA"
    else:
        insc.confirmar_pago(float(caso["monto"]))
        assert insc.estado == caso["esperado"]


@pytest.mark.parametrize("caso", cargar_casos("RN-02"))
def test_rn02_elegibilidad_certificacion(caso):
    resultado = evaluar_elegibilidad(float(caso["asistencia"]), float(caso["calificacion"]))
    assert resultado == caso["esperado"]


@pytest.mark.parametrize("caso", cargar_casos("RN-03"))
def test_rn03_bloqueo_por_saldo_pendiente(caso):
    insc = Inscripcion(float(caso["costo_curso"]), float(caso["monto"]))
    if caso["esperado"] in EXCEPCIONES:
        with pytest.raises(EXCEPCIONES[caso["esperado"]]):
            insc.validar_emision_certificado()
    else:
        insc.validar_emision_certificado()


def test_pago_rechazado_no_modifica_monto_pagado():
    insc = Inscripcion(1000)
    with pytest.raises(AnticipoInsuficiente):
        insc.confirmar_pago(100)
    assert insc.monto_pagado == 0


def test_pago_no_positivo_es_invalido():
    with pytest.raises(ValueError):
        Inscripcion(1000).confirmar_pago(0)