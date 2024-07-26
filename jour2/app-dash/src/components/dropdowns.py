import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

def categories_disponibles_render(df : pd.DataFrame) -> html.Div:
    # Liste des catégories disponibles pour la liste déroulante
    categories_disponibles = df['categorie'].unique()
    return html.Div([
                        # Label pour la liste déroulante
                        html.Label("Sélectionnez une catégorie:", style={'font-weight': 'bold', 'marginRight': '10px'}),
                        # Dropdown pour sélectionner la catégorie
                        dcc.Dropdown(
                            id='dropdown-categorie',
                            options=[{'label': cat, 'value': cat} for cat in categories_disponibles],
                            value=categories_disponibles[0],  # Valeur par défaut : première catégorie dans la liste
                            style={'width': '50%'}  # Style pour définir la largeur du dropdown
                        ),
                    ], style={'display': 'flex', 'alignItems': 'center'})  # Flexbox pour aligner verticalement les éléments et centrer horizontalement


def produits_disponibles_render(df: pd.DataFrame) ->html.Div :
    produits_disponibles = produits_disponibles = df['nom'].unique()
    return html.Div([ # Div en ligne pour aligner le label et le dropdown horizontalement à gauche
                # Label pour la liste déroulante
                html.Label("Sélectionnez un produit:", style={'font-weight': 'bold', 'marginRight': '10px'}),      
                # Dropdown pour sélectionner le produit
                dcc.Dropdown(
                    id='dropdown-produit',
                    options=[{'label': prod, 'value': prod} for prod in produits_disponibles],
                    value=produits_disponibles[0],  # Valeur par défaut : premier produit dans la liste
                    style={'width': '50%'}  # Style pour définir la largeur du dropdown
                ),
            ], style={'display': 'flex', 'alignItems': 'center'})  # Flexbox pour aligner verticalement les éléments et centrer horizontalement