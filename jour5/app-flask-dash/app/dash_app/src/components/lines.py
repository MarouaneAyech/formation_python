import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Input, Output

def quantite_mensuelle_render(df : pd.DataFrame) -> html.Div:
    # Quantité mensuelle vendue
    quantite_mensuelle = df.groupby('mois')['quantite_vendue'].sum().reset_index()
    return  html.Div([
                dcc.Graph(
                    id='line-quantite-mensuelle',
                    figure=px.line(quantite_mensuelle, x='mois', y='quantite_vendue', title='Quantité vendue mensuelle')
                )
            ], className="stats-bar")
    
def revenu_mensuel_render(df : pd.DataFrame) -> html.Div:
    revenu_mensuel = df.groupby('mois')['montant'].sum().reset_index()
    return  html.Div([
                dcc.Graph(
                    id='line-revenu_mensuel',
                    figure=px.line(revenu_mensuel, x='mois', y='montant', title='Revenu mensuel')
                )
            ], className="stats-bar")

def quantite_revenu_mensuels_cat_render(df : pd.DataFrame, app : Dash) -> html.Div:
    # Callback pour mettre à jour les graphiques de la catégorie sélectionnée
    @app.callback(
        [Output('line-quantite-categorie', 'figure'),
        Output('line-revenu-categorie', 'figure')],
        [Input('dropdown-categorie', 'value')]
    )
    def update_category_graphs(selected_category):
        # Filtrer les données pour la catégorie sélectionnée
        df_category = df[df['categorie'] == selected_category]
        # Quantité mensuelle vendue pour la catégorie sélectionnée
        quantite_mensuelle_cat = df_category.groupby('mois')['quantite_vendue'].sum().reset_index()
        # Revenu mensuel pour la catégorie sélectionnée
        revenu_mensuel_cat = df_category.groupby('mois')['montant'].sum().reset_index()
        # Créer les figures pour les graphiques
        fig_quantite_cat = px.line(quantite_mensuelle_cat, x='mois', y='quantite_vendue', title=f"Quantité mensuelle de {selected_category}")
        fig_revenu_cat = px.line(revenu_mensuel_cat, x='mois', y='montant', title=f"Revenu mensuel de {selected_category}")
        return fig_quantite_cat, fig_revenu_cat

    return html.Div([
                dcc.Graph(
                    id='line-quantite-categorie',
                    style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}
                ),
                dcc.Graph(
                    id='line-revenu-categorie',
                    style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}
                )
            ], style={'display': 'flex'})

def quantite_revenu_mensuels_prod_render(df : pd.DataFrame, app : Dash) -> html.Div:
    # # Callback pour mettre à jour les graphiques du produit sélectionné
    # Callback pour mettre à jour les graphiques du produit sélectionné
    @app.callback(
        [Output('line-quantite-produit', 'figure'),
        Output('line-revenu-produit', 'figure')],
        [Input('dropdown-produit', 'value')]
    )
    def update_product_graphs(selected_product):
        # Filtrer les données pour le produit sélectionné
        df_product = df[df['nom'] == selected_product]
        # Quantité mensuelle vendue pour le produit sélectionné
        quantite_mensuelle_prod = df_product.groupby('mois')['quantite_vendue'].sum().reset_index()
        # Revenu mensuel pour le produit sélectionné
        revenu_mensuel_prod = df_product.groupby('mois')['montant'].sum().reset_index()
        
        # Créer les figures pour les graphiques
        fig_quantite_prod = px.line(quantite_mensuelle_prod, x='mois', y='quantite_vendue', title=f"Quantité mensuelle de {selected_product}")
        fig_revenu_prod = px.line(revenu_mensuel_prod, x='mois', y='montant', title=f"Revenu mensuel de {selected_product}")
        
        return fig_quantite_prod, fig_revenu_prod

    # Div en ligne pour aligner les graphiques horizontalement
    return html.Div([
        # Graphique ligne pour la quantité vendue mensuelle du produit sélectionné
        dcc.Graph(
            id='line-quantite-produit',
            style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}
        ),
        # Graphique ligne pour le revenu mensuel du produit sélectionné
        dcc.Graph(
            id='line-revenu-produit',
            style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}
        )
    ], style={'display': 'flex'})