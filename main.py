import apache_beam as beam
from apache_beam import PCollection
from apache_beam.options.pipeline_options import PipelineOptions

from typing import Tuple
import argparse

import re

def tuple2str(kv):
    k, v = kv
    return "%s,%d" % (k, v)

def normalizar(w):
    regex = re.compile('[^a-zA-Z]')
    w = regex.sub('', w).lower()
    return w

def main():
    parser = argparse.ArgumentParser(description="Ejemplo pipeline beam")
    parser.add_argument("--input", help="Archivo de entrada")
    parser.add_argument("--output", help="Archivo de salida")
    parser.add_argument("--n", default=100, type=int, help="Cantidad de palabras salida")

    args, beam_args = parser.parse_known_args()
    run_pipeline(args, beam_args)

def run_pipeline(args, beam_args):
    input_file = args.input
    output_file = args.output
    n_palabras = args.n

    opts = PipelineOptions(beam_args)

    with beam.Pipeline(options=opts) as pipeline:
        lineas: PCollection[str] = pipeline | "Lectura de archivo" >> beam.io.ReadFromText(input_file)
        palabras: PCollection[str] = lineas | "Divide por palabras" >> beam.FlatMap(lambda l: l.split())

        limpieza_palabras = palabras | "Limpieza - Formato" >> beam.Map(normalizar)
        cant_palabras: PCollection[Tuple[str, int]] = limpieza_palabras | "Contar cantidad de palabras" >> beam.combiners.Count.PerElement()
        
        cant_palabras_total = lineas | "Contar cantidad de palabras total" >> beam.combiners.Count.Globally() \
                                     | beam.Map(print)                                                                   

        top_palabras = cant_palabras | "Limite de palabras %d" % n_palabras >> beam.combiners.Top.Of(cant_palabras_total[0], 
                                                                                                    key=lambda x: x[1], 
                                                                                                    reverse=False)  # False= Mayor a Menor | True Menor a Mayor

        formato_palabras = top_palabras | "Obtener valores de la coleccion" >> beam.FlatMap(lambda x: x) \
                                        | "Normaliza la salida para csv" >> beam.Map(tuple2str)

        formato_palabras | beam.io.WriteToText(output_file)

if __name__ == '__main__':
    main()