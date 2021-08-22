import apache_beam as beam

with beam.Pipeline() as pipeline:
  elements_with_max_value_per_key = (
      pipeline
      | 'Create produce' >> beam.Create([
          ('🥕', 3),
          ('🥕', 2),
          ('🍆', 1),
          ('🍅', 4),
          ('🍅', 5),
          ('🍅', 3),
      ])
      | 'Get max value per key' >> beam.CombinePerKey(max)
      | beam.Map(print))