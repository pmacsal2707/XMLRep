import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "bachillerato": {
      "type": "object",
      "properties": {
        "asignatura": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "nombre": {
                "type": "string"
              },
              "contenidos": {
                "type": "object",
                "properties": {
                  "tema": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "nombre": {
                          "type": "string"
                        },
                        "descripcion": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "nombre",
                        "descripcion"
                      ]
                    }
                  }
                },
                "required": [
                  "tema"
                ]
              }
            },
            "required": [
              "nombre",
              "contenidos"
            ]
          }
        }
      },
      "required": [
        "asignatura"
      ]
    }
  },
  "required": [
    "bachillerato"
  ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "bachillerato": {
      "asignatura": [
        {
          "nombre": "Matemáticas",
          "contenidos": {
            "tema": [
              {
                "nombre": "Álgebra",
                "descripcion": "Estudia los números, las operaciones y las relaciones entre ellos."
              },
              {
                "nombre": "Trigonometría",
                "descripcion": "Explora las relaciones entre los ángulos y los lados de los triángulos."
              },
              {
                "nombre": "Cálculo Diferencial",
                "descripcion": "Estudio de las derivadas y las aplicaciones de las derivadas en la resolución de problemas matemáticos."
              },
              {
                "nombre": "Probabilidad y Estadística",
                "descripcion": "Explora las probabilidades y estadísticas y cómo se aplican a los problemas del mundo real."
              }
            ]
          }
        },
        {
          "nombre": "Física",
          "contenidos": {
            "tema": [
              {
                "nombre": "Termodinámica",
                "descripcion": "Investiga las propiedades de la energía y sus transformaciones."
              },
              {
                "nombre": "Mecánica",
                "descripcion": "Estudia los movimientos de los cuerpos y las fuerzas que los afectan."
              },
              {
                "nombre": "Optica",
                "descripcion": "Explora los fenómenos de la luz y cómo interactúa con diferentes materiales."
              },
              {
                "nombre": "Termodinamica Cuántica",
                "descripcion": "Investiga las propiedades de la materia a nivel cuántico y cómo estas propiedades influyen en la termodinámica."
              }
            ]
          }
        },
        {
          "nombre": "Química",
          "contenidos": {
            "tema": [
              {
                "nombre": "Elementos y compuestos",
                "descripcion": "Estudia los elementos químicos y sus combinaciones para formar compuestos."
              },
              {
                "nombre": "Reacciones químicas",
                "descripcion": "Explora cómo los átomos interactúan para formar nuevos compuestos."
              },
              {
                "nombre": "Química Orgánica",
                "descripcion": "Explora las propiedades y comportamientos de los compuestos orgánicos."
              },
              {
                "nombre": "Química Analítica",
                "descripcion": "Estudia los métodos para identificar y cuantificar los elementos y compuestos en una muestra."
              }
            ]
          }
        },
        {
          "nombre": "Biología",
          "contenidos": {
            "tema": [
              {
                "nombre": "Genética",
                "descripcion": "Investiga cómo los genes controlan las características de los organismos vivos."
              },
              {
                "nombre": "Ecología",
                "descripcion": "Estudia cómo los organismos viven juntos en ecosistemas."
              },
              {
                "nombre": "Microbiología",
                "descripcion": "Explora el estudio de los microorganismos y cómo interactúan con los humanos y con otros organismos."
              },
              {
                "nombre": "Zoología",
                "descripcion": "Estudia la biología de los animales, incluyendo su clasificación, anatomía, comportamiento y ecología."
              }
            ]
          }
        },
        {
          "nombre": "Historia y Ciencias Sociales",
          "contenidos": {
            "tema": [
              {
                "nombre": "Historia antigua",
                "descripcion": "Explora los eventos históricos desde la antigüedad hasta el medioevo."
              },
              {
                "nombre": "Sociología",
                "descripcion": "Investiga las estructuras sociales y cómo funcionan."
              },
              {
                "nombre": "Historia Contemporánea",
                "descripcion": "Explora los eventos históricos desde el siglo XX hasta la actualidad."
              },
              {
                "nombre": "Política",
                "descripcion": "Investiga las estructuras políticas y cómo estas afectan a la sociedad."
              }
            ]
          }
        },
        {
          "nombre": "Lengua y Literatura",
          "contenidos": {
            "tema": [
              {
                "nombre": "Literatura española",
                "descripcion": "Estudia la literatura escrita en español desde la Edad Media hasta la actualidad."
              },
              {
                "nombre": "Teoría literaria",
                "descripcion": "Analiza cómo se interpretan y analizan las obras literarias."
              },
              {
                "nombre": "Literatura Hispanoamericana",
                "descripcion": "Estudia la literatura escrita en español fuera de España, desde la época colonial hasta la actualidad."
              },
              {
                "nombre": "Poesía",
                "descripcion": "Analiza la poesía y cómo se interpreta y analiza."
              }
            ]
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