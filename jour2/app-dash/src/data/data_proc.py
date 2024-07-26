
import pandas as pd

def data_process(file_paths):
    # Charger les données
    df_produit = pd.read_csv(file_paths['produit'])
    df_temps = pd.read_csv(file_paths['temps'])
    df_vente = pd.read_csv(file_paths['vente'])
    # Fusion (Merge) des dataframes en un seul dataframe (entrepot)
    df_merged = pd.merge(df_vente, df_temps, on='id_temps')
    df_merged = pd.merge(df_merged, df_produit, on='id_produit')
    # post-process : 
    # - calcul du montant à partir de puht et quantité
    # - calcul du mois à partir de la date
    df_merged['montant'] = df_merged['quantite_vendue'] * df_merged['puht']
    df_merged['date'] = pd.to_datetime(df_merged['date'])
    # df_merged.drop('date', axis=1, )
    df_merged['mois'] = df_merged['date'].dt.strftime('%Y-%m')
    
    return df_merged