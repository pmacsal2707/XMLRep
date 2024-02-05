import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "clientes": {
        "type": "object",
        "properties": {
          "sede": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "dir1": {
                  "type": "string"
                },
                "dir2": {
                  "type": "string"
                },
                "empleado": {
                  "type": "string"
                },
                "fecha": {
                  "type": "string"
                },
                "cliente1": {
                  "type": "object",
                  "properties": {
                    "cod": {
                      "type": "number"
                    },
                    "descripcion": {
                      "type": "string"
                    },
                    "numero": {
                      "type": "number"
                    },
                    "coste": {
                      "type": "string"
                    },
                    "resumen": {
                      "type": "string"
                    },
                    "plazo": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "cod",
                    "descripcion",
                    "numero",
                    "coste",
                    "resumen",
                    "plazo"
                  ]
                }
              },
              "required": [
                "dir1",
                "dir2",
                "empleado",
                "fecha",
                "cliente1"
              ]
            }
          }
        },
        "required": [
          "sede"
        ]
      }
    },
    "required": [
      "clientes"
    ]
  }

# Archivo JSON a validar
archivo_json = '''
{
    "clientes": {
      "sede": [
        {
          "dir1": "Palacio Real de Riofrío",
          "dir2": "Bosque de Riofrío",
          "empleado": "Empleado 1",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 1,
            "descripcion": "Real Sitio de Riofrío",
            "numero": 100,
            "coste": "$200",
            "resumen": "Resumen del Real Sitio de Riofrío",
            "plazo": "30 días"
          }
        },
        {
          "dir1": "Real Sitio de La Granja de San Ildefonso",
          "dir2": "Palacio Real de La Granja de San Ildefonso",
          "empleado": "Empleado 2",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 2,
            "descripcion": "Real Sitio de La Granja de San Ildefonso",
            "numero": 101,
            "coste": "$201",
            "resumen": "Resumen del Real Sitio de La Granja de San Ildefonso",
            "plazo": "31 días"
          }
        },
        {
          "dir1": "Real Sitio de Aranjuez",
          "dir2": "Palacio Real de Aranjuez",
          "empleado": "Empleado 3",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 3,
            "descripcion": "Real Sitio de Aranjuez",
            "numero": 102,
            "coste": "$202",
            "resumen": "Resumen del Real Sitio de Aranjuez",
            "plazo": "32 días"
          }
        },
        {
          "dir1": "Real Sitio de El Escorial",
          "dir2": "Monasterio de El Escorial",
          "empleado": "Empleado 4",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 4,
            "descripcion": "Real Sitio de El Escorial",
            "numero": 103,
            "coste": "$203",
            "resumen": "Resumen del Real Sitio de El Escorial",
            "plazo": "33 días"
          }
        },
        {
          "dir1": "Real Sitio de Moncloa",
          "dir2": "Palace of Moncloa",
          "empleado": "Empleado 5",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 5,
            "descripcion": "Real Sitio de Moncloa",
            "numero": 104,
            "coste": "$204",
            "resumen": "Resumen del Real Sitio de Moncloa",
            "plazo": "34 días"
          }
        },
        {
          "dir1": "Real Sitio de Fuencarral",
          "dir2": "Palace of Fuencarral",
          "empleado": "Empleado 6",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 6,
            "descripcion": "Real Sitio de Fuencarral",
            "numero": 105,
            "coste": "$205",
            "resumen": "Resumen del Real Sitio de Fuencarral",
            "plazo": "35 días"
          }
        },
        {
          "dir1": "Real Sitio de Boadilla del Monte",
          "dir2": "Palace of Boadilla del Monte",
          "empleado": "Empleado 7",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 7,
            "descripcion": "Real Sitio de Boadilla del Monte",
            "numero": 106,
            "coste": "$206",
            "resumen": "Resumen del Real Sitio de Boadilla del Monte",
            "plazo": "36 días"
          }
        },
        {
          "dir1": "Real Sitio de El Pardo",
          "dir2": "Palacio de El Pardo",
          "empleado": "Empleado 8",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 8,
            "descripcion": "Real Sitio de El Pardo",
            "numero": 107,
            "coste": "$207",
            "resumen": "Resumen del Real Sitio de El Pardo",
            "plazo": "37 días"
          }
        },
        {
          "dir1": "Real Sitio de Valdemoro",
          "dir2": "Palacio de Valdemoro",
          "empleado": "Empleado 9",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 9,
            "descripcion": "Real Sitio de Valdemoro",
            "numero": 108,
            "coste": "$208",
            "resumen": "Resumen del Real Sitio de Valdemoro",
            "plazo": "38 días"
          }
        },
        {
          "dir1": "Real Sitio de Mejorada del Campo",
          "dir2": "Palacio de Mejorada del Campo",
          "empleado": "Empleado 10",
          "fecha": "01/01/2024",
          "cliente1": {
            "cod": 10,
            "descripcion": "Real Sitio de Mejorada del Campo",
            "numero": 109,
            "coste": "$209",
            "resumen": "Resumen del Real Sitio de Mejorada del Campo",
            "plazo": "39 días"
          }
        }
      ]
    }
  }
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.