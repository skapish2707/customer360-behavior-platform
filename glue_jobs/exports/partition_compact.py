import sys
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

input_path = "s3://your-bucket/exports/daily_snapshot/"
output_path = "s3://your-bucket/exports/compacted_snapshot/"

df = spark.read.parquet(input_path)

# Repartition to reduce small files
df.repartition(1).write.mode("overwrite").parquet(output_path)

job.commit()
