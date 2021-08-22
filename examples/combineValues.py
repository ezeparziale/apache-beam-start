import apache_beam as beam

with beam.Pipeline() as pipeline:
  total = (
      pipeline
      | 'Create produce counts' >> beam.Create([
          ('🥕', [3, 2]),
          ('🍆', [1]),
          ('🍅', [4, 5, 3]),
      ])
      | 'Sum' >> beam.CombineValues(sum)
      | beam.Map(print))