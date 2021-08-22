import apache_beam as beam

with beam.Pipeline() as pipeline:
  total = (
      pipeline
      | 'Create numbers' >> beam.Create([3, 4, 1, 2])
      | 'Sum values' >> beam.CombineGlobally(sum)
      | beam.Map(print))