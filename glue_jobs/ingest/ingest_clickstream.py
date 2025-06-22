import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_path = "s3://your-bucket/raw/clickstream/"
output_path = "s3://your-bucket/staging/clickstream/"

df = spark.read.json(input_path)

from pyspark.sql.functions import current_timestamp
df = df.withColumn("ingest_time", current_timestamp())

df.write.mode("overwrite").parquet(output_path)

job.commit()
