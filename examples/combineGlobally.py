import apache_beam as beam

def get_common_items(sets):
  # set.intersection() takes multiple sets as separete arguments.
  # We unpack the `sets` list into multiple arguments with the * operator.
  # The combine transform might give us an empty list of `sets`,
  # so we use a list with an empty set as a default value.
  return set.intersection(*(sets or [set()]))

with beam.Pipeline() as pipeline:
  common_items = (
      pipeline
      | 'Create produce' >> beam.Create([
          {'🍓', '🥕', '🍌', '🍅', '🌶️'},
          {'🍇', '🥕', '🥝', '🍅', '🥔'},
          {'🍉', '🥕', '🍆', '🍅', '🍍'},
          {'🥑', '🥕', '🌽', '🍅', '🥥'},
      ])
      | 'Get common items' >> beam.CombineGlobally(get_common_items)
      | beam.Map(print))