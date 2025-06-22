import sys
from datetime import datetime
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

today = datetime.today().strftime('%Y-%m-%d')

input_path = "s3://your-bucket/enriched/churn_scoring/"
output_path = f"s3://your-bucket/exports/daily_snapshot/date={today}/"

df = spark.read.parquet(input_path)

df.write.mode("overwrite").parquet(output_path)

job.commit()
