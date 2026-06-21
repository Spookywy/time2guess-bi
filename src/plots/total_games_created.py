from src.db.db import query_to_scalar


def plot_total_games_created():
    total_games_created = query_to_scalar("""
        SELECT COUNT(*) AS total_games_created
        FROM "Game"
    """)

    print(f"Total Games Created: {total_games_created}")
