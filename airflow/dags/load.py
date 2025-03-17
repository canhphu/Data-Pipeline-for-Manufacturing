from google.cloud import bigquery
import pandas as pd

def run():
    # Khai báo client BigQuery
    client = bigquery.Client()

    # Đọc dữ liệu đã xử lý
    df = pd.read_csv("data/air_quality_cleaned.csv")

    # Xác định ID Dataset và Table
    table_id = "air-quality-database-454010.airquality.air-quality-items"

    # Ghi dữ liệu vào BigQuery
    job = client.load_table_from_dataframe(df, table_id, job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE"))

    job.result()  # Chờ hoàn thành
    print("Data uploaded to BigQuery successfully.")
