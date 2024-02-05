import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "BDcontactos": {
      "type": "object",
      "properties": {
        "contacto": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "nombre": {
                "type": "string"
              },
              "telefono": {
                "type": "string"
              },
              "direccion": {
                "type": "string"
              },
              "email": {
                "type": "string"
              }
            },
            "required": [
              "nombre",
              "telefono",
              "direccion",
              "email"
            ]
          }
        }
      },
      "required": [
        "contacto"
      ]
    }
  },
  "required": [
    "BDcontactos"
  ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "BDcontactos": {
      "contacto": [
        {
          "nombre": "Juan Pérez",
          "telefono": "123-456-789",
          "direccion": "Gran Vía, 1, 28013 Madrid, España",
          "email": "juan.perez@gmail.com"
        },
        {
          "nombre": "Maria Rodriguez",
          "telefono": "987-654-310",
          "direccion": "Plaza Mayor, 3, 28012 Madrid, España",
          "email": "maria.rodriguez@gmail.com"
        },
        {
          "nombre": "Luis Martínez",
          "telefono": "555-123-467",
          "direccion": "Museo del Prado, 9, 28014 Madrid, España",
          "email": "luis.martinez@gmail.com"
        },
        {
          "nombre": "Ana López",
          "telefono": "555-987-543",
          "direccion": "Puerta del Sol, 1, 28013 Madrid, España",
          "email": "ana.lopez@gmail.com"
        },
        {
          "nombre": "Pablo González",
          "telefono": "555-234-568",
          "direccion": "Estadio Santiago Bernabéu, Av. de Concha Espina, 1, 28036 Madrid, España",
          "email": "pablo.gonzalez@gmail.com"
        },
        {
          "nombre": "Isabel Castro",
          "telefono": "555-876-542",
          "direccion": "Templo de Debod, Calle Ferraz, 1, 28008 Madrid, España",
          "email": "isabel.castro@gmail.com"
        },
        {
          "nombre": "Carlos Ruiz",
          "telefono": "555-345-689",
          "direccion": "Parque del Retiro, Plaza de la Independencia, 7, 28001 Madrid, España",
          "email": "carlos.ruiz@gmail.com"
        },
        {
          "nombre": "Laura Fernández",
          "telefono": "555-765-421",
          "direccion": "Mercado de San Miguel, Plaza de San Miguel, 6, 28005 Madrid, España",
          "email": "laura.fernandez@gmail.com"
        },
        {
          "nombre": "Roberto Sánchez",
          "telefono": "555-456-790",
          "direccion": "Palacio Real, Calle de Bailén, 3, 28071 Madrid, España",
          "email": "roberto.sanchez@gmail.com"
        },
        {
          "nombre": "Elena Díaz",
          "telefono": "555-890-124",
          "direccion": "Cibeles Palace, Plaza de Cibeles, 1, 28014 Madrid, España",
          "email": "elena.diaz@gmail.com"
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