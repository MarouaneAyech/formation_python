################################""
import pandas as pd
import dash
from dash import dcc # Ancienne façon : import dash_core_components as dcc
from dash import html # import dash_html_components as html
import plotly.express as px
from dash_bootstrap_components.themes import BOOTSTRAP
from .src.components import cards, pie_charts, bar_charts, lines, dropdowns
from .src.data.data_proc import data_process

import os

data_dir =  os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')
df_merged = data_process({'produit': os.path.join(data_dir,'produit.csv'), 
                        'temps':os.path.join(data_dir,'temps.csv') , 
                        'vente':os.path.join(data_dir,'vente.csv')
                        })

def create_dash_app(flask_app):
    dash_app = dash.Dash(
        server=flask_app,
        name="app/dash_app",
        url_base_pathname='/dash/',
        external_stylesheets=[BOOTSTRAP],
        assets_folder='app/dash_app/assets',
    )
    dash_app.layout = html.Div(["TB vide"])
    return dash_app

def load_dash_app_layout(dash_app):
    from flask.helpers import get_root_path
    print(os.path.join(get_root_path(dash_app.config.name), dash_app.config.assets_folder))
    # dash_app.layout = 
    # Créer l'application Dash
    # app = dash.Dash(__name__,external_stylesheets=[BOOTSTRAP,"assets/style.css"])

    # Layout de l'application
    dash_app.layout = html.Div([
    html.H1("Tableau de Bord des Ventes", className="dashboard-title"),
    
    # Section des indicateurs globaux
    html.Div([
        cards.quantite_totale_vendue_render(df_merged),
        cards.montant_total_vente_render(df_merged),
        cards.categorie_plus_vendue_render(df_merged),
        cards.produit_plus_vendu_render(df_merged),
        cards.categorie_plus_rentable_render(df_merged),
        cards.produit_plus_rentable_render(df_merged)
    ], className='cards-container'),

    html.Hr(),

    # Section de Statistiques sur les catégories
    html.Div([
        html.H2("Statistiques sur les Catégories", className="section-title"),
        html.Div([
            pie_charts.stats_categorie_quantite_render(df_merged),
            pie_charts.stats_categorie_revenu_render(df_merged)                
        ], style={'display': 'flex'}),
    ], className="stats-container"),
    
    html.Hr(),
    
    # Section des statistiques sur les produits
    html.Div([
        html.H2("Statistiques sur les Produits", className="section-title"),
        html.Div([
            bar_charts.stats_produit_quantite_render(df_merged),
            bar_charts.stats_produit_revenu_render(df_merged)
        ], style={'display': 'flex'})   
    ], className="stats-container"),

    html.Hr(),

    # Section d'analyse temporelle
    html.Div([
            html.H2("Analyse Temporelle", className="section-title"),
            # Div en ligne pour aligner les graphiques horizontalement
            html.Div([
                lines.quantite_mensuelle_render(df_merged),
                lines.revenu_mensuel_render(df_merged)
            ], style={'display': 'flex'})
    ], className="stats-container"),
    
    # Section d'analyse temporelle par catégrie
    html.Div([
            html.H2("Analyse Temporelle par catégories", className="section-title"),
            dropdowns.categories_disponibles_render(df_merged),
            lines.quantite_revenu_mensuels_cat_render(df_merged, dash_app)
    ], className="stats-container"),

    # Section d'analyse temporelle par produit
    html.Div([
            html.H2("Analyse Temporelle par produit", className="section-title"),
            dropdowns.produits_disponibles_render(df_merged),
            lines.quantite_revenu_mensuels_prod_render(df_merged, dash_app)
    ], className="stats-container"),

    html.Div([
        bar_charts.stats_ventes_rentabilite_render(df_merged)
    ], className="stats-container")

    # Section Histogramme de prédiction
    # html.Div([
    #         html.H2("Prédiction de rentabilité des ventes ", className="section-title"),
    #         dcc.Graph(
    #             figure= px.histogram(df, x='Fréquence', title="Histogramme de Rentabilité des Ventes")
    #         )
    # ], className="stats-container")

    ])

    return dash_app