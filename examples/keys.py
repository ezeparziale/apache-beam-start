import apache_beam as beam

with beam.Pipeline() as pipeline:
  icons = (
      pipeline
      | 'Garden plants' >> beam.Create([
          ('🍓', 'Strawberry'),
          ('🥕', 'Carrot'),
          ('🍆', 'Eggplant'),
          ('🍅', 'Tomato'),
          ('🥔', 'Potato'),
      ])
      | 'Keys' >> beam.Keys()
      | beam.Map(print))