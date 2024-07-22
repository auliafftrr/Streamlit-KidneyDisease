import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


from sklearn import tree
import streamlit as st

from web_functions import train_model

def app(df, x, y):
    
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    st.title("Visualisasi Prediksi Penyakit Ginjal")
    
    if st.checkbox("Confusion Matrix"):
        model, score =  train_model(x, y)
        plt.figure(figsize=(10,6))
        confusion_matrix(model, x, y, values_format='df') #error
        st.pyplot()
        
    if st.checkbox("Plot Desicion Tree"):
        model, score = train_model(x, y)
        load_data = tree.export_graphviz(
            decision_tree= model, max_depth=4, out_file=None, filled=True, rounded=True,
            feature_names= x.columns, class_names=['nockd', 'ckd']
        )
        
        st.graphviz_chart(dot_data)