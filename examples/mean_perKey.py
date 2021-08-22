import apache_beam as beam

with beam.Pipeline() as pipeline:
  elements_with_mean_value_per_key = (
      pipeline
      | 'Create produce' >> beam.Create([
          ('🥕', 3),
          ('🥕', 2),
          ('🍆', 1),
          ('🍅', 4),
          ('🍅', 5),
          ('🍅', 3),
      ])
      | 'Get mean value per key' >> beam.combiners.Mean.PerKey()
      | beam.Map(print))