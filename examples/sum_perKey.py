import apache_beam as beam

with beam.Pipeline() as pipeline:
  totals_per_key = (
      pipeline
      | 'Create produce' >> beam.Create([
          ('🥕', 3),
          ('🥕', 2),
          ('🍆', 1),
          ('🍅', 4),
          ('🍅', 5),
          ('🍅', 3),
      ])
      | 'Sum values per key' >> beam.CombinePerKey(sum)
      | beam.Map(print))