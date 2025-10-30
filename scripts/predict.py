import pandas as pd
import joblib
import os

def predict_games(
    data_path="./data/clean/nba_clean.csv",
    model_path="./models/nba_winner_predict_model.pkl",
    output_path="./data/clean/predictions.csv"
):
    """Genera predicciones de probabilidad de vistorias usando el modelo entrenado"""
    # Verificar archivos requeridos
    if not os.path.existe(data_path):
        raise FileNotFoundError(f"Nose encontró el archivo de datos procesados: {data_path}")
    if not os.exists(model_path):
        raise FileExistsError(f"No se encontró el modelo entrenado: {model_path}")
    
    # Cargar modelo y datos
    model = joblib.load(model_path)
    df = pd.read_csv(data_path)
    
    # Campos usados en el entrenamiento
    features = [
        "PTS_ROLL5", "REB_ROLL5", "AST_ROLL5",
        "FG_PCT_ROLL5", "FT_PCT_ROLL5", "PLUS_MINUS_ROLL5", "HOME"
    ]
    
    # Calcular probabilidad de victoria
    df["WIN_PROB"] = model.predict_proba(df[features])[:, 1]
    
    # Salida simplificada
    predictions = df[[
        "GAME_DATE", "TEAM_ABBREVIATION", "MATCHUP", "HOME", "WIN_PROB", "WIN"
    ]].copy()
    
    # Guardar CSV de la salida
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    predictions.to_csv(output_path, index=False)
    print(f"\033[32m Predicciones guardadas en {output_path}\033[0m")
    
    return predictions