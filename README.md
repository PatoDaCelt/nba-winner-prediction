# NBA Winner Prediction
Proyecto de Python y Power BI, modelo que predice el ganador de un partido según estadísticas recientes de los equipos de la NBA.


# NBA API
Librería oficial que consume los endpoints de datos públicos de la NBA. Permite acceder a estadisticas de jugadores, equipos o partidos, entre otras opciones más.

En el proyecto se usa el endopoint LeagueGameFinder que devuelve una tabla con los partidos de la NBA históricos y recientes.

# Preparación de los datos
A partir de los datos crudo s extraidos con la librería NBA API se genera un dataset con los resultados de los partidos más recientes de la temporada actual.
El script precessed_data.py realiza lo siguiente:

- Convierte la columna WL (Win/Loss) en una variable binaria WIN (1 = victoria, 0 = derrota).

- Determina si el equipo jugó como local o visitante a partir de la columna MATCHUP.

- Calcula promedios móviles de los últimos partidos para métricas clave:

    - Puntos (PTS_ROLL5)

    - Rebotes (REB_ROLL5)

    - Asistencias (AST_ROLL5)

    - Porcentajes de tiro (FG_PCT_ROLL5, FT_PCT_ROLL5)

    - Diferencia de puntos (PLUS_MINUS_ROLL5)


# Modelo de predicción
El modelo de predicción utiliza "Random Forest Classifier", que es un algoritmo de aprendizaje supervidaso basdo en árboles de decisión, para estimar la probabilidad de que un equipo gane su próximo partdio.

Documentación de Random Forest Classifier
https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.RandomForestClassifier.html

# Entrenamiento del modelo
El script train_model.py utiliza los campos importantes como variables de entrada (X) y el resultado del partido en binario (WIN) como variable objetivo (Y).

El modelo esta configurado como:
    - n_estimators = 150 -> Número de árboles en el bosque

    - max_depth = 8 -> Profundidad máxima de cada árbol

    - random_state = 42 -> Asegura resproducibilidad

Se divide el conjunto de datos en:

    80% para el entrenamiento

    20% para validación

Evaluación:
    Accuracy -> Proporción de predicciones correctas

    Matriz de confusión -> Distribuye positivos, falsos positivos, falsos negativos, etc.

        En las pruebas iniciales el modelo alcanza una presición de 73% con los datos actuales.

# Estructura del proyecto
nba-game-winner-predictor/
│
├── data/
│   ├── raw/    # Datos crudos
│   ├── clean/  # Datos limpios
│
├── notebooks/
│   ├── 01_get_data.ipynb
│   ├── 02_processed_data.ipynb
│
├── models/
│   └── model.pkl
│
├── scripts/
│   ├── get_data.py        # Descarga y actualiza los datos NBA
│   ├── processed_data.py  # Limpieza y feature engineering
│   ├── train_model.py     # Entrenamiento y guardado del modelo
│   ├── predict.py         # Predicciones nuevas para Power BI
│
├── powerbi/
│   └── nba_dashboard.pbix
│
├── requirements.txt
├── README.md
└── .gitignore
