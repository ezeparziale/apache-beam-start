import apache_beam as beam

with beam.Pipeline() as p:
  grouped = (
      p
      | beam.Create(['strawberry', 'raspberry', 'blueberry', 'blackberry', 'banana']) \
      | beam.GroupBy(lambda s: s[0])) \
      | beam.Map(print)