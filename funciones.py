def filtrar_seniors(listas_devs):
    return [dev.nombre for dev in listas_devs if dev.es_senior()]