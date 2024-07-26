import pandas as pd
from dash import Dash, html, dcc

def quantite_totale_vendue_render(df : pd.DataFrame) -> html.Div:
    quantite_totale_vendue = df['quantite_vendue'].sum()
    return html.Div([
            html.H3("Quantité totale vendue"),
            html.P(quantite_totale_vendue)
        ], className="card")

def montant_total_vente_render(df : pd.DataFrame) -> html.Div:
    montant_total_vente = df['montant'].sum()
    return html.Div([
            html.H3("Quantité totale vendue"),
            html.P(montant_total_vente)
        ], className="card")

def categorie_plus_vendue_render(df : pd.DataFrame) -> html.Div:
    categorie_plus_vendue = df.groupby('categorie')['quantite_vendue'].sum().idxmax()
    return html.Div([
            html.H3("Quantité totale vendue"),
            html.P(categorie_plus_vendue)
        ], className="card")

def produit_plus_vendu_render(df : pd.DataFrame) -> html.Div:
    produit_plus_vendu = df.groupby('nom')['quantite_vendue'].sum().idxmax()
    return html.Div([
            html.H3("Quantité totale vendue"),
            html.P(produit_plus_vendu)
        ], className="card")

def categorie_plus_rentable_render(df : pd.DataFrame) -> html.Div:
    categorie_plus_rentable = df.groupby('categorie')['montant'].sum().idxmax()
    return html.Div([
            html.H3("Quantité totale vendue"),
            html.P(categorie_plus_rentable)
        ], className="card")

def produit_plus_rentable_render(df : pd.DataFrame) -> html.Div:
    produit_plus_rentable = df.groupby('nom')['montant'].sum().idxmax()
    return html.Div([
            html.H3("Quantité totale vendue"),
            html.P(produit_plus_rentable)
        ], className="card")

