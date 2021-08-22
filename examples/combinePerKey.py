import apache_beam as beam

with beam.Pipeline() as pipeline:
  total = (
      pipeline
      | 'Create plant counts' >> beam.Create([
          ('🥕', 3),
          ('🥕', 2),
          ('🍆', 1),
          ('🍅', 4),
          ('🍅', 5),
          ('🍅', 3),
      ])
      | 'Sum' >> beam.CombinePerKey(sum)
      | beam.Map(print))