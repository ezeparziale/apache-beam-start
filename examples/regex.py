import apache_beam as beam

# Matches a named group 'icon', and then two comma-separated groups.
regex = r'(?P<icon>[^\s,]+), *(\w+), *(\w+)'
with beam.Pipeline() as pipeline:
  plants_matches = (
      pipeline
      | 'Garden plants' >> beam.Create([
          '🍓, Strawberry, perennial',
          '🥕, Carrot, biennial ignoring trailing words',
          '🍆, Eggplant, perennial',
          '🍅, Tomato, annual',
          '🥔, Potato, perennial',
          '# 🍌, invalid, format',
          'invalid, 🍉, format',
      ])
      | 'Parse plants' >> beam.Regex.matches(regex)
      | beam.Map(print))