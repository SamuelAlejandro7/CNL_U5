class AnticipoInsuficiente(Exception):
    pass


class SaldoPendiente(Exception):
    pass


class Inscripcion:
    def __init__(self, costo_curso, monto_pagado=0):
        raise NotImplementedError

    def confirmar_pago(self, monto):
        raise NotImplementedError

    def saldo_pendiente(self):
        raise NotImplementedError

    def validar_emision_certificado(self):
        raise NotImplementedError


def evaluar_elegibilidad(asistencia, calificacion):
    raise NotImplementedError