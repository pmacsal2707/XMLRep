import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "informeVentas": {
      "type": "object",
      "properties": {
        "informeRegional": {
          "type": "object",
          "properties": {
            "Descripcion": {
              "type": "string"
            },
            "Region": {
              "type": "object",
              "properties": {
                "Norte": {
                  "type": "object",
                  "properties": {
                    "Trimestres": {
                      "type": "object",
                      "properties": {
                        "Trimestre1": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        },
                        "Trimestre2": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        },
                        "Trimestre3": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        },
                        "Trimestre4": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        }
                      },
                      "required": [
                        "Trimestre1",
                        "Trimestre2",
                        "Trimestre3",
                        "Trimestre4"
                      ]
                    }
                  },
                  "required": [
                    "Trimestres"
                  ]
                },
                "Centro": {
                  "type": "object",
                  "properties": {
                    "Trimestres": {
                      "type": "object",
                      "properties": {
                        "Trimestre1": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        },
                        "Trimestre2": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        },
                        "Trimestre3": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        },
                        "Trimestre4": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        }
                      },
                      "required": [
                        "Trimestre1",
                        "Trimestre2",
                        "Trimestre3",
                        "Trimestre4"
                      ]
                    }
                  },
                  "required": [
                    "Trimestres"
                  ]
                },
                "Sur": {
                  "type": "object",
                  "properties": {
                    "Trimestres": {
                      "type": "object",
                      "properties": {
                        "Trimestre1": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        },
                        "Trimestre2": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        },
                        "Trimestre3": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        },
                        "Trimestre4": {
                          "type": "object",
                          "properties": {
                            "librosVendidos": {
                              "type": "number"
                            }
                          },
                          "required": [
                            "librosVendidos"
                          ]
                        }
                      },
                      "required": [
                        "Trimestre1",
                        "Trimestre2",
                        "Trimestre3",
                        "Trimestre4"
                      ]
                    }
                  },
                  "required": [
                    "Trimestres"
                  ]
                }
              },
              "required": [
                "Norte",
                "Centro",
                "Sur"
              ]
            }
          },
          "required": [
            "Descripcion",
            "Region"
          ]
        }
      },
      "required": [
        "informeRegional"
      ]
    }
  },
  "required": [
    "informeVentas"
  ]
}

# Archivo JSON a validar
archivo_json = '''
{
    "informeVentas": {
      "informeRegional": {
        "Descripcion": "Informe de Ventas Regionales",
        "Region": {
          "Norte": {
            "Trimestres": {
              "Trimestre1": {
                "librosVendidos": 100
              },
              "Trimestre2": {
                "librosVendidos": 200
              },
              "Trimestre3": {
                "librosVendidos": 150
              },
              "Trimestre4": {
                "librosVendidos": 250
              }
            }
          },
          "Centro": {
            "Trimestres": {
              "Trimestre1": {
                "librosVendidos": 300
              },
              "Trimestre2": {
                "librosVendidos": 400
              },
              "Trimestre3": {
                "librosVendidos": 350
              },
              "Trimestre4": {
                "librosVendidos": 450
              }
            }
          },
          "Sur": {
            "Trimestres": {
              "Trimestre1": {
                "librosVendidos": 500
              },
              "Trimestre2": {
                "librosVendidos": 600
              },
              "Trimestre3": {
                "librosVendidos": 550
              },
              "Trimestre4": {
                "librosVendidos": 650
              }
            }
          }
        }
      }
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