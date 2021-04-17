from models import db, Boletas

def validarPago(nData):
    cod = nData.codBoleta if hasattr(nData, 'codBoleta') else -1
    req = db.session.query(Boletas).filter(Boletas.boleta == nData.boleta).all()
    for pago in req:
        if pago != None and pago.codBoleta != cod:
            if pago.medioPago == nData.medioPago:
                if pago.cuentaCod == nData.cuentaCod and pago.medioPago == 1:
                    return ('El depósito realizado a la cuenta ya ha sido registrado.', 409)
                elif pago.clienteCod == nData.clienteCod and pago.medioPago != 1:
                    return ('La transferencia/cheque del cliente ya ha sido registrado.', 409)
    return False