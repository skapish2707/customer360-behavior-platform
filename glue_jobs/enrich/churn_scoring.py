import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, when, count, avg

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Input: Customer360 curated dataset
input_path = "s3://your-bucket/curated/customer360/"
output_path = "s3://your-bucket/enriched/churn_scoring/"

# Read the curated data
df = spark.read.parquet(input_path)

# Optional: define churn logic
# Example logic:
# - If customer hasn't clicked in last 30 days → likely to churn
# - Few sessions + no CRM activity = high churn risk

df_scored = df.withColumn(
    "churn_score",
    when(col("last_event_time").isNull(), 0.9)
    .when(col("event_type") == "logout", 0.7)
    .when(col("event_type") == "session_end", 0.6)
    .otherwise(0.2)
)

# Optional: classify churn level
df_scored = df_scored.withColumn(
    "churn_risk_level",
    when(col("churn_score") >= 0.8, "HIGH")
    .when((col("churn_score") >= 0.5) & (col("churn_score") < 0.8), "MEDIUM")
    .otherwise("LOW")
)

# Write to enriched output
df_scored.write.mode("overwrite").parquet(output_path)

job.commit()
