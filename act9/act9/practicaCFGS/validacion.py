import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "alumnos": {
        "type": "object",
        "properties": {
          "alumno": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "nif": {
                  "type": "string"
                },
                "resultado": {
                  "type": "string"
                },
                "ip": {
                  "type": "string"
                },
                "mac": {
                  "type": "string"
                }
              },
              "required": [
                "nif",
                "resultado"
              ]
            }
          }
        },
        "required": [
          "alumno"
        ]
      }
    },
    "required": [
      "alumnos"
    ]
  }

# Archivo JSON a validar
archivo_json = '''
{
    "alumnos": {
      "alumno": [
        {
          "nif": "23456789Z",
          "resultado": "apto",
          "ip": "192.168.1.3"
        },
        {
          "nif": "23456789Z",
          "resultado": "apto",
          "ip": "192.168.1.3"
        },
        {
          "nif": "98765432Z",
          "resultado": "No apto",
          "mac": "00:0a:95:9d:68:18"
        },
        {
          "nif": "34567891Z",
          "resultado": "apto",
          "ip": "192.168.1.4"
        },
        {
          "nif": "76543219Z",
          "resultado": "No apto",
          "mac": "00:0a:95:9d:68:19"
        },
        {
          "nif": "45678912Z",
          "resultado": "apto",
          "ip": "192.168.1.5"
        },
        {
          "nif": "65432198Z",
          "resultado": "No apto",
          "mac": "00:0a:95:9d:68:20"
        },
        {
          "nif": "56789123Z",
          "resultado": "apto",
          "ip": "192.168.1.6"
        },
        {
          "nif": "54321987Z",
          "resultado": "No apto",
          "mac": "00:0a:95:9d:68:21"
        },
        {
          "nif": "67891234Z",
          "resultado": "apto",
          "ip": "192.168.1.7"
        },
        {
          "nif": "43219876Z",
          "resultado": "No apto",
          "mac": "00:0a:95:9d:68:22"
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