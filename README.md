# AWS Sales Data Pipeline

Simple **serverless data pipeline** built on AWS to process and analyze sales data.

## Architecture

CSV Upload → Amazon S3 (raw data) → AWS Lambda (data processing) → Amazon S3 (processed data) → Amazon Athena (SQL queries)

## Technologies

* Amazon S3
* AWS Lambda
* Amazon Athena
* Python

## Project Overview

This project demonstrates a basic cloud data pipeline using AWS services.

1. A CSV file containing sales data is uploaded to an S3 bucket.
2. The upload triggers a Lambda function.
3. The Lambda function processes the data and calculates total sales.
4. The processed file is stored back in S3.
5. The results can be queried using Athena.

## Example Query

SELECT producto, SUM(total) as ventas
FROM ventas_procesado
WHERE producto != 'producto'
GROUP BY producto;
```

## Learning Goal

This project was built as part of a learning roadmap to practice building **data pipelines on AWS using serverless services**.
