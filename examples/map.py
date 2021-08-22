import apache_beam as beam

with beam.Pipeline() as pipeline:
  plants = (
      pipeline
      | 'Gardening plants' >> beam.Create([
          '   🍓Strawberry   \n',
          '   🥕Carrot   \n',
          '   🍆Eggplant   \n',
          '   🍅Tomato   \n',
          '   🥔Potato   \n',
      ])
      | 'Strip' >> beam.Map(str.strip)
      | beam.Map(print))