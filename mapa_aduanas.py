import pandas as pd
import folium
from folium.features import CustomIcon
from folium.plugins import MarkerCluster
import random
import json
import webbrowser

print("Construyendo proyecto para el control de inventario de los equipos no-intrusivos de ANAM")
print("                                  Noviembre 2025                                    ")
print("")
print("******************************************************************************************")
print("Equipo de Desarrollo de aplicativos de ANAM")
print("")
print("Rocio Acosta González")
print("Dulce María Ramírez Gómez")
print("Yanet Ramírez Flores")
print("Jaime Mojica Rodríguez")
print("******************************************************************************************")

# webbrowser.open('https://www.python.org')

#para manejarlo como un módulo:
def mapas():
   app = Flask(__name__)
  
mapa_principal_rmx = folium.Map(location=[23.634501,-102.552784], zoom_start=6)

marker_cluster = MarkerCluster().add_to(mapa_principal_rmx)

# Integrar en un arreglo JSON las ubicaciones y asignarles un Marcador en el Mapa:

puntos_ni = [
  {
    "id": 1,
    "type": 1,
    "name": "Acapulco, Gro.",
    "lat": 16.848700,
    "lng": -99.904961,
    "icon": "/img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 2,
    "type": 2,
    "name": "Altamira, Tamps.",
    "lat": 22.445620,
    "lng": -97.886726,
    "icon": "/img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "true",
    "img": "img/altamirad.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "277, 316 operaciones. Lugar 16° nacional. 3° en las aduanas marítimas"
      },
      {
        "title": "Recaudación (2018) :",
        "body": "34.4 mmdp. 8° lugar nacional. 6° en las aduanas marítimas"
      },
      {
        "title": "Observaciones:",
        "body": "En 2018 subió al 8° lugar nacional en recaudación."
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [16076.27, 14970.15, 17022.37, 21319.51, 24152.96, 30091.39, 34479.99]
      }
    ],
    "descripcion": "El proyecto tiene como objetivo, ampliar las áreas de importación, mediante la ubicación de carriles exclusivos para vehículos de carga regular y vehículos sobredimensionados en los cuales no habrá cruces entre estos y los vehículos ligeros, permitiendo que el flujo y la operación pueda realizarse de manera ágil. Lo anterior a través de una configuración y dimensiones adecuadas de carriles, patios de maniobras, plataformas y edificaciones, contando además con un almacén y plataforma de decomisos con el espacio apropiado. Este desarrollo se ubicará en un predio de más de 20 hectáreas puesto a disposición del SAT por la API a través de un convenio de colaboración."
  },
  {
    "id": 3,
    "type": 1,
    "name": "Cancún, Q.R.",
    "lat": 21.038069,
    "lng": -86.871582,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 4,
    "type": 1,
    "name": "Cd. del Carmen, Camp.",
    "lat": 18.650707,
    "lng": -91.839973,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 5,
    "type": 2,
    "name": "Coatzacoalcos, Ver.",
    "lat": 18.131287,
    "lng": -94.420204,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "true",
    "img": "img/coatzacoalcosd.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "10,091 operaciones.  Posición 39° a nivel nacional. Posición 11° en aduanas marítimas"
      },
      {
        "title": "Recaudación (2018) :",
        "body": "61.3 mmdp. Posición 6° a nivel nacional. Posición 5° en aduanas marítimas"
      },
      {
        "title": "Observaciones:",
        "body": "A pesar de tener la posición 39° a nivel nacional por número de operaciones es la sexta aduana que más recauda en el país."
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [2728.92,3193.88,3044.49,42792.35,54084.53,59461.88,61357.95]
      }
    ],
    "descripcion": "Debido a que el puerto de Coatzacoalcos, Veracruz, no cuenta con infraestructura aduanera para la revisión de mercancías de comercio exterior transportadas vía ferrocarril, es necesario dotarla con la siguiente infraestructura y equipamiento:<br><ul><li>Plataforma de reconocimiento para ferrocarril en 15 posiciones.</li><li>Equipos ERNI tipo rayos X carretero para Importación y exportación.</li><li>Equipos ERNI tipo rayos X ferroviario para Importación y exportación.</li><li>Oficinas administrativas y operativas.</li></ul>Adicionalmente, para satisfacer el incremento de las mercancías transportadas vía carretera en el puerto de Coatzacoalcos debido a la implementación del Corredor Transístmico se requiere reforzar la infraestructura y equipamiento existente en la Aduana."
  },
  {
    "id": 6,
    "type": 1,
    "name": "Dos Bocas, Tab.",
    "lat": 18.432581,
    "lng": -93.199326,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 7,
    "type": 1,
    "name": "Ensenada, B.C.",
    "lat": 31.856941,
    "lng": -116.634003,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 8,
    "type": 2,
    "name": "Guaymas, Son.",
    "lat": 27.924290,
    "lng": -110.886414,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "true",
    "img": "img/guaymasd.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "38,981 operaciones. Lugar 32° a nivel nacional. Lugar 8° en aduanas marítimas"
      },
      {
        "title": "Recaudación (2018) :",
        "body": "11,636.45 mdp. Lugar 21° a nivel nacional. 10° en aduanas marítimas"
      },
      {
        "title": "Observaciones:",
        "body": "De 2012 a 2018 pasó del lugar 37° al lugar 21° en materia de recaudación a nivel nacional"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [242.09,280.40,227.27,9335.82,7495.40,7701.72,11636.45]
      }
    ],
    "descripcion": "El proyecto considera una plataforma con cinco posiciones para tracto camiones, edificio administrativo desarrollado en planta baja y planta alta con alojamientos para verificadores (dormitorios para mujeres y hombres), área para resguardo de equipo de revisión no intrusiva, área para planta de emergencia, así como el confinamiento a todo lo largo de la ruta fiscal.<br>Con la finalidad de dar cumplimiento a los requerimientos actuales y dimensiones necesarias de la Aduana, la Administración Portuaria Integral (API), estará a cargo del proyecto ejecutivo y la construcción de la ampliación y modernización de la plataforma de importación y edificio administrativo."
  },
  {
    "id": 9,
    "type": 1,
    "name": "La Paz, B.C.S.",
    "lat": 24.161507,
    "lng": -110.318108,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 10,
    "type": 1,
    "name": "Lázaro Cárdenas, Mich.",
    "lat": 17.953913,
    "lng": -102.178299,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 11,
    "type": 2,
    "name": "Manzanillo, Col.",
    "lat": 19.074869,
    "lng": -104.285339,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "true",
    "img": "img/manzanillod.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "748,731 operaciones. Posición 7° a nivel nacional. Posición 1ª entre aduanas marítimas"
      },
      {
        "title": "Recaudación (2018) :",
        "body": "103.7 mmdp. Posición 2da a nivel nacional. Posición 1ª entre aduanas marítimas."
      },
      {
        "title": "Observaciones:",
        "body": "En 2018 Manzanillo subió a la 7° posición en operaciones a nivel nacional"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [36224.41,34746.51,42324.24,63876.93,73719.79,84854.10,103725.79]
      }
    ],
    "descripcion": "Debido al incremento del movimiento de las mercancías de comercio exterior que ha presentado el puerto de Manzanillo, la API tiene el proyecto de implementar la fase 02 de las instalaciones de importación de la Aduana de Manzanillo en la zona norte del puerto. Estas instalaciones contarán con la siguiente infraestructura y equipamiento:<ul><li>Ampliación de la plataforma de reconocimiento de importación en 10 posiciones.</li><li>Un equipo ERNI gamma carretero (importación).</li></ul>"
  },
  {
    "id": 12,
    "type": 2,
    "name": "Mazatlán, Sin.",
    "lat": 23.195091,
    "lng": -106.416801,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "true",
    "img": "img/mazatland.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "10,506 operaciones. Lugar 37° a nivel nacional. Lugar 10° en aduanas marítimas"
      },
      {
        "title": "Recaudación (2018) :",
        "body": "$22,033.45 mdp. Lugar 13° a nivel nacional. 8° en aduanas marítimas"
      },
      {
        "title": "Observaciones:",
        "body": "De 2012 a 2018 pasó del lugar 27° al lugar 13° en materia de recaudación a nivel nacional"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [586.71, 646.66, 748.88, 12979.98, 19619.95, 19531.72, 22033.45]
      }
    ],
    "descripcion": "Construir plataforma con cinco posiciones para mejorar las instalaciones y aprovechar eficientemente el espacio para evitar que la revisión sea ineficiente, ya que los tractocamiones se estacionan en el patio de maniobras y descargan la mercancía en piso, lo cual pone en riesgo la integridad del personal de la aduana y los operadores.<br>Beneficios:<ul><li>Incrementar y agilizar las revisiones en menor tiempo</li><li>Fortalecer la imagen institucional</li><li>Ofrecer seguridad al personal</li></ul> "
  },
  {
    "id": 13,
    "type": 1,
    "name": "Progreso, Yuc.",
    "lat": 21.286264,
    "lng": -89.664703,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 14,
    "type": 2,
    "name": "Salina Cruz, Oax.",
    "lat": 16.170885,
    "lng": -95.190117,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "true",
    "img": "img/salina_cruzd.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "274 operaciones. Lugar 48° a nivel nacional. Lugar 16° entre las aduanas marítimas"
      },
      {
        "title": "Recaudación (2018) :",
        "body": "1.2 mmdp. Lugar 35° a nivel nacional. Lugar 14!° entre las aduanas marítimas."
      },
      {
        "title": "Observaciones:",
        "body": "En 2018 pasó del lugar 48 al 35° a nivel nacional en materia de recaudación"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [496.15, 237.50, 271.38, 16.92, 0.33, 888.75, 1269.10]
      }
    ],
    "descripcion": "Debido a que el puerto de Salina Cruz, Oaxaca, no cuenta con infraestructura aduanera para la revisión de mercancías de comercio exterior transportadas vía ferrocarril, es necesario dotarla con la siguiente infraestructura y equipamiento:<ul><li>Plataforma de reconocimiento para ferrocarril en 15 posiciones.</li><li>Equipos ERNI tipo rayos X carretero para Importación y exportación.</li><li>Equipos ERNI tipo rayos X ferroviario para Importación y exportación.</li><li>Oficinas administrativas y operativas.</li></ul>Adicionalmente, para satisfacer el incremento de las mercancías transportadas vía carretera en el puerto de Salina Cruz debido a la implementación del Corredor Transístmico se requiere reforzar la infraestructura y equipamiento existente en la Aduana."
  },
  {
    "id": 15,
    "type": 1,
    "name": "Tampico, Tamps.",
    "lat": 22.214836,
    "lng": -97.868813,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 16,
    "type": 1,
    "name": "Tuxpan, Ver.",
    "lat": 20.968172,
    "lng": -97.323860,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 17,
    "type": 1,
    "name": "Veracruz, Ver.",
    "lat": 19.214764,
    "lng": -96.154152,
    "icon": "img/icono_maritima.png",
    "tipo": "Maritima",
    "visible": "false"
  },
  {
    "id": 18,
    "type": 1,
    "name": "Agua Prieta, Son.",
    "unidad": 879,
    "lat": 31.333660,
    "lng": -109.560532,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 19,
    "type": 1,
    "name": "Cd. Acuña, Coah.",
    "unidad": 822,
    "lat": 29.325432,
    "lng": -100.929070,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 20,
    "type": 1,
    "name": "Cd. Camargo, Tamps.",
    "unidad": 888,
    "lat": 26.362514,
    "lng": -98.806419,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "true"
  },
  {
    "id": 21,
    "type": 1,
    "name": "Cd. Juárez, Chih.",
    "unidad": 830,
    "lat": 31.762089,
    "lng": -106.453110,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "true"
  },
  {
    "id": 22,
    "type": 1,
    "name": "Cd. Miguel Alemán, Tamps.",
    "unidad": 886,
    "lat": 26.402657,
    "lng": -99.020996,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 23,
    "type": 1,
    "name": "Cd. Reynosa, Tamps.",
    "unidad": 887,
    "lat": 26.040724,
    "lng": -98.210716,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 24,
    "type": 1,
    "name": "Colombia, N.L.",
    "unidad": 861,
    "lat": 27.697836,
    "lng": -99.748932,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 25,
    "type": 1,
    "name": "Matamoros, Tamps.",
    "unidad": 884,
    "lat": 25.871889,
    "lng": -97.475830,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 26,
    "type": 2,
    "name": "Mexicali, B.C.",
    "unidad": 813,
    "lat": 32.664536,
    "lng": -115.496269,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "true",
    "img": "img/mexicalid.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "608,099 operaciones. Lugar 12° a nivel nacional. Lugar 8° en aduanas de la frontera norte"
      },
      {
        "title": "Recaudación (2018) :",
        "body": "$8,760.45 mdp. Lugar 25° a nivel nacional. 9° en aduanas de la frontera norte"
      },
      {
        "title": "Observaciones:",
        "body": "De 2012 a 2018 pasó del lugar 20° al lugar 25° en materia de recaudación a nivel nacional"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [3965.34, 4201.79, 4729.89, 6453.4, 7896.47, 8079.88, 8760.45]
      }
    ],
    "descripcion": "Se considera la ampliación del área de importación en la Aduana de Mexicali II, las instalaciones actuales no cumplen con las necesidades de operación ya que la plataforma de revisión no tiene las dimensiones adecuadas, lo que obliga a ocupar 2 o más posiciones al momento de realizar la revisión de mercancías, las instalaciones son obsoletas, se encuentran en condiciones deficientes y no corresponde con la imagen actual de las Aduanas.<br><br>El proyecto considera 10 carriles de entrada (1 Vacíos, 1 Express, 6 Carga, 1 Sobredimensionados, 1 Ligeros), 7 carriles de salida (1 Vacíos, 1 Express, 1 Sobredimensionados, 3 Carga), Plataforma con 39 posiciones, Edificio Administrativo en un nivel, Unidad Canina para 8 sensores, Subestación eléctrica, Área de basura y Planta de tratamiento."
  },
  {
    "id": 27,
    "type": 1,
    "name": "Naco, Son.",
    "unidad": 880,
    "lat": 31.333790,
    "lng": -109.948257,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 28,
    "type": 1,
    "name": "Nogales, Son",
    "unidad": 878,
    "lat": 31.332157,
    "lng": -110.943398,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 29,
    "type": 2,
    "name": "Nuevo Laredo, Tamps.",
    "unidad": 885,
    "lat": 27.595783,
    "lng": -99.545013,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "true",
    "img": "img/nuevo_laredod.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "4, 396, 907 operaciones. 1er lugar nacional. 1er lugar entre las aduanas de la frontera norte"
      },
      {
        "title": "Recaudación (2018) :",
        "body": "133.7 mmdp. 1er lugar nacional. 1er lugar entre las aduanas de la frontera norte."
      },
      {
        "title": "Cruces:",
        "body": ""
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [75888.29, 74968.81, 82138.05, 102408.78, 107765.60, 111761.21, 133702.01]
      }
    ],
    "descripcion": "Adecuar las vialidades del Puente III de la Aduana de Nuevo Laredo, con el fin de mejorar el tráfico y agilizar la operación en las rutas de importación y exportación. Dentro de los alcances se contemplan las siguientes obras:<ul><li>Nuevas oficinas del Fideicomiso</li><li>Construcción del tanque elevado y cisterna</li><li>Adecuación de Red hidráulica y sanitaria</li><li>Planta tratadora de aguas residuales</li><li>Mejoramiento de jardinería e implementación de sistema automatizado de riego</li><li>Caseta de revisión de acceso peatonal de importación</li><li>Andador peatonal confinado en importación </li><li>Remozamiento de plataformas de los andenes de revisión de importación y exportación</li><li>Adecuación de accesos y estacionamientos de visitantes y personal</li><li>Construcción del carril 5 para exportación</li><li>Reubicación de Rayos Gamma en exportación y acondicionamiento de vialidad</li><li>Reubicación de equipos RNI y acondicionamiento de vialidad</li><li>Adecuación de carriles de salida de importación</li><li>Ampliación de carriles de salida para el área de amortiguamiento de carga para exportación</li><li>Portones en ingreso y salida de importación y exportación, así como mantenimiento de los existentes</li><li>Señalización interior – exterior (vertical y horizontal)</li><li>Ampliación de cuarto de Máquinas para TI</li><li>Diagnostico eléctrico, levantamiento de necesidades para luminarias, instalación de Planta de emergencia e implementación del proyecto </li><li>Cambio de confinamiento de malla ciclónica por tubular</li><li>Construcción del carril de vacíos y colocación de poncha llantas</li><li>Construcción de cámaras refrigeradas</li><li>Construcción de bahías para carriles de vacíos</li><li>Confinamiento de vialidades en importación y exportación</li><li>Habilitación de áreas de maniobras y posiciones para revisión de RNI</li><li>Implementación de red pluvial</li><li>Recuperación del sistema de protección de pararrayos</li></ul>"
  },
  {
    "id": 30,
    "type": 1,
    "name": "Ojinaga, Chih.",
    "unidad": 833,
    "lat": 29.561005,
    "lng": -104.397728,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "true"
  },
  {
    "id": 31,
    "type": 1,
    "name": "Piedras Negras, Coah.",
    "unidad": 821,
    "lat": 28.697304,
    "lng": -100.513008,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 32,
    "type": 1,
    "name": "Puerto Palomas, Chih.",
    "unidad": 831,
    "lat": 31.783478,
    "lng": -107.627632,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 33,
    "type": 2,
    "name": "San Luis Río Colorado, Son.",
    "unidad": 814,
    "lat": 32.484734,
    "lng": -114.782776,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "true",
    "img": "img/san_luisd.png",
    "estadisticas": [
      {
        "title": "Operaciones Aduana de San Luis Río Colorado (2018):",
        "body": "42,626 operaciones. Lugar 31° a nivel nacional.  Lugar 14° en aduanas de la frontera norte"
      },
      {
        "title": "Recaudación Aduana de San Luis Río Colorado (2018) :",
        "body": "348 mdp. Lugar 40° a nivel nacional. Posición 15° en aduanas de la frontera norte."
      },
      {
        "title": "Observaciones:",
        "body": "La aduana se encuentra inmersa en la ciudad de San Luis Río Colorado."
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [280.70, 246.85, 271.39, 243.92, 278.24, 229.42, 348.20]
      }
    ],
    "descripcion": "Las instalaciones de la Aduana se encuentran saturadas y han sido absorbidas por la mancha urbana, por lo que no se cuenta con área disponible para llevar a cabo un reordenamiento.<br><br>A pesar de la insistencia por parte de CBP y demás autoridades americanas de llevar a cabo un reordenamiento en el Puente I, México propone que el Puente II sea habilitado para el cruce de vehículos ligeros.<br><br><b>Avance de obra: </b>En planeación<ul><li>Continuar con la coordinación entre dependencias, Gobierno del Estado y municipio para realizar un proyecto de Reordenamiento y ampliación en San Luis Rio Colorado I, así como ver su factibilidad.</li></ul>"
  },
  {
    "id": 34,
    "type": 1,
    "name": "Sonoyta, Son.",
    "unidad": 815,
    "lat": 31.879677,
    "lng": -112.817574,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 35,
    "type": 2,
    "name": "Tecate, B.C.",
    "unidad": 817,
    "lat": 32.575947,
    "lng": -116.627747,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "true",
    "img": "img/tecated.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "72,401 operaciones. Lugar 26° a nivel nacional. Lugar 11° en aduanas de la frontera norte"
      },
      {
        "title": "Recaudación (2018) :",
        "body": "23.35 mdp. Lugar 42° a nivel nacional. 16° en aduanas de la frontera norte"
      },
      {
        "title": "Observaciones:",
        "body": "De 2012 a 2018 pasó del lugar 38° al lugar 42° en materia de recaudación a nivel nacional"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [211.63, 231.45, 238.42, 251.61, 260.47, 262.32, 233.35]
      }
    ],
    "descripcion": "Reordenar, ampliar y modernizar las áreas de importación, exportación, vehículos ligeros y peatones en la aduana de Tecate en Baja California, en un predio de 7.1 hectáreas, para facilitar el despacho aduanero y agilizar el cruce de mercancías, vehículos y personas."
  },
  {
    "id": 36,
    "type": 1,
    "name": "Tijuana, B.C.",
    "unidad": 816,
    "lat": 32.541397,
    "lng": -117.028397,
    "icon": "img/icono_norte.png",
    "tipo": "Norte",
    "visible": "false"
  },
  {
    "id": 37,
    "type": 1,
    "name": "Cd. Hidalgo, Chis.",
    "unidad": 829,
    "lat": 14.711716,
    "lng": -92.154610,
    "icon": "img/icono_sur.png",
    "tipo": "Sur",
    "visible": "false"
  },
  {
    "id": 38,
    "type": 2,
    "name": "Subteniente López, Q.R.",
    "unidad": 870,
    "lat": 18.492744,
    "lng": -88.395500,
    "icon": "img/icono_sur.png",
    "tipo": "Sur",
    "visible": "true",
    "img": "img/subteniente_lopezd.png",
    "estadisticas": [
      {
        "title": "Operaciones (2018):",
        "body": "10,387 operaciones Lugar 38 a nivel nacional. Lugar 18 en las aduanas de la frontera."
      },
      {
        "title": "Recaudación (2018) :",
        "body": "$9.15 mdp Lugar 48 a nivel nacional,  20 en las aduanas fronterizas."
      },
      {
        "title": "Observaciones:",
        "body": "De 2012 a 2018 la recaudación bruta por este punto ha tendido a la baja, en este periodo ha disminuido en 75.53%, pasando de $37,391 mdp a $9. 15 mdp"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [39.39, 32.19, 21.54, 21.21, 12.12, 6.08, 9.15]
      }
    ],
    "descripcion": "Dotar de infraestructura suficiente y necesaria para satisfacer las necesidades actuales de funcionalidad y operación de la propia aduana, con el fin de optimizar la operación y homologar la imagen institucional.<br><br>Considera las siguientes instalaciones:<ul><li>Edificio Administrativo SAT.</li><li>Migración.</li><li>Unidad Canina.</li><li>Alojamiento para OCE.</li><li>Almacén de decomisos.</li><li>Almacén CERYS.</li><li>SENASICA.</li><li>Alojamiento para SEDENA.</li><li>Equipamiento:<ul><li>Equipo de rayos x para revisión de equipaje (2).</li></ul></li></ul>"
  },
  {
    "id": 39,
    "type": 1,
    "name": "Aeropuerto Int. de la Cd. de México, D.F.",
    "unidad": 839,
    "lat": 19.442707,
    "lng": -99.071732,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "false"
  },
  {
    "id": 40,
    "type": 1,
    "name": "Aguascalientes, Ags.",
    "unidad": 811,
    "lat": 21.845087,
    "lng": -102.291771,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "false"
  },
  {
    "id": 41,
    "type": 1,
    "name": "Chihuahua, Chih.",
    "unidad": 832,
    "lat": 28.713673,
    "lng": -106.100769,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "true"
  },
  {
    "id": 42,
    "type": 1,
    "name": "Guadalajara, Jal.",
    "unidad": 848,
    "lat": 20.524729,
    "lng": -103.298523,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "false"
  },
  {
    "id": 43,
    "type": 1,
    "name": "Guanajuato, Gto.",
    "unidad": 840,
    "lat": 21.008961,
    "lng": -101.509834,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "false"
  },
  {
    "id": 44,
    "type": 1,
    "name": "México, D.F.",
    "unidad": 835,
    "lat": 19.474346,
    "lng": -99.165749,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "false"
  },
  {
    "id": 45,
    "type": 1,
    "name": "Monterrey, N.L.",
    "unidad": 859,
    "lat": 25.807175,
    "lng": -100.295731,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "false"
  },
  {
    "id": 46,
    "type": 1,
    "name": "Puebla, Pue.",
    "unidad": 866,
    "lat": 19.072258,
    "lng": -98.160446,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "false"
  },
  {
    "id": 47,
    "type": 1,
    "name": "Querétaro, Qro.",
    "unidad": 867,
    "lat": 20.615021,
    "lng": -100.427032,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "true"
  },
  {
    "id": 48,
    "type": 1,
    "name": "Toluca, Méx.",
    "unidad": 853,
    "lat": 19.337385,
    "lng": -99.570641,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "false"
  },
  {
    "id": 49,
    "type": 1,
    "name": "Torreón, Coah.",
    "unidad": 824,
    "lat": 25.550032,
    "lng": -103.397118,
    "icon": "img/icono_interior.png",
    "tipo": "Interior",
    "visible": "false"
  },
  {
    "id": 50,
    "type": 3,
    "name": "Academia Canina de Atención Integral (ACAI), Chichimequillas. Querétaro.",
    "unidad": 0,
    "lat": 20.757650,
    "lng": -100.315825,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "false",
    "descripcion": "Reabastecimiento a la Academia Canina con la infraestructura necesaria, mobiliario, insumos y servicios para el resguardo y/o atención de los semovientes que en conjunto permitan optimizar su labor operativa y así contribuir al cumplimiento de los objetivos y metas institucionales.<br><br>Considera las siguientes instalaciones:<br><br>Unidad canina.<ul><li>Estancias caninas - 100 sensores.</li> <li>Estancias caninas - 10 infecciosos.</li>  <li>Área de almacenaje y preparación de alimentos.</li> <li>Área de esparcimiento.</li> <li>Campo de agilidad.</li></ul>Unidad Médico Veterinaria.<ul>  <li>1 Quirófano.</li> <li>1 Cuarto de radiología y revelado.</li> <li>3 Consultorios.</li>  <li>2 dormitorios dobles para médicos.</li> <li>Módulo de baños con vestidor.</li>  <li>Área de recuperación con 12 jaulas.</li>  <li>Área de lavado y esterilización.</li> <li>Bodega de medicamentos (farmacia).</li><li>Área de rehabilitación.</li>  <li>Laboratorio.</li> <li>Almacén y cuarto de aseo.</li></ul>Equipamiento Unidad Canina.<ul>  <li>Campo de agilidad.</li> <ul>    <li>Cerca de salto.</li>    <li>Vallas de salto.</li>   <li>Ventana de salto.</li>    <li>Túnel de arrastre.</li>   <li>Plataformas para escalar.</li>  </ul></ul>Equipamiento Unidad Médico Veterinaria.<ul> <li>Equipo de Rayos X.</li> <li>Mesa de quirófano.</li> <li>Unidad ultrasónica dental.</li> <li>Aspirador médico.</li>  <li>Báscula digital veterinaria.</li> <li>Electro cauterizador.</li>  <li>Máquina de anestesia.</li>  <li>Tripie quirúrgico.</li> <li>Tina hidroterapia.</li> <li>Termómetro infrarrojo.</li> <li>Nebulizador.</li> <li>Camilla plegable.</li></ul>"
  },
  {
    "id": 51,
    "type": 2,
    "name": "Cruce Alzaldúas",
    "unidad": 0,
    "lat": 26.111386,
    "lng": -98.333681,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "img": "img/cruce_alzalduasd.png",
    "estadisticas": [
      {
        "title": "Operaciones Aduana de Reynosa (2018):",
        "body": "1,137,895 operaciones. 5° lugar nacional. 4° entre las aduanas de la frontera norte."
      },
      {
        "title": "Recaudación Aduana de Reynosa (2018):",
        "body": "21.2 mmdp. 14° lugar nacional. 5° entre las aduanas de la frontera norte."
      },
      {
        "title": "Observaciones:",
        "body": "En 2017 subió al 14° lugar nacional en recaudación."
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [9049.93,7803.99,9036.85,13721.20,14708.58,18336.31,21219.5]
      }
    ],
    "descripcion": "Existe un proyecto para la construcción de instalaciones de revisión de carga, el cual fue retomado por la Dirección de Proyectos Intermodales de la SCT y el propio concesionario (MarHnos), en la reunión conjunta con los Alcaldes de las ciudades de Mission y McAllen, TX., realizada el pasado 5/marzo/2019.<br><br>Una vez definida la propuesta conceptual, con los cambios y ajustes necesarios para incluir la inspección conjunta que se ha acordado con la CBP americana, se programara una revisión conjunta con la SCT y las Dependencias que requieran presencia en el punto.<br><br>Con lo anterior, se desarrollaría el proyecto ejecutivo el cual definiría la inversión requerida y su programa de ejecución."
  },
  {
    "id": 52,
    "type": 2,
    "name": "Centro de Atención Integral al Tránsito Fronterizo (CAITF) Frontera, Tabasco",
    "unidad": 0,
    "lat": 18.540883,
    "lng": -92.637381,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "img": "img/Centro_de_Atenciond.png",
    "estadisticas": [
      {
        "title": "Operaciones totales Frontera Sur  2018:",
        "body": "189,675 operaciones por la frontera sur, equivalentes al 1.02% del total."
      },
      {
        "title": "Recaudación Frontera Sur 2018 :",
        "body": "$1,445.84 mdp por la frontera sur, equivalentes al .15% del total."
      },
      {
        "title": "Observaciones:",
        "body": "De 2012 a 2018 la recaudación bruta a nivel nacional, se ha incrementado en 52.47%, pasando de $948.30 mdp a $1,445.84 mdp"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [948.30,831.66,916.03,1094.65,1244.09,1349.08,1445.84]
      }
    ],
    "descripcion": "El Centro de Atención Integral al Tránsito Fronterizo (CAITF) Frontera, Tabasco, permitirá a distintas dependencias federales, la revisión de flujos de personas, mercancías y vehículos que se internan al país desde la frontera sur; es el cuarto en su tipo en el país. Este centro tiene la misión de reforzar la seguridad y control de la franja sur del país, antes del Itsmo de Tehuantepec.; lo anterior apoyará a mitigar el problema del tráfico ilegal de personas, mercancías y vehículos.<br><br>Considera las siguientes instalaciones:<ul><li>Instalaciones para el SAT.<ul><li>Dormitorios para personal.</li><li>Plataforma de reconocimiento aduanero (5 posiciones).</li><li>Módulos de selección automatizada para carga (2).</li><li>Unidad técnica administrativa de muestreo.</li><li>Unidad canina.</li><li>Área de revisión de autobuses (2).</li><li>Oficinas administrativas y operativas.</li><li>Módulo de Autodeclaración.</li><li>Área de revisión de pasajeros.</li><li>Módulos de selección automatizada para ligeros (4).</li><li>Revisión de ligeros (10 bahías).</li><li>Área de monitoreo.</li><li>Áreas de decomisos.</li></ul></li><li>Estancia migratoria, dormitorio para personal.</li><li>BANJERCITO.</li><li>SEDENA. - Alojamiento para personal.</li><li>Policía Federa. - Área de revisión, oficinas y dormitorios.</li><li>INDAABIN. – Oficinas.</li><li>Casetas de control de ingreso y salida, vialidad, estacionamientos, plaza cívica, plataforma de aterrizaje, canchas deportivas, casetas de control de ingreso.</li><li>Equipamiento.<ul><li>Equipo de rayos X para revisión de equipaje (2).</li><li>Equipos de revisión no intrusiva tipo gamma (1).</li></ul></li></ul>"
  },
  {
    "id": 53,
    "type": 2,
    "name": "Centro de Atención Integral al Tránsito Fronterizo (CAITF) Palenque, Chiapas.",
    "unidad": 0,
    "lat": 17.439225,
    "lng": -91.940725,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "img": "img/Centro_de_Atencion_Integrald.png",
    "estadisticas": [
      {
        "title": "Operaciones totales Frontera Sur  2018:",
        "body": "189,675 operaciones por la frontera sur, equivalentes al 1.02% del total. "
      },
      {
        "title": "Recaudación Frontera Sur  2018 :",
        "body": "$1,445.84 mdp por la frontera sur, equivalentes al .15% del total."
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [948.30,831.66,916.03,1094.65,1244.09,1349.08,1445.84]
      }
    ],
    "descripcion": "El Centro de Atención Integral al Tránsito Fronterizo (CAITF) Palenque, Chiapas, permitirá a distintas dependencias federales, la revisión de flujos de personas, mercancías y vehículos que se internan al país desde la frontera sur; es el cuarto en su tipo en el país. Este centro tiene la misión de reforzar la seguridad y control de la franja sur del país, antes del Itsmo de Tehuantepec.; lo anterior apoyará a mitigar el problema del tráfico ilegal de personas, mercancías y vehículos.<br><br>Considera las siguientes instalaciones:<ul><li>Instalaciones para el SAT.<ul><li>Dormitorios para personal.</li><li>Plataforma de reconocimiento aduanero (4 posiciones).</li><li>Módulos de selección automatizada para carga (2).</li><li>Edificio de reconocimiento de carga.</li><li>Unidad técnica administrativa de muestreo.</li><li>Unidad canina.</li><li>Área de revisión de autobuses (2).</li><li>Oficinas administrativas y operativas.</li><li>Módulo de Autodeclaración.</li><li>Área de revisión de pasajeros.</li><li>Módulos de selección automatizada para ligeros (2).</li><li>Revisión de ligeros (6 bahías).</li><li>Área de monitoreo.</li></ul></li><li>Migración. - Oficinas, Estancia migratoria, dormitorio para personal.</li><li>Banjercito. - Oficinas.</li><li>SEDENA. - Alojamiento para personal.</li><li>Policía Federa. - Área de revisión, oficinas y dormitorios.</li><li>INDAABIN. – Oficinas.</li><li>Casetas de control de ingreso y salida. – Vialidad, estacionamientos, Plaza Cívica, Comedor comunitario.</li><li>Equipamiento.<ul><li>Equipo de rayos X para revisión de equipaje (2).</li><li>Equipos de revisión no intrusiva tipo gamma (1).</li></ul></li></ul>"
  },
  {
    "id": 54,
    "type": 2,
    "name": "Modernización del Puente Córdova, Ciudad Juárez",
    "unidad": 0,
    "lat": 31.763108,
    "lng": -106.451881,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "img": "img/Puente_Cordovad.png",
    "estadisticas": [
      {
        "title": "Operaciones Aduana Ciudad Juárez (2018):",
        "body": "1, 692, 720 operaciones. 3er lugar a nivel nacional y 2do para las aduanas de la frontera norte."
      },
      {
        "title": "Recaudación Aduana Ciudad Juárez  (2018}:",
        "body": "31.9 mmdp. 9° lugar a nivel nacional y 2do en las aduanas de la frontera norte."
      },
      {
        "title": "Observaciones:",
        "body": "En 2018 subió al 9° lugar nacional por número de operaciones."
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [8112.94,7827.34,9283.35,26968.61,31443.31,29649.30,31907.58]
      }
    ],
    "descripcion": "<b>Proyecto:</b> Modernización del Puente Córdova<br><br>Área total del predio: 19.5 ha<br><br><b>Objetivo:</b> Reordenar y ampliar las instalaciones de la Aduana, para atender la creciente demanda para asegurar que el personal de la AGA realice revisiones de manera ágil, oportuna y conforme a la ley a través de la infraestructura adecuada a las nuevas necesidades de comercio.<br><br><b>Componentes del Proyecto:</b><br>El proyecto fue elaborado por la empresa Muzquiz y Asociados en el año 2009 por lo que requiere una actualización de acuerdo a los nuevos esquemas de revisión de mercancías, al aumento de la demanda en el puerto fronterizo y la implementación se nuevos sistemas y tecnologías en las aduanas."
  },
  {
    "id": 55,
    "type": 3,
    "name": "Delegación la AGA/Instituto de Capacitación Aduanera",
    "unidad": 0,
    "lat": 27.488696,
    "lng": -99.516528,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "descripcion": "Para la edificación de la sede la AGA, se propone utilizar el predio y edificaciones interiores de la Antigua Aduana de Nuevo Laredo, rescatando seis edificios con valor histórico, así como la reutilización o demolición de 11 edificaciones, que no tienen valor histórico, y que rompen con el conjunto original. <br><br>El estacionamiento del antiguo CIITEV, cuenta con un área aproximada de 13,320 m2 y es perfectamente apto para el desarrollo de la delegación.<br><br>En este predio requiere inversiones iniciales de rescate y restauración, debido a su valor histórico y estado físico. <br><br>Existen dos predios para posible integración al conjunto de la Antigua Aduana, estos predios aumentan el potencial de desarrollo. La propuesta está basada en el ofrecimiento de donación por parte del Secretario de Desarrollo Económico del municipio de Nuevo Laredo, estos son el edificio de la Agencia Aduanal Montemayor y las instalaciones de una compañía transportista.<br><br>Delegación de oficinas Centrales de la AGA <ul><li>Alojamientos seguros para todo el personal asignado durante el periodo</li><li>Áreas de atención al público</li><li>Áreas de esparcimiento</li><li>Área de servicios alojamientos</li><li>Servicios generales</li><li>Servicios de comunicación</li><li>Servicios administrativos</li><li>Helipuerto</li><li>Estacionamiento</li></ul><br><br>Instituto de Capacitación Aduanera y Comercio exterior<ul><li>Área administrativa</li><li>Área para aulas</li><li>Auditorio</li><li>Biblioteca</li><li>Estacionamiento vehicular (interno-visitas)</li><li>Área de servicios</li></ul><br>Trabajos adicionales de mejoras <ul><li>Reubicación del archivo dentro del conjunto de la Antigua Aduana</li></ul>Todos estos trabajos manteniendo la vocación de esta zona como un espacio cultural, revisando la posibilidad de incluir dentro del conjunto un Museo de la Aduana Mexicana"
  },
  {
    "id": 56,
    "type": 2,
    "name": "Sección Aduanera en la estación de ferrocarril de Ojinaga-línea Q. Ojinaga-Topolobampo",
    "unidad": 0,
    "lat": 29.542144,
    "lng": -104.377503,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "img": "img/ferrocarril_de_Ojinagad.png",
    "estadisticas": [
      {
        "title": "Operaciones totales 2018:",
        "body": "11,433 operaciones. Lugar 36° a nivel nacional. Lugar 16° en aduanas de la frontera norte"
      },
      {
        "title": "Recaudación 2018 :",
        "body": "$142.82 mdp. Lugar 44° a nivel nacional. 17° en aduanas de la frontera norte"
      },
      {
        "title": "Observaciones:",
        "body": "De 2012 a 2018 pasó del lugar 42° al lugar 44° en materia de recaudación a nivel nacional"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [103.17,133.95,140.58,110.36,110.52,110.29,142.82]
      }
    ],
    "descripcion": "Construcción de Sección Aduanera en la estación de ferrocarril de Ojinaga que contará con oficinas de la Aduana de Ojinaga con un Jefe de Sección y dos operativos, IDF, cuarto de monitoreo, área para PITA, sanitarios, cocineta y cuarto de aseo."
  },
  {
    "id": 57,
    "type": 3,
    "name": "Instalaciones de Entrenamiento Especializado",
    "unidad": 0,
    "lat": 20.757730,
    "lng": -100.315546,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "descripcion": "Construcción de instalaciones de entrenamiento especializado en el manejo de armas de fuego para el personal que labora en la Administración General de Aduanas. Se propone la construcción en cada una de las aduanas del país, exentando aquellas que por su ubicación y/o dimensiones sea posible la construcción para el uso de dos o más aduanas.<br><br>Existen tres tipos de instalaciones, las cuales serán ubicadas en las aduanas de acuerdo a las características que mejor se adapten, tomando en cuenta las limitantes de espacio, operativas, así como la cantidad de personal que deberá de hacer uso de las mismas.<br><br>Las opciones disponibles son:<ul><li>Galería de tiro cerrada: Edificación con carriles modulares de 4, 6 y 8 líneas de tiro, cuenta con área de recepción, sanitarios, armero, líneas de tiro, bodega, cuarto de máquinas y equipamiento automatizado de blancos</li><li>Galería de tiro tipo contenedor: Estructura semifija con capacidad para dos líneas de tiro</li><li>Galería de tiro virtual: Equipamiento tecnológico con la capacidad para simulación para el entrenamiento de personal</li></ul>"
  },
  {
    "id": 58,
    "type": 3,
    "name": "Instituto de Capacitación Aduanera y de Comercio Exterior, Campus Ciudad de México.",
    "unidad": 0,
    "lat": 19.743194,
    "lng": -99.000456,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "descripcion": "Contar con infraestructura necesaria para la capacitación y formación del personal operativo de las aduanas del país.<br>Considera las siguientes instalaciones:<ul><li>Aulas de capacitación.</li><li>Auditorio.</li><li>Salas de juntas.</li><li>Salón de capacitadores.</li><li>Biblioteca.</li><li>Área de estudio.</li><li>Comedor.</li><li>Sanitarios.</li><li>Estancia/Vestíbulos.</li><li>Área administrativa.</li><li>Control de acceso.</li><li>Áreas verdes.</li><li>Cuarto de máquinas.</li></ul>"
  },
  {
    "id": 59,
    "type": 2,
    "name": "Modernización de la Aduana de Camargo",
    "unidad": 0,
    "lat":  26.362514,
    "lng": -98.806419,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "img": '<table class="table table-hover table-sm"><thead class="text-center" style="color: #FFF; background-color: #7e0308;"><tr><th colspan="4">CD. CAMARGO</th></tr></thead><tbody><tr><th>2012</th><td>25,343.10</td><th>*2019</th><td>25,343.10</td></tr><tr><th>2013</th><td>25,343.10</td><th>*2020</th><td>25,343.10</td></tr><tr><th>2014</th><td>25,343.10</td><th>*2021</th><td>25,343.10</td></tr><tr><th>2015</th><td>25,343.10</td><th>*2022</th><td>25,343.10</td></tr><tr><th>2016</th><td>25,343.10</td><th>*2023</th><td>25,343.10</td></tr><tr><th>2017</th><td>25,343.10</td><th>*2024</th><td>25,343.10</td></tr><tr><th>2018</th><td>25,343.10</td></tr></tbody></table>',
    "estadisticas": [
      {
        "title": "Operaciones totales 2018:",
        "body": "66, 954 operaciones. Lugar 28° a nivel nacional. Lugar 12° en aduanas de la frontera norte"
      },
      {
        "title": "Recaudación 2018 :",
        "body": "9.93 mmdp. Lugar 24° a nivel nacional. 8° en aduanas de la frontera norte"
      },
      {
        "title": "Observaciones:",
        "body": "De 2015 a 2019 pasó del lugar 29° al lugar 24° en materia de recaudación a nivel nacional"
      }
    ],
    "tendencia": [
      {
        "title": "Tendencia de recaudación 2018-2024(millones de pesos)",
        "label": "Tendencia de recaudación",
        "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
        "data": [109.93, 100.19, 94.63, 2274.56, 4787.55, 7425.38, 9993.62]
      }
    ],
    "descripcion": "Con el desarrollo de este proyecto se ampliará la capacidad de operación de la aduana y dotar con infraestructura adecuada, enfocando la prioridad a la zona de importación derivado a la posible implementación de la inspección conjunta, que se revisa con CBP, y con ello se elimina la infraestructura para la exportación.  <br><br>Dentro de los alcances del proyecto se pretende habilitar un carril de carga extraordinaria para el cruce de aspas de aerogeneradores e hidrocarburos, así como el reordenamiento general de la aduana y su ruta fiscal, con una actualización de las edificaciones administrativas, para la seguridad y alojamientos para sedeña."
  },
  {
    "id": 60,
    "type": 3,
    "name": "Elaboración de seis proyectos ejecutivos en aduanas",
    "unidad": 0,
    "lat": 0,
    "lng": 0,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "descripcion": "La Administración General de Aduanas en la misión de contribuir al crecimiento en el país mediante una eficaz operación aduanera que facilite el movimiento de mercancías, pasajeros y vehículos, fortaleciendo la seguridad nacional, realiza diversos esfuerzos enfocados a la mejora de condiciones en las instalaciones aduaneras, así como la actualización del equipamiento existente.<br><br>Por lo anterior, detectando diversos puntos de atención donde la infraestructura es obsoleta o insuficiente para llevar a cabo el despacho aduanero, afectando directamente a la calidad de atención, se propone la elaboración de 6 proyectos ejecutivos, los cuales permitirán en el mediano plazo una mejora en el servicio prestado por esta Administración General.<br><br>Algunos de los puntos a resolver son:<ul><li>Problemas de saturación</li><li>Aduanas rodeadas por la mancha urbana </li><li>Infraestructura inadecuada para el despacho aduanero</li><li>Infraestructura obsoleta en relación al esquema actual de operación</li><li>Homologación de infraestructura </li><li>Integración regional ineficiente</li><li>Equipamiento tecnológico insuficiente</li></ul>"
  },
  {
    "id": 61,
    "type": 3,
    "name": "Nuevas instalaciones para la autoridad aduanera en Puerto Chiapas",
    "unidad": 0,
    "lat": 0,
    "lng": 0,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "descripcion": "Nuevas instalaciones para la autoridad aduanera en Puerto Chiapas"
  },
  {
    "id": 62,
    "type": 3,
    "name": "Cruce Río Bravo-Donna",
    "unidad": 0,
    "lat": 0,
    "lng": 0,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "descripcion": "Cruce Río Bravo-Donna"
  },
  {
    "id": 63,
    "type": 3,
    "name": "Servicio de Equipamiento No Intrusivo",
    "unidad": 0,
    "lat": 0,
    "lng": 0,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "descripcion": "Servicio de Equipamiento No Intrusivo"
  },
  {
    "id": 64,
    "type": 3,
    "name": "Nuevas instalaciones para la autoridad aduanera en el Aeropuerto Internacional de Santa Lucia",
    "unidad": 0,
    "lat": 0,
    "lng": 0,
    "icon": "img/icono_estrella.png",
    "tipo": "Otros",
    "visible": "true",
    "descripcion": "Nuevas instalaciones para la autoridad aduanera en el Aeropuerto Internacional de Santa Lucia"
  }
]

