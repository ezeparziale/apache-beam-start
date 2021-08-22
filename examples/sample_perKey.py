import apache_beam as beam

with beam.Pipeline() as pipeline:
  samples_per_key = (
      pipeline
      | 'Create produce' >> beam.Create([
          ('spring', '🍓'),
          ('spring', '🥕'),
          ('spring', '🍆'),
          ('spring', '🍅'),
          ('summer', '🥕'),
          ('summer', '🍅'),
          ('summer', '🌽'),
          ('fall', '🥕'),
          ('fall', '🍅'),
          ('winter', '🍆'),
      ])
      | 'Samples per key' >> beam.combiners.Sample.FixedSizePerKey(3)
      | beam.Map(print))