from math import ceil
from settings import SAP_DEFAULT_PAGE, SAP_DEFAULT_RECORDS, SAP_MAX_RECORDS
from .sap_filter_options import *

def haveArgs(f):
    """
    Verificar si la expresión posee argumentos
    """
    def check(*args, **kwargs):
        if len(args):
            return f(*args, **kwargs)
        else:
            return None
    return check


@haveArgs
def argFilter(*args, op='eq'):
    """
    Estructura el filtro a utiizar.
    Syntax logic: expresiones a comparar, operador
    Syntax function: funcion, campo, valor, type='Function'
    """
    if op in operadores:
        if len(args) > 0:
            return ' {0} '.format(op).join(args)
        else:
            return None
    else:    
        nom = args[0]
        val = args[1] if type(args[1]) == int else '\'{0}\''.format(args[1])
        if op in comparadores:
            return '{0} {1} {2}'.format(nom, op, val)
        elif op in funciones:
            return '{0}({1},{2})'.format(op, nom, val)
        else:
            return None

def filters(args, campos):
    filtros = []
    for campo in campos:
        if args[campo[0]] != None:
            filtros.append(argFilter( campo[0] , args[campo[0]], op=campo[1] ))
    return filtros

@haveArgs
def argSelect(*args):
    """
    Determina los campos a selección a utiizar.
    Syntax: campos
    """
    if None in args:
        return None
    fields = [str(i) for i in args]
    return ', '.join(fields)


@haveArgs
def argOrderBy(*args):
    """
    Determina el formato de orden de acuerdo a los campos indicados.
    Syntax: [campo, orden]
    """
    if None in args:
        return None
    eachOrder = [' '.join(i) for i in args]
    return ', '.join(eachOrder)

#@haveArgs
def argTopSkip(page, size):
    """
    En base a la paginación, indica los valores apropiados de top y skip.
    Syntax: pagina, tamaño
    Result: top, skip, header
    """
    prefer = 'odata.maxpagesize='
    if str(page).isdigit() and str(size).isdigit():
        pg = int(page)
        sz = int(size)
        top = sz
        skip = (pg-1)*sz
        prefer += str(sz)
        return top, skip, prefer
    prefer += str(SAP_MAX_RECORDS)
    return None, None, prefer

def getParams(pOrderBy, pFilter, pSelect, page=None, pageSize=None):
    top, skip, header = argTopSkip(page, pageSize)
    params = {'$filter': pFilter, '$orderby': argOrderBy(pOrderBy), '$select': argSelect(pSelect), '$top': top, '$skip': skip, '$inlinecount': 'allpages'}
    return params, header

def getPgParams(pOrderBy, pFilter, pSelect, page, pageSize):
    pageF = SAP_DEFAULT_PAGE if (page==None or page<1) else page
    pageSizeF = SAP_DEFAULT_RECORDS if (pageSize==None or pageSize<0) else pageSize
    return getParams(pOrderBy, pFilter, argSelect(pSelect), pageF, pageSizeF)

def paginateSAP(page, pageSize, total, items):
    totalItems = int(total)
    json = {
        "page": page,
        "pages": ceil(totalItems/pageSize) if pageSize>0 else None,
        "pageSize": pageSize,
        "total": totalItems,
        "items": items
    }
    return json

def deleteFields(lista, subLista, camposDelete):
    for i in lista:
        for j in i[subLista]:
            for campo in camposDelete:
                j.pop(campo)
    return lista