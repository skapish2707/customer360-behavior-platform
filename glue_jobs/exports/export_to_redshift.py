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

input_path = "s3://your-bucket/enriched/churn_scoring/"

df = spark.read.parquet(input_path)

# Redshift config (replace placeholders with actual values)
redshift_tmp_dir = "s3://your-bucket/temp/"
redshift_conn_options = {
    "url": "jdbc:redshift://your-redshift-cluster:5439/dev",
    "user": "your_user",
    "password": "your_password",
    "dbtable": "public.customer360_churn",
    "redshiftTmpDir": redshift_tmp_dir
}

df.write \
  .format("com.databricks.spark.redshift") \
  .options(**redshift_conn_options) \
  .mode("overwrite") \
  .save()

job.commit()
