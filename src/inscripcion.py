ANTICIPO_MINIMO = 0.50
ASISTENCIA_MINIMA = 80
CALIFICACION_MINIMA = 70


class AnticipoInsuficiente(Exception):
    pass


class SaldoPendiente(Exception):
    pass


class Inscripcion:
    def __init__(self, costo_curso, monto_pagado=0):
        self.costo_curso = costo_curso
        self.monto_pagado = monto_pagado
        self.estado = "PREINSCRITA"

    def confirmar_pago(self, monto):
        if monto <= 0:
            raise ValueError("el monto debe ser positivo")
        nuevo_total = round(self.monto_pagado + monto, 2)
        if nuevo_total < round(self.costo_curso * ANTICIPO_MINIMO, 2):
            raise AnticipoInsuficiente("el anticipo es menor al 50% requerido")
        self.monto_pagado = nuevo_total
        self.estado = "INSCRITA"

    def saldo_pendiente(self):
        return round(self.costo_curso - self.monto_pagado, 2)

    def validar_emision_certificado(self):
        if self.saldo_pendiente() > 0:
            raise SaldoPendiente("emision bloqueada: saldo pendiente de pago")


def evaluar_elegibilidad(asistencia, calificacion):
    if calificacion < CALIFICACION_MINIMA:
        return "NO_ACREDITADO"
    if asistencia < ASISTENCIA_MINIMA:
        return "CONSTANCIA"
    return "CERTIFICADO" 