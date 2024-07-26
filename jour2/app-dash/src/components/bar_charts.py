import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

def stats_produit_quantite_render(df : pd.DataFrame) -> html.Div:
    stats_produit_quantite = df.groupby('nom')['quantite_vendue'].sum().reset_index()
    return  html.Div([
                dcc.Graph(
                    id='bar-produit-quantite',
                    figure=px.bar(stats_produit_quantite, 
                                  x='nom', 
                                  y='quantite_vendue', 
                                  title='Répartition des quantités vendues par produit')
                )
            ], className="stats-bar")

def stats_produit_revenu_render(df : pd.DataFrame) -> html.Div:
    stats_produit_revenu = df.groupby('nom')['montant'].sum().reset_index()
    return  html.Div([
                    dcc.Graph(
                        id='bar-produit-revenu',
                        figure=px.bar(stats_produit_revenu, 
                                      x='nom', 
                                      y='montant', 
                                      title='Répartition des revenus par produit')
                    )
                ], className="stats-bar")