from pyspark.sql import SparkSession
import json

spark = SparkSession.\
        builder.\
        appName("pyspark-restapi").\
        master("spark://spark-master:7077").\
        config("spark.executor.memory", "1g").\
        config("spark.mongodb.input.uri","mongodb://mongo1:27017,mongo2:27018,mongo3:27019/Factory.product?replicaSet=rs0").\
        config("spark.mongodb.output.uri","mongodb://mongo1:27017,mongo2:27018,mongo3:27019/Factory.product?replicaSet=rs0").\
        config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.0").\
        getOrCreate()

#reading dataframes from MongoDB
df = spark.read.format("mongo").load()

#let's change the data type to a timestamp
df = df.withColumn("execution_date", df.execution_date.cast("timestamp"))

#using SparkSQL with MongoDB
# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("product")

def get_lastest_record_fail(number_record):
    result = []
    query = "SELECT * FROM (SELECT * FROM product ORDER BY execution_date DESC LIMIT {}) ORDER BY fail_rate DESC;".format(number_record)
    sqlDF = spark.sql(query)
    for row in sqlDF.rdd.collect():
        # row: <class 'pyspark.sql.types.Row'>
        row_dict = row.asDict()
        result.append(row_dict)
    return result