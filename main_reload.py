import apache_beam as beam
from apache_beam import PCollection
from apache_beam.options.pipeline_options import PipelineOptions

from typing import Tuple
import argparse

import re

def normalizar(palabra):
    return palabra.lower()


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
        lineas: PCollection[str] = pipeline \
                                    | "Lectura de archivo" >> beam.io.ReadFromText(input_file) \
                                    | "Divide por palabras" >> beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x)) \
                                    | "Limpieza - Formato" >> beam.Map(normalizar) \
                                    | "Contar cantidad de palabras" >> beam.combiners.Count.PerElement() \
                                    | "Limite de palabras %d" % n_palabras >> beam.combiners.Top.Of(n_palabras, 
                                                                                                    key=lambda x: x[1], 
                                                                                                    # False= Mayor a Menor | True Menor a Mayor
                                                                                                    reverse=False) \
                                    | "Obtener valores de la coleccion" >> beam.FlatMap(lambda x: x) \
                                    | "Normaliza la salida para csv" >> beam.MapTuple(lambda word, count: '%s,%d' % (word, count)) \
                                    | beam.io.WriteToText(output_file)

if __name__ == '__main__':
    main()