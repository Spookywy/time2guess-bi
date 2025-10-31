import plotly.express as px

from src.db.db import query_to_df


def plot_games_created_by_day():
    df = query_to_df(
        """
        SELECT
            DATE("createdAt") AS day,
            COUNT(*) AS games_created
        FROM "Game"
        GROUP BY day
        ORDER BY day
    """
    )

    fig = px.line(df, x="day", y="games_created", title="Number of Games Created by Day", markers=True)
    fig.update_layout(xaxis_title="Date", yaxis_title="Games Created per Day", template="plotly_white")
    fig.show()
