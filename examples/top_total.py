import apache_beam as beam

with beam.Pipeline() as pipeline:
  largest_elements = (
      pipeline
      | 'Create numbers' >> beam.Create([3, 4, 1, 2])
      | 'Largest N values' >> beam.combiners.Top.Largest(2)
      | beam.Map(print))