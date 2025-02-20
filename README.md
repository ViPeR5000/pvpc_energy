# pvpc_energy
![UFD logo](https://github.com/yinyang17/pvpc_energy/raw/main/assets/logo-ufd.png) ![ESIOS logo](https://github.com/yinyang17/pvpc_energy/raw/main/assets/logo-esios.png) ![CNMC logo](https://github.com/yinyang17/pvpc_energy/raw/main/assets/logo-cnmc.png)
Importa en el panel de energía los consumos y costes de ufd.es y ree.es. Calcula la factura en curso y las anterioes de cnmc.gob.es

![Daily consumption](https://github.com/yinyang17/pvpc_energy/raw/main/assets/energy-daily.png)![Monthly consumption](https://github.com/yinyang17/pvpc_energy/raw/main/assets/energy-monthly.png)
![Bills](https://github.com/yinyang17/pvpc_energy/raw/main/assets/bills.png)

## Imstalación y configuración
Necesitas estar registrado en https://www.ufd.es.
Después de reiniciar y añadir la integración, deberás indicar las credenciales de UFD y el número de facturas a mostrar en la Markdown Card.
![Config credentials](https://github.com/yinyang17/pvpc_energy/raw/main/assets/config-credentials.png)![Config bills](https://github.com/yinyang17/pvpc_energy/raw/main/assets/config-bills-number.png)
Los datos de energía y coste (energy_data.csv) y los de las facturas (billing_periods.csv) se almacenan en el directorio "user_files". Descárgalos antes de desinstalar la integración si la vas a reinstalar más adelante.
En el caso de tener datos de instalaciones previas, crea el directorio y añade los ficheros en él antes de añadir la integración

## Salida
Después de añadir y configuración la integración, se descargará automáticamente los datos desde:
* https://www.ufd.es: Consumos horarios de electricidad y periodos de facturación
* https://api.esios.ree.es: Precios horarios de la electricidad
* https://comparador.cnmc.gob.es/facturaluz/inicio: Simulaciones de las facturas

Tardará unos cuantos minutos en obtener todos los datos disponibles (alrededor de unos 2 años). Después de esto tendrás:
* Estadísticas
    * pvpc_energy:consumption (PVPC: Consumo): Consumos horarios de electricidad
    * pvpc_energy:cost (PVPC: Coste): Costes horarios de electricidad
* States
    * pvpc_energy.current_bill: Coste de la factura en curso. En el atributo "detail" se almacena un texto formateado con markdown con los datos de las últimas facturas para mostrar con Markdown Card.

## Paneles
Añade el consumo de la red al panel de energía:
* Elige un sensor que mida el consumo de la red en GJ, kWh, MJ, MWh, Wh.: "PVPC: Consumo"
* Usar una entidad que realiza un seguimiento de los costes totales: "PVPC: Coste"
![Grid consumption configuration](https://github.com/yinyang17/pvpc_energy/raw/main/assets/grid-consumption-configuration.png)

Añade a Lovelace un Markdown card para mostrar los datos de las últimas facturas:
```yml
{{ state_attr('pvpc_energy.current_bill', 'detail')}}
```
![Markdown card configuration](https://github.com/yinyang17/pvpc_energy/raw/main/assets/markdown-card-config.png)
