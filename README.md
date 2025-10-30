# NBA Winner Prediction
Proyecto de Python y Power BI, modelo que prediga el ganador de un partido según estadísticas recientes.


# NBA API
Librería oficial que consume los endpoints de datos públicos de la NBA. Permite acceder a estadisticas de jugadores, equipos o partidos, entre otras opciones más.

En el proyecto se usa el endopoint LeagueGameFinder que devuelve una tabla con los partidos de la NBA históricos y recientes.


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
