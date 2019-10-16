import pyspark

sc =pyspark.SparkContext('local[*]')
txt = sc.textFile('gs://spark-bucket-kilth/interactions_test.csv')
print(txt.count)

python_lines = txt.filter(lambda line: '62895' in line.lower())
print(python_lines.count())