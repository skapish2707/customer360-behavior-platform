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

input_path = "s3://your-bucket/raw/crm/"
output_path = "s3://your-bucket/staging/crm/"

df = spark.read.json(input_path)

df.write.mode("overwrite").parquet(output_path)

job.commit()
