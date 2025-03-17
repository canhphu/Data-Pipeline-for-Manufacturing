import pandas as pd

def run():
    df = pd.read_csv("data/air_quality_data.csv")

    # Chuyển đổi dữ liệu
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.time

    # Xử lý missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    df.to_csv("data/air_quality_cleaned.csv", index=False)
    print("Transform data successfully.")
