import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "equipos": {
      "type": "object",
      "properties": {
        "equipo": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "nombre": {
                "type": "string"
              },
              "presupuesto": {
                "type": "number"
              },
              "historia": {
                "type": "string"
              },
              "diseño": {
                "type": "string"
              },
              "color": {
                "type": "string"
              }
            },
            "required": [
              "nombre",
              "presupuesto",
              "historia"
            ]
          }
        }
      },
      "required": [
        "equipo"
      ]
    }
  },
  "required": [
    "equipos"
  ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "equipos": {
      "equipo": [
        {
          "nombre": "Real Madrid",
          "presupuesto": 500000000,
          "historia": "El Real Madrid es uno de los clubes de fútbol más exitosos del mundo.",
          "diseño": "Estrella blanca"
        },
        {
          "nombre": "Barcelona",
          "presupuesto": 450000000,
          "historia": "El Barcelona ha ganado numerosos títulos internacionales.",
          "color": "Azul y gris"
        },
        {
          "nombre": "Manchester United",
          "presupuesto": 400000000,
          "historia": "El Manchester United es uno de los clubes de fútbol más antiguos del mundo.",
          "color": "Rojo"
        },
        {
          "nombre": "Bayern Munich",
          "presupuesto": 350000000,
          "historia": "El Bayern Munich ha ganado numerosos títulos nacionales e internacionales.",
          "diseño": "Rayas blancas y azules"
        },
        {
          "nombre": "Liverpool",
          "presupuesto": 300000000,
          "historia": "El Liverpool es conocido por su rivalidad con el Manchester United.",
          "color": "Rojo"
        },
        {
          "nombre": "Juventus",
          "presupuesto": 250000000,
          "historia": "La Juventus es uno de los clubes de fútbol más exitosos de Italia.",
          "diseño": "Rayas negras y blancas"
        },
        {
          "nombre": "PSG",
          "presupuesto": 200000000,
          "historia": "El PSG es uno de los clubes de fútbol más ricos del mundo.",
          "color": "Blanco"
        },
        {
          "nombre": "Atletico Madrid",
          "presupuesto": 150000000,
          "historia": "El Atletico Madrid ha ganado numerosos títulos nacionales.",
          "diseño": "Rayas verticales"
        },
        {
          "nombre": "Chelsea",
          "presupuesto": 100000000,
          "historia": "El Chelsea es uno de los clubes de fútbol más exitosos de Inglaterra.",
          "color": "Azul"
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