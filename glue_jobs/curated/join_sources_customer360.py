df_crm = spark.read.parquet("s3://your-bucket/clean/crm/")
df_clickstream = spark.read.parquet("s3://your-bucket/clean/clickstream/")

df_joined = df_clickstream.join(df_crm, on="user_id", how="left")

df_joined.write.mode("overwrite").parquet("s3://your-bucket/curated/customer360/")
