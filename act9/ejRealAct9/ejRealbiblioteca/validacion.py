import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "videojuegos": {
      "type": "object",
      "properties": {
        "videojuego": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "titulo": {
                "type": "string"
              },
              "desarrollador": {
                "type": "string"
              },
              "lanzamiento": {
                "type": "string"
              },
              "genero": {
                "type": "string"
              }
            },
            "required": [
              "titulo",
              "desarrollador",
              "lanzamiento",
              "genero"
            ]
          }
        }
      },
      "required": [
        "videojuego"
      ]
    }
  },
  "required": [
    "videojuegos"
  ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "videojuegos": {
      "videojuego": [
        {
          "titulo": "The Legend of Zelda: Breath of the Wild",
          "desarrollador": "Nintendo",
          "lanzamiento": "3 de marzo de 2017",
          "genero": "Aventura"
        },
        {
          "titulo": "Super Mario Bros.",
          "desarrollador": "Nintendo",
          "lanzamiento": "13 de septiembre de 1985",
          "genero": "Plataformas"
        },
        {
          "titulo": "The Witcher 3: Wild Hunt",
          "desarrollador": "CD Projekt",
          "lanzamiento": "19 de mayo de 2015",
          "genero": "RPG de acción"
        },
        {
          "titulo": "Grand Theft Auto V",
          "desarrollador": "Rockstar North",
          "lanzamiento": "17 de septiembre de 2013",
          "genero": "Acción y aventura"
        },
        {
          "titulo": "Skyrim",
          "desarrollador": "Bethesda Game Studios",
          "lanzamiento": "11 de noviembre de 2011",
          "genero": "RPG de acción"
        },
        {
          "titulo": "Dark Souls",
          "desarrollador": "FromSoftware",
          "lanzamiento": "22 de septiembre de 2011",
          "genero": "Acción y RPG"
        },
        {
          "titulo": "The Elder Scrolls IV: Oblivion",
          "desarrollador": "Bethesda Game Studios",
          "lanzamiento": "20 de marzo de 2006",
          "genero": "RPG de acción"
        },
        {
          "titulo": "Red Dead Redemption 2",
          "desarrollador": "Rockstar Studios",
          "lanzamiento": "26 de octubre de 2018",
          "genero": "Aventura de acción"
        },
        {
          "titulo": "Portal 2",
          "desarrollador": "Valve",
          "lanzamiento": "18 de abril de 2011",
          "genero": "Puzzle, Plataformas"
        },
        {
          "titulo": "Half-Life 2",
          "desarrollador": "Valve",
          "lanzamiento": "16 de noviembre de 2004",
          "genero": "Shooter en primera persona"
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