"""
#primera versión iterada:
for punto in puntos_ni:

    folium.Marker(
        #location=punto["coordenadas"],
        location=[punto[lat,lng],
        #location=([row['lat'], row['lng']),
        popup=punto['name']  # El texto que se muestra al hacer clic
        # tooltip=f"Visita: {punto['nombre']}" # El texto que se muestra al pasar el cursor

    ).add_to(mapa_principal)
"""

# Segunda versión a iterar el JSON de la ubicaciones&datos, ya con la utilería JSON en el proyecto:
for punto in puntos_ni:
   # Extraer las coordenadas del punto táctico para marcalas en el mapa
   # Extraer otros datos relevantes
   latitud = punto['lat']
   longitud = punto['lng']
   nombre = punto['name']

   #icono='cloud'
   #icono = CustomIcon(icon_image=(punto['icon']))
   #icon_url = './'
   #icon_image = "./img/icono_maritima.png"

   #icono = folium.CustomIcon('./icono_maritima.png', icon_size=(45, 45))
   tipo = punto['tipo']

   #icon_image = "icono_maritima.png"
   icon_path = r"C:\Users\LENOVO\Documents\Proyectos Python\no_intrusivos_anam"
   icon_image = icon_path+"/"+punto['icon']

   # Crear el contenido del popup o ventana emergente (también podría se un HTML)
   popup_html = f"<h4>{nombre}</h4><p>{tipo}</p>"

   # 3. Crear y Agregar el marcador al mapa principal de la República Mexicana. 1a.Versión funcionando.

   folium.CircleMarker(
      radius = 20,
      fill = True,
      fill_color = "yellow",
      location = [latitud, longitud],
      popup=popup_html,
      tooltip=nombre, #Texto que aparecerá al pasar el mouse por encima del Marker
      icon=folium.Icon(color='blue', icon='icono_maritima.png') #icono estandard
      #icon=CustomIcon("icono_maritima.png", icon_size =(75, 95), icon_anchor = (10,30)), #icono personalizado
   ).add_to(mapa_principal_rmx)

"""   
   #3-2 Crear y Agregar el marcador al mapa principal de la República Mexicana (2o.)
   icon=CustomIcon(
      icon_image = icon_path+"/"+punto['icon'], 
      #icon_size =(75, 95),
      #icon_anchor = (10,30)
    ).add_to(mapa_principal_rmx)

#3-New
marker = folium.Marker(location=[latitud, longitud], icon=icon, popup=popup_html)
mapa_principal_rmx.add_child(marker)

"""

# 4. Guardar el mapa en un archivo HTML

mapa_principal_rmx.save('mapa_principal_rmx.html')

webbrowser.open('mapa_principal_rmx.html')

#para manejarlo como un módulo: Cerrar el módulo
#return app
if __name__ == '__main__':
    app = mapas()
    app.run()

