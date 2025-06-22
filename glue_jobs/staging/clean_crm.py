import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import trim, col

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_path = "s3://your-bucket/staging/crm/"
output_path = "s3://your-bucket/clean/crm/"

# Read CRM data
df = spark.read.parquet(input_path)

# Basic cleaning: remove leading/trailing spaces and drop null customer ids
df_clean = df.withColumn("user_id", trim(col("user_id"))) \
             .withColumn("email", trim(col("email"))) \
             .dropna(subset=["user_id"])

# Write clean CRM data
df_clean.write.mode("overwrite").parquet(output_path)

job.commit()
