from pyspark.sql import SparkSession

spark = (SparkSession
    .builder
    .appName("TestApp")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .config("spark.python.worker.reuse", "false")
    .config("spark.sql.shuffle.partitions", "1")
    .config("spark.network.timeout", "800s")
    .config("spark.executor.heartbeatInterval", "60s")
    .getOrCreate())

# Test with a simple dataframe
data = [("Alice", 25), ("Bob", 30)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, schema=columns)
df.show()

spark.stop()
