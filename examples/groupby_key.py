import apache_beam as beam

with beam.Pipeline() as pipeline:
  produce_counts = (
      pipeline
      | 'Create produce counts' >> beam.Create([
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
      | 'Group counts per produce' >> beam.GroupByKey()
      | beam.Map(print))