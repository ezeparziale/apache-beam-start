import apache_beam as beam

with beam.Pipeline() as pipeline:
  mean_element = (
      pipeline
      | 'Create numbers' >> beam.Create([3, 4, 1, 2])
      | 'Get mean value' >> beam.combiners.Mean.Globally()
      | beam.Map(print))