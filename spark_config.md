# PySpark Windows Configuration for Jupyter

Add this code to your Jupyter notebook BEFORE creating SparkSession:

```python
import os
import sys

# Set environment variables for Windows
os.environ['SPARK_HOME'] = os.path.join(sys.prefix, 'lib', 'site-packages', 'pyspark')
os.environ['JAVA_HOME'] = r'C:\Program Files\Eclipse Adoptium\jdk-17.0.18.8-hotspot'

from pyspark.sql import SparkSession

spark = (SparkSession
    .builder
    .appName("MyApp")
    .master("local[1]")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .config("spark.sql.shuffle.partitions", "1")
    .config("spark.python.worker.reuse", "false")
    .config("spark.memory.fraction", "0.5")
    .config("spark.memory.storageFraction", "0.3")
    .getOrCreate())
```

This configuration:
- Uses local mode with 1 partition (avoids worker communication issues)
- Disables worker reuse to prevent socket errors
- Uses proper JAVA_HOME for Windows
- Configures memory properly for local development

