import json
from typing import Any, Dict, List

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


def get_postgres_engine() -> Engine:
    """
    Cria uma conexão com o banco de dados PostgreSQL.

    Returns:
        Engine: Instância do SQLAlchemy Engine conectada ao PostgreSQL.
    """
    return create_engine("postgresql://user:password@postgres:5432/analytics_db")


def load_json_to_dataframe(filepath: str) -> pd.DataFrame:
    """
    Carrega um arquivo JSON e o converte em um DataFrame.

    Args:
        filepath (str): Caminho do arquivo JSON.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados do JSON.
    """
    with open(filepath, mode="r", encoding="utf-8") as file:
        data: List[Dict[str, Any]] = json.load(file)
    return pd.json_normalize(data)


def load_csv_to_dataframe(filepath: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV em um DataFrame.

    Args:
        filepath (str): Caminho do arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados do CSV.
    """
    return pd.read_csv(filepath)


def save_dataframe_to_postgres(
    df: pd.DataFrame, table_name: str, engine: Engine
) -> None:
    """
    Salva um DataFrame no banco de dados PostgreSQL.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        table_name (str): Nome da tabela no banco de dados.
        engine (Engine): Conexão SQLAlchemy com o PostgreSQL.

    Returns:
        None
    """
    df.to_sql(table_name, engine, if_exists="replace", index=False)


def main() -> None:
    """
    Executa o pipeline de ingestão e transformação de dados.

    Realiza as seguintes etapas:
        1. Conexão com o PostgreSQL.
        2. Carregamento de dados do JSON e CSVs.
        3. Transformações básicas nos dados.
        4. Salvamento dos dados transformados no banco de dados PostgreSQL.

    Returns:
        None
    """
    # Conexão com o PostgreSQL
    engine: Engine = get_postgres_engine()

    # Carregamento de dados
    weighins: pd.DataFrame = load_json_to_dataframe("data/weighins.json")
    customer: pd.DataFrame = load_csv_to_dataframe("data/customer.csv")
    objectives: pd.DataFrame = load_csv_to_dataframe("data/objectives.csv")
    customer_objectives: pd.DataFrame = load_csv_to_dataframe(
        "data/customer_objectives.csv"
    )

    # Transformações Básicas
    weighins.dropna(inplace=True)
    customer.drop_duplicates(inplace=True)

    # Salvamento no PostgreSQL
    save_dataframe_to_postgres(weighins, "weighins", engine)
    save_dataframe_to_postgres(customer, "customer", engine)
    save_dataframe_to_postgres(objectives, "objectives", engine)
    save_dataframe_to_postgres(customer_objectives, "customer_objectives", engine)


if __name__ == "__main__":
    main()
