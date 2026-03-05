import json
import boto3
import csv
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):

    # Obtener info del archivo subido
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Leer archivo desde S3
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    reader = csv.DictReader(io.StringIO(content))

    output = io.StringIO()
    fieldnames = ["fecha","producto","categoria","precio","cantidad","total"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        precio = float(row["precio"])
        cantidad = int(row["cantidad"])
        total = precio * cantidad

        writer.writerow({
            "fecha": row["fecha"],
            "producto": row["producto"],
            "categoria": row["categoria"],
            "precio": precio,
            "cantidad": cantidad,
            "total": total
        })

    output_key = key.replace("raw/", "processed/")

    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=output.getvalue()
    )

    return {
        "statusCode": 200,
        "body": "Archivo procesado correctamente"
    }