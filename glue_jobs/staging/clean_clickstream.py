from pyspark.sql.functions import col, to_timestamp

df = spark.read.parquet("s3://your-bucket/staging/clickstream/")

df_clean = df.dropna(subset=["event_type", "user_id"]) \
             .withColumn("event_time", to_timestamp("event_time"))

df_clean.write.mode("overwrite").parquet("s3://your-bucket/clean/clickstream/")
