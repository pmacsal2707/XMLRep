import json
from jsonschema import validate

# Definir el esquema
schema = {
    "restaurantes": {
      "sucursal": [
        {
          "direccion1": "Avenida 456",
          "direccion2": "Barrio Sur",
          "chef": "Maria Garcia",
          "fecha": "2022-05-02",
          "plato1": {
            "codigo": 2,
            "descripcion": "Gazpacho Andaluz",
            "cantidad": 4,
            "precio": 18,
            "ingredientes": "Tomate, aceitunas, pan, aceite de oliva",
            "tiempoPreparacion": 30
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Paella Valenciana",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Arroz, pollo, verduras",
            "tiempoPreparacion": 60
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Pollo a la plancha",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Pollo, aceite de oliva, sal",
            "tiempoPreparacion": 10
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Huevos Rotos",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Huevos, chorizo",
            "tiempoPreparacion": 10
          }
        },
        {
          "direccion1": "Avenida 456",
          "direccion2": "Barrio Sur",
          "chef": "Maria Garcia",
          "fecha": "2022-05-02",
          "plato1": {
            "codigo": 2,
            "descripcion": "Gazpacho Andaluz",
            "cantidad": 4,
            "precio": 18,
            "ingredientes": "Tomate, aceitunas, pan, aceite de oliva",
            "tiempoPreparacion": 30
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Paella Valenciana",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Arroz, pollo, verduras",
            "tiempoPreparacion": 60
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Pollo a la plancha",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Pollo, aceite de oliva, sal",
            "tiempoPreparacion": 10
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Huevos Rotos",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Huevos, chorizo",
            "tiempoPreparacion": 10
          }
        },
        {
          "direccion1": "Via 654",
          "direccion2": "Quartiere Trastevere",
          "chef": "Antonio Rossi",
          "fecha": "2022-05-05",
          "plato1": {
            "codigo": 5,
            "descripcion": "Patatas Bravas",
            "cantidad": 4,
            "precio": 10,
            "ingredientes": "Patatas, pimiento, vinagre",
            "tiempoPreparacion": 15
          }
        },
        {
          "direccion1": "Rua 987",
          "direccion2": "Bairro Alto",
          "chef": "Miguel Santos",
          "fecha": "2022-05-06",
          "plato1": {
            "codigo": 6,
            "descripcion": "Calamares a la Romana",
            "cantidad": 4,
            "precio": 25,
            "ingredientes": "Calamares, aceite de oliva, limon",
            "tiempoPreparacion": 25
          }
        },
        {
          "direccion1": "Strada 123",
          "direccion2": "Centru Civic",
          "chef": "Elena Popescu",
          "fecha": "2022-05-07",
          "plato1": {
            "codigo": 7,
            "descripcion": "Tarta de Santiago",
            "cantidad": 4,
            "precio": 30,
            "ingredientes": "Hojaldre, crema, frutas",
            "tiempoPreparacion": 45
          }
        },
        {
          "direccion1": "Street 456",
          "direccion2": "Downtown",
          "chef": "James Johnson",
          "fecha": "2022-05-08",
          "plato1": {
            "codigo": 8,
            "descripcion": "Churros con Chocolate",
            "cantidad": 4,
            "precio": 15,
            "ingredientes": "Churros, chocolate, azúcar",
            "tiempoPreparacion": 20
          }
        }
      ]
    }
  }

# Archivo JSON a validar
archivo_json = '''
{
    "restaurantes": {
      "sucursal": [
        {
          "direccion1": "Avenida 456",
          "direccion2": "Barrio Sur",
          "chef": "Maria Garcia",
          "fecha": "2022-05-02",
          "plato1": {
            "codigo": 2,
            "descripcion": "Gazpacho Andaluz",
            "cantidad": 4,
            "precio": 18,
            "ingredientes": "Tomate, aceitunas, pan, aceite de oliva",
            "tiempoPreparacion": 30
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Paella Valenciana",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Arroz, pollo, verduras",
            "tiempoPreparacion": 60
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Pollo a la plancha",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Pollo, aceite de oliva, sal",
            "tiempoPreparacion": 10
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Huevos Rotos",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Huevos, chorizo",
            "tiempoPreparacion": 10
          }
        },
        {
          "direccion1": "Avenida 456",
          "direccion2": "Barrio Sur",
          "chef": "Maria Garcia",
          "fecha": "2022-05-02",
          "plato1": {
            "codigo": 2,
            "descripcion": "Gazpacho Andaluz",
            "cantidad": 4,
            "precio": 18,
            "ingredientes": "Tomate, aceitunas, pan, aceite de oliva",
            "tiempoPreparacion": 30
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Paella Valenciana",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Arroz, pollo, verduras",
            "tiempoPreparacion": 60
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Pollo a la plancha",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Pollo, aceite de oliva, sal",
            "tiempoPreparacion": 10
          }
        },
        {
          "direccion1": "Calle 123",
          "direccion2": "Colonia Centro",
          "chef": "Juan Perez",
          "fecha": "2022-05-01",
          "plato1": {
            "codigo": 1,
            "descripcion": "Huevos Rotos",
            "cantidad": 4,
            "precio": 20,
            "ingredientes": "Huevos, chorizo",
            "tiempoPreparacion": 10
          }
        },
        {
          "direccion1": "Via 654",
          "direccion2": "Quartiere Trastevere",
          "chef": "Antonio Rossi",
          "fecha": "2022-05-05",
          "plato1": {
            "codigo": 5,
            "descripcion": "Patatas Bravas",
            "cantidad": 4,
            "precio": 10,
            "ingredientes": "Patatas, pimiento, vinagre",
            "tiempoPreparacion": 15
          }
        },
        {
          "direccion1": "Rua 987",
          "direccion2": "Bairro Alto",
          "chef": "Miguel Santos",
          "fecha": "2022-05-06",
          "plato1": {
            "codigo": 6,
            "descripcion": "Calamares a la Romana",
            "cantidad": 4,
            "precio": 25,
            "ingredientes": "Calamares, aceite de oliva, limon",
            "tiempoPreparacion": 25
          }
        },
        {
          "direccion1": "Strada 123",
          "direccion2": "Centru Civic",
          "chef": "Elena Popescu",
          "fecha": "2022-05-07",
          "plato1": {
            "codigo": 7,
            "descripcion": "Tarta de Santiago",
            "cantidad": 4,
            "precio": 30,
            "ingredientes": "Hojaldre, crema, frutas",
            "tiempoPreparacion": 45
          }
        },
        {
          "direccion1": "Street 456",
          "direccion2": "Downtown",
          "chef": "James Johnson",
          "fecha": "2022-05-08",
          "plato1": {
            "codigo": 8,
            "descripcion": "Churros con Chocolate",
            "cantidad": 4,
            "precio": 15,
            "ingredientes": "Churros, chocolate, azúcar",
            "tiempoPreparacion": 20
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