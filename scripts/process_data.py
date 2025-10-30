import pandas as pd
import os

def process_data(input_path="./data/raw/nba_games.csv", output_path="./data/clean/nba_clean.csv"):
    """Limpia y prepara los datos obtenidos para el modelo de predicción"""
    
    # Crear carpeta de salida
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Cargar datos
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"No se encontró el archivo de entrada: {input_path}")
    
    df = pd.read_csv(input_path)
    
    # Convertir formato fechas
    df["GAME_DATE"] = pd.to_datetime(df["GAME_DATE"])
    
    # Seleccionar columnas necesarias
    columns = [
        "GAME_DATE",
        "TEAM_ABBREVIATION",
        "MATCHUP",
        "WL",
        "PTS",
        "REB",
        "AST",
        "FG_PCT",
        "FT_PCT",
        "PLUS_MINUS"
    ]
    df = df[columns]
    
    # Convertir WL (Win/Loss) a 1/0
    df["WIN"] = df["WL"].apply(lambda x: 1 if x == "W" else 0)
    
    # Marcar si es local
    df["HOME"] = df["MATCHUP"].apply(lambda x: 0 if "@" in x else 1)
    
    # Ordenar por equipo y fecha
    df = df.sort_values(by=["TEAM_ABBREVIATION", "GAME_DATE"])
    
    # Calcular medias móviles de rendimiento de los últimos juegos
    rolling_features = ["PTS", "REB", "AST", "FG_PCT", "FT_PCT", "PLUS_MINUS"]
    for col in rolling_features:
        df[f"{col}_ROLL5"] = df.groupby("TEAM_ABBREVIATION")[col].transform(lambda x: x.rolling(5, min_periods=1).mean())
    
    # Eliminar valores nulos
    df = df.dropna().reset_index(drop=True)
    
    # Guardar CSV
    df.to_csv(output_path, index=False)
    print(f"Total de registros: {len(df)}")
    print(f"\033[32m Datos procesados guardados en {output_path}\033[0m")
    
    return df

if __name__ == "__main__":
    process_data()