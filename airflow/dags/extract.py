import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def run():
    # Tạo dữ liệu giả lập
    np.random.seed(42)
    rows = 1000  # Số lượng dòng dữ liệu

    date_rng = pd.date_range(start="2023-01-01", periods=rows, freq='H')
    df = pd.DataFrame({
        "Date": date_rng.date,
        "Time": date_rng.time,
        "CO_GT": np.random.uniform(0, 10, rows),
        "PT08_S1_CO": np.random.uniform(500, 2000, rows),
        "NMHC_GT": np.random.uniform(100, 500, rows),
        "C6H6_GT": np.random.uniform(0, 50, rows),
        "PT08_S2_NMHC": np.random.uniform(500, 2000, rows),
        "NOx_GT": np.random.uniform(50, 2000, rows),
        "PT08_S3_NOx": np.random.uniform(500, 2000, rows),
        "NO2_GT": np.random.uniform(20, 500, rows),
        "PT08_S4_NO2": np.random.uniform(500, 2000, rows),
        "PT08_S5_O3": np.random.uniform(500, 2000, rows),
        "Temperature": np.random.uniform(10, 40, rows),
        "Humidity": np.random.uniform(10, 90, rows),
        "Absolute_Humidity": np.random.uniform(0.5, 2.0, rows)
    })

    # Tạo thư mục lưu trữ
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/air_quality_data.csv", index=False)
    print("Create data Successfully.")