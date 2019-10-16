# file location and type
fl_location = 'interactions_test.csv'
fl_type = 'csv'

# csv options
infer_schema = 'true'
first_row_is_header = 'true'
delimiter = ','

df = spark.read.format(fl_type).option(
    'inferSchema', infer_schema
).option(
    'header', first_row_is_header
).option(
    'sep', delimiter
).load(fl_location)

display(df)
