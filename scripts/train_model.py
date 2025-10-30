import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
import os

def train_model(input_path="./data/clean/nba_clean.csv", model_path="./models/nba_winner_predict_model.pkl"):
    """Entrena un modelo de predicción del ganador de partidos"""
    # Cargar datos procesados
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"No se encontró el archivo procesado: {input_path}")

    df = pd.read_csv(input_path)
    print(f"Datos cargados: {len(df)} registros.")

    # Seleccionar campos importantes
    features = [
        "PTS_ROLL5", "REB_ROLL5", "AST_ROLL5",
        "FG_PCT_ROLL5", "FT_PCT_ROLL5", "PLUS_MINUS_ROLL5", "HOME"
    ]
    X = df[features]
    Y = df["WIN"]
    
    # Dividir en entrenamiento y prueba
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
    
    # Crear y entrenar el modelo
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=8,
        random_state=42,
        n_jobs=1
    )
    model.fit(X_train, Y_train)
    
    # Evaluacion
    Y_pred = model.predict(X_test)
    acc = accuracy_score(Y_test, Y_pred)
    cm = confusion_matrix(Y_test, Y_pred)

    print(f"Modelo entrenado con presición: {acc:.3f}")
    print("Matriz de confusión:")
    print(cm)
    
    # Crear carpeta para guardar el modelo
    model_dir = os.path.dirname(model_path)
    os.makedirs(model_dir, exist_ok=True)
    
    #Guardar modelo
    joblib.dump(model, model_path)
    print(f"\033[32m Modelo guardado en {model_path}\033[0m")
    
    return model, acc

if __name__ == "__main__":
    train_model()