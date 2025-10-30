from nba_api.stats.endpoints import leaguegamefinder
from datetime import datetime, timedelta
import pandas as pd
import os
import sys
import time

def get_current_season():
    """Devuelve la temporada actual en formato 'YYY-YY"""
    now = datetime.now()
    year = now.year
    if now.month >= 10:
        return f"{year}-{str(year + 1)[-2:]}"
    else:
        return f"{year - 1}-{str(year)[-2:]}"

def get_recent_games(days=30, retries=3):
    """Descarga los partidos recientes"""
    season = get_current_season()
    print(f"Obteniendo juegos de la temporada {season} de los últimos {days} días...")
      
    # Crear carpeta si no existe
    os.makedirs("../data/raw", exist_ok=True)
    output_path = "../data/raw/nba_games.csv"
    
    for attempt in range(retries):
        try:
            #Llamada a la API
            gamefinder = leaguegamefinder.LeagueGameFinder(
                season_nullable=season, #Obtener temporada actual
                season_type_nullable="Regular Season" #Temporada regular
            )
            
            games = gamefinder.get_data_frames()[0]
            
            #Ordenar por fecha
            games["GAME_DATE"] = pd.to_datetime(games["GAME_DATE"])
            games = games.sort_values("GAME_DATE", ascending=False)
            
            # Filtrar por rango de dias
            limit = datetime.now() - timedelta(days=days)
            recent_games = games[games["GAME_DATE"] >= limit]
            
            if recent_games.empty:
                print("No se encontraron juegos recientes. Verifica que la temporada sea la correcta.")
                return pd.DataFrame()
            
            # Guardar CSV
            recent_games.to_csv(output_path, index=False)
            print(f"\033[32m Se guardaron {len(recent_games)} partidos recientes en {output_path}\033[0m")
            print(f"\nRango de fechas: {recent_games['GAME_DATE'].min().date()} → {recent_games['GAME_DATE'].max().date()}")
            
            return recent_games
        
        except Exception as e:
            print(f"\033[31m Error al obtener los datos (intento {attempt + 1}/{retries}): {e}\033[0m")
            time.sleep(3)
    
    print("\033[31m No se pudo obtener información tras varios intentos.\033[0m")
    sys.exit(1)


if __name__ == "__main__":
    get_recent_games(days=30)