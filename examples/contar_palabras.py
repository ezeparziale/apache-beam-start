import apache_beam as beam
import re

inputs_pattern = 'data\*'
outputs_prefix = 'outputs/part'

with beam.Pipeline() as pipeline:
  (
      pipeline
      | 'Leer lineas' >> beam.io.ReadFromText(inputs_pattern)
      | 'Solo palabras' >> beam.FlatMap(lambda line: re.findall(r"[a-zA-Z']+", line))
      | 'Palabras con valor 1' >> beam.Map(lambda word: (word, 1))
      | 'Agrupa y suma' >> beam.CombinePerKey(sum)
      | 'Formatea el resultado' >> beam.Map(lambda word_count: str(word_count))
      | 'Graba en archivo' >> beam.io.WriteToText(outputs_prefix)
  )