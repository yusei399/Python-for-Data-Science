import pandas as pd

def load(path: str):
    """
    指定されたパスからCSVファイルを読み込み、Pandas DataFrameとして返す。

    Args:
        path (str): CSVファイルのパス。

    Returns:
        pd.DataFrame: 読み込んだCSVデータのPandas DataFrame。

    Raises:
        FileNotFoundError: 指定されたパスにCSVファイルが存在しない場合。
        pd.errors.EmptyDataError: 読み込んだCSVデータが空の場合。
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
