import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define input and output paths
crm_path = "s3://your-bucket/clean/crm/"
clickstream_path = "s3://your-bucket/clean/clickstream/"
output_path = "s3://your-bucket/curated/customer360/"

# Load cleaned CRM and clickstream data
df_crm = spark.read.parquet(crm_path)
df_clickstream = spark.read.parquet(clickstream_path)

df_joined = df_clickstream.join(df_crm, on="user_id", how="left")


df_joined.write.mode("overwrite").parquet(output_path)

job.commit()
