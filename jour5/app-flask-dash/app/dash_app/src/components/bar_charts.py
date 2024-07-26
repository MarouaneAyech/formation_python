import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import requests

def stats_produit_quantite_render(df : pd.DataFrame) -> html.Div:
    stats_produit_quantite = df.groupby('nom')['quantite_vendue'].sum().reset_index()
    return  html.Div([
                dcc.Graph(
                    id='bar-produit-quantite',
                    figure=px.bar(stats_produit_quantite, x='nom', y='quantite_vendue', title='Répartition des quantités vendues par produit')
                )
            ], className="stats-bar")

def stats_produit_revenu_render(df : pd.DataFrame) -> html.Div:
    stats_produit_revenu = df.groupby('nom')['montant'].sum().reset_index()
    return  html.Div([
                    dcc.Graph(
                        id='bar-produit-revenu',
                        figure=px.bar(stats_produit_revenu, x='nom', y='montant', title='Répartition des revenus par produit')
                    )
                ], className="stats-bar")

def stats_ventes_rentabilite_render(df : pd.DataFrame) -> html.Div:
    url = 'http://localhost:5000/predict'

    # Convertir le DataFrame en format JSON
    X=df[['puht','quantite_vendue','date','categorie','nom']]
    X['date'] = X['date'].dt.strftime('%Y-%m-%d')
    data = X.to_dict(orient='records')
    
    # Envoyer le DataFrame complet à l'endpoint /predict
    response = requests.post(url, json={'data': data})
    
    if response.status_code == 200:
        # Extraire les prédictions de la réponse
        predictions = response.json()['prediction']
        df['Classe'] = predictions
    else:
        df['Classe'] = None  # Gérer les erreurs selon vos besoins

    # df=pd.DataFrame({'Classe':['Oui','Non','Non','Oui','Oui','Oui']})    
    hist = df.groupby('Classe')['Classe'].count()
    stats_classes = pd.DataFrame({'Classe': hist.index , 'Count' : hist.values})
    return  html.Div([
                dcc.Graph(
                    id='bar-vente-rentabilite',
                    figure=px.bar(stats_classes, x='Classe', y='Count', title='Rentabilité des ventes')
                )
            ], className="stats-bar")