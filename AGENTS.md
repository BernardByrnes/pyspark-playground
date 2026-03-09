# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

PySpark data engineering learning project running locally on Windows. Work is done primarily in Jupyter notebooks, with CSV/JSON datasets for employee and sales data.

## Environment

- **Python**: 3.10 (`C:\Users\Ben\AppData\Local\Programs\Python\Python310\python.exe`)
- **PySpark**: 3.5.1
- **Java**: Eclipse Adoptium JDK 17 (`C:\Program Files\Eclipse Adoptium\jdk-17.0.18.8-hotspot`)
- **Hadoop**: `C:\hadoop`
- **Development**: Jupyter Notebook

## Running Jupyter

```
python -m jupyter notebook --notebook-dir="D:\Data Engineering\project" --no-browser
```

## Running a standalone PySpark script

```
python spark_test.py
```

## Windows SparkSession Configuration (Critical)

PySpark on Windows requires specific configuration to avoid `SocketTimeoutException` / "Python worker failed to connect back" errors. Every notebook and script must set environment variables and SparkSession config as follows:

```python
import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\Ben\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\Ben\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"
os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["hadoop.home.dir"] = r"C:\hadoop"
os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.18.8-hotspot"

from pyspark.sql import SparkSession
spark = (SparkSession.builder
    .appName("MyApp")
    .master("local[1]")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .config("spark.sql.shuffle.partitions", "1")
    .config("spark.python.worker.reuse", "false")
    .getOrCreate())
```

Key points:
- Use `local[1]` (not `local[*]`) to avoid multi-partition worker communication issues
- Always bind to `127.0.0.1`
- Disable worker reuse (`spark.python.worker.reuse = false`)
- Set shuffle partitions to `1` for local development
- Always call `spark.stop()` at the end of standalone scripts

## Datasets

CSV and JSON files in the project root (e.g., `employees.csv`, `employees_raw.csv`, `sales_info.csv`, `appl_stock.csv`, `people.json`) are used as input data for the notebooks. Output data is written to `output/` as partitioned CSVs.

The `pyspark-zero-to-hero-master/` directory is a reference tutorial repo with its own datasets in `pyspark-zero-to-hero-master/datasets/`.

## Repository Structure

- Root `.ipynb` files: learning notebooks progressing through PySpark fundamentals (DataFrames, joins, transformations, reading/writing data)
- `spark_test.py`: standalone Spark connectivity test
- `spark_config.md`: reference for Windows Spark configuration
- `output/`: Spark-written output (partitioned CSVs)
- `pyspark-zero-to-hero-master/`: reference tutorial (YouTube series companion code)
