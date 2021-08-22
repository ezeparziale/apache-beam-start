import apache_beam as beam

with beam.Pipeline() as pipeline:
  unique_elements = (
      pipeline
      | 'Create produce' >> beam.Create([
          '🥕',
          '🥕',
          '🍆',
          '🍅',
          '🍅',
          '🍅',
      ])
      | 'Deduplicate elements' >> beam.Distinct()
      | beam.Map(print))