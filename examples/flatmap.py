import apache_beam as beam

with beam.Pipeline() as pipeline:
  plants = (
      pipeline
      | 'Gardening plants' >> beam.Create(['🍓Strawberry 🥕Carrot 🍆Eggplant','🍅Tomato 🥔Potato',])
      | 'Split words' >> beam.FlatMap(str.split)
      | beam.Map(print))