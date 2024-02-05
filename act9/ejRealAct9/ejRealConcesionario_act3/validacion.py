import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "almacenMoviles": {
      "type": "object",
      "properties": {
        "movil": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "codigo": {
                "type": "number"
              },
              "marca": {
                "type": "string"
              },
              "modelo": {
                "type": "string"
              },
              "IMEI": {
                "type": "number"
              },
              "almacenamiento": {
                "type": "string"
              },
              "RAM": {
                "type": "string"
              },
              "pantalla": {
                "type": "string"
              }
            },
            "required": [
              "codigo",
              "marca",
              "modelo",
              "IMEI",
              "almacenamiento",
              "RAM",
              "pantalla"
            ]
          }
        }
      },
      "required": [
        "movil"
      ]
    }
  },
  "required": [
    "almacenMoviles"
  ]
}

# Archivo JSON a validar
archivo_json = '''
{
  "almacenMoviles": {
    "movil": [
      {
        "codigo": 1001,
        "marca": "Samsung",
        "modelo": "Galaxy A52",
        "IMEI": 356789012345678,
        "almacenamiento": "128 GB",
        "RAM": "6 GB",
        "pantalla": "6.5 pulgadas"
      },
      {
        "codigo": 1002,
        "marca": "Apple",
        "modelo": "iPhone 12",
        "IMEI": 359012345678901,
        "almacenamiento": "256 GB",
        "RAM": "4 GB",
        "pantalla": "6.1 pulgadas"
      },
      {
        "codigo": 1003,
        "marca": "Google",
        "modelo": "Pixel 5",
        "IMEI": 351234567890123,
        "almacenamiento": "128 GB",
        "RAM": "8 GB",
        "pantalla": "6.0 pulgadas"
      },
      {
        "codigo": 1004,
        "marca": "Xiaomi",
        "modelo": "Redmi Note 10",
        "IMEI": 354567890123456,
        "almacenamiento": "64 GB",
        "RAM": "4 GB",
        "pantalla": "6.43 pulgadas"
      },
      {
        "codigo": 1005,
        "marca": "OnePlus",
        "modelo": "OnePlus 9",
        "IMEI": 359012345678902,
        "almacenamiento": "256 GB",
        "RAM": "12 GB",
        "pantalla": "6.55 pulgadas"
      },
      {
        "codigo": 1006,
        "marca": "Motorola",
        "modelo": "Moto G Power",
        "IMEI": 357890123456789,
        "almacenamiento": "64 GB",
        "RAM": "4 GB",
        "pantalla": "6.4 pulgadas"
      },
      {
        "codigo": 1007,
        "marca": "Huawei",
        "modelo": "P40 Lite",
        "IMEI": 356789012345679,
        "almacenamiento": "128 GB",
        "RAM": "6 GB",
        "pantalla": "6.4 pulgadas"
      },
      {
        "codigo": 1008,
        "marca": "Sony",
        "modelo": "Xperia 5 II",
        "IMEI": 354567890123457,
        "almacenamiento": "128 GB",
        "RAM": "8 GB",
        "pantalla": "6.1 pulgadas"
      },
      {
        "codigo": 1009,
        "marca": "LG",
        "modelo": "V60 ThinQ",
        "IMEI": 359012345678903,
        "almacenamiento": "256 GB",
        "RAM": "8 GB",
        "pantalla": "6.8 pulgadas"
      },
      {
        "codigo": 1010,
        "marca": "Nokia",
        "modelo": "8.3 5G",
        "IMEI": 357890123456790,
        "almacenamiento": "128 GB",
        "RAM": "6 GB",
        "pantalla": "6.81 pulgadas"
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