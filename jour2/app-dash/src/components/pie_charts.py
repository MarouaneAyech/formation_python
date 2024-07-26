import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

def stats_categorie_quantite_render(df : pd.DataFrame) -> html.Div:
    stats_categorie_quantite = df.groupby('categorie')['quantite_vendue'].sum().reset_index()
    return html.Div([
        dcc.Graph(
            id='pie-categorie-quantite',
            figure=px.pie(stats_categorie_quantite, 
                            values='quantite_vendue', 
                            names='categorie', 
                            title='Répartition des quantités vendues par catégorie')
        )
    ], className="stats-pie")


def stats_categorie_revenu_render(df : pd.DataFrame) -> html.Div:
    stats_categorie_revenu = df.groupby('categorie')['montant'].sum().reset_index()
    return html.Div([
        dcc.Graph(
            id='pie-categorie-montant',
            figure=px.pie(stats_categorie_revenu, 
                            values='montant', 
                            names='categorie', 
                            title='Répartition des revenus par catégorie')
        )
    ], className="stats-pie")