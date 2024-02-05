import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "coches": {
        "type": "object",
        "properties": {
          "coche": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "cod": {
                  "type": "string"
                },
                "marca": {
                  "type": "string"
                },
                "modelo": {
                  "type": "string"
                },
                "matricula": {
                  "type": "string"
                },
                "potencia": {
                  "type": "number"
                },
                "plazas": {
                  "type": "number"
                },
                "numPuertas": {
                  "type": "number"
                }
              },
              "required": [
                "cod",
                "marca",
                "modelo",
                "matricula",
                "potencia",
                "plazas",
                "numPuertas"
              ]
            }
          }
        },
        "required": [
          "coche"
        ]
      }
    },
    "required": [
      "coches"
    ]
  }

# Archivo JSON a validar
archivo_json = '''
{
    "coches": {
      "coche": [
        {
          "cod": "C001",
          "marca": "Toyota",
          "modelo": "Corolla",
          "matricula": "ABC123",
          "potencia": 120,
          "plazas": 5,
          "numPuertas": 4
        },
        {
          "cod": "C002",
          "marca": "Ford",
          "modelo": "Focus",
          "matricula": "XYZ789",
          "potencia": 150,
          "plazas": 5,
          "numPuertas": 4
        },
        {
          "cod": "C003",
          "marca": "Chevrolet",
          "modelo": "Malibu",
          "matricula": "DEF456",
          "potencia": 140,
          "plazas": 5,
          "numPuertas": 4
        },
        {
          "cod": "C004",
          "marca": "Honda",
          "modelo": "Accord",
          "matricula": "GHI789",
          "potencia": 160,
          "plazas": 5,
          "numPuertas": 4
        },
        {
          "cod": "C005",
          "marca": "Volkswagen",
          "modelo": "Passat",
          "matricula": "JKL012",
          "potencia": 130,
          "plazas": 5,
          "numPuertas": 4
        },
        {
          "cod": "C006",
          "marca": "Hyundai",
          "modelo": "Elantra",
          "matricula": "MNO345",
          "potencia": 110,
          "plazas": 5,
          "numPuertas": 4
        },
        {
          "cod": "C007",
          "marca": "Nissan",
          "modelo": "Altima",
          "matricula": "PQR678",
          "potencia": 125,
          "plazas": 5,
          "numPuertas": 4
        },
        {
          "cod": "C008",
          "marca": "Mercedes-Benz",
          "modelo": "C-Class",
          "matricula": "STU901",
          "potencia": 180,
          "plazas": 5,
          "numPuertas": 4
        },
        {
          "cod": "C009",
          "marca": "Audi",
          "modelo": "A4",
          "matricula": "VWX234",
          "potencia": 170,
          "plazas": 5,
          "numPuertas": 4
        },
        {
          "cod": "C010",
          "marca": "BMW",
          "modelo": "3 Series",
          "matricula": "YZA567",
          "potencia": 190,
          "plazas": 5,
          "numPuertas": 4
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