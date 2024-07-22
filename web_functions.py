# import modul yang akan digunkanan
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

#load dataset
@st.cache_resource()
def load_data():
    
    #load dataset
    df = pd.read_csv('kroniz.csv')
    
    x = df[['tekanan_darah','berat_jenis','albumin','gula','sel_Darah_merah','sel_nanah',
    'gumpalan_sel_nanah','bacteria','glukosa_darah_acak','urea_darah','kreatinin_serum',
    'natrium','kalium','haemoglobin','volume_sel_yang_dikemas','jumlah_sel_darah_putih','jumlah_sel_darah_merah',
    'hipertensi','diabetes_mellitus','penyakit_arteri_koroner','nafsu_makan','pedal_edema',
    'anemia ']]
    y = df[['class']]
    
    return df, x, y

#untuk model decision tree
@st.cache_resource()
def train_model(x, y):
    model = DecisionTreeClassifier(
    ccp_alpha=0.02,  # Menambahkan pruning untuk mengurangi kompleksitas model
    criterion='gini',  # Menggunakan kriteria 'gini' yang mungkin kurang optimal untuk dataset ini
    max_depth=2,  # Mengurangi kedalaman pohon keputusan
    random_state=42
)

    model.fit(x,y)
    
    score = model.score(x,y)
    
    return model, score

def predict(x,y, features):
    model, score = train_model(x, y)
    
    prediction = model.predict(np.array(features).reshape(1,-1))
    
    return prediction, score

