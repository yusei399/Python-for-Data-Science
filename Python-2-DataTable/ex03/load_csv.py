import pandas as pd

def load(path: str):
    """
    指定されたパスからCSVファイルを読み込み、Pandas DataFrameとして返す。

    Args:
        path (str): CSVファイルのパス。

    Returns:
        pd.DataFrame: 読み込んだCSVデータのPandas DataFrame。
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
