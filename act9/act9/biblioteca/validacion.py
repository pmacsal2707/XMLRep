import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "biblioteca": {
        "type": "object",
        "properties": {
          "libro": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "titulo": {},
                "autor": {
                  "type": "string"
                },
                "publicacion": {},
                "genero": {
                  "type": "string"
                }
              },
              "required": [
                "titulo",
                "autor",
                "publicacion",
                "genero"
              ]
            }
          }
        },
        "required": [
          "libro"
        ]
      }
    },
    "required": [
      "biblioteca"
    ]
  }

# Archivo JSON a validar
archivo_json = '''
{
    "biblioteca": {
      "libro": [
        {
          "titulo": "Don Quijote de la Mancha",
          "autor": "Miguel de Cervantes",
          "publicacion": 1605,
          "genero": "Novela picaresca"
        },
        {
          "titulo": 1984,
          "autor": "George Orwell",
          "publicacion": 1949,
          "genero": "Distopía"
        },
        {
          "titulo": "El gran Gatsby",
          "autor": "F. Scott Fitzgerald",
          "publicacion": 1925,
          "genero": "Novela histórica"
        },
        {
          "titulo": "La Odisea",
          "autor": "Homero",
          "publicacion": "800 a.C.",
          "genero": "Epopeya"
        },
        {
          "titulo": "Frankenstein",
          "autor": "Mary Shelley",
          "publicacion": 1818,
          "genero": "Ciencia ficción"
        },
        {
          "titulo": "Orgullo y prejuicio",
          "autor": "Jane Austen",
          "publicacion": 1813,
          "genero": "Romance"
        },
        {
          "titulo": "Ulises",
          "autor": "James Joyce",
          "publicacion": 1922,
          "genero": "Novela modernista"
        },
        {
          "titulo": "Lolita",
          "autor": "Vladimir Nabokov",
          "publicacion": 1955,
          "genero": "Novela psicológica"
        },
        {
          "titulo": "Matar un ruiseñor",
          "autor": "Harper Lee",
          "publicacion": 1960,
          "genero": "Novela del sur"
        },
        {
          "titulo": "Crimen y castigo",
          "autor": "Fyodor Dostoevsky",
          "publicacion": 1866,
          "genero": "Novela filosófica"
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