
def app():
    
    import streamlit.components.v1 as components
    
    from email_extractor import extract
    import csv 
    import re
    import streamlit as st
    import zipfile
    import pandas as pd 
    import os
    from model import model
    import base64
    import warnings 
    
    path=os.getcwd()
    
    st.set_option('deprecation.showfileUploaderEncoding', False)
    data_file = st.file_uploader('Upload', type="zip", encoding="latin1")
    st.set_option('deprecation.showfileUploaderEncoding', False)
    #text_io = io.TextIOWrapper(data_file)
    warnings.filterwarnings(action= 'ignore')
    if  st.button("Classify"):
        
        if  (data_file is not None):
            zf = zipfile.ZipFile(data_file)
            
            file_path=zipfile.Path(data_file)
            file_path_name=str(file_path)
            files=zf.extractall()
            folder_path=path + "\\" + file_path_name
            folder_path=folder_path.replace(".zip/","")
            extract(folder_path)
            os.chdir(path)
            csv_path=folder_path +"\\"+ "test.csv"
            train_path=path +"\\"+ "data.csv"
            df_test=pd.read_csv(csv_path)
            data = pd.read_csv(train_path)
            st.dataframe(df_test)
            final_df = model(df_test , data)
            csv=final_df.to_csv(index = False)
            st.dataframe(final_df)
            
            
            b64 = base64.b64encode(csv.encode()).decode()
            st.markdown('### **⬇️ Download output CSV File **')
            

            st.markdown(f'<a href="data:file/csv;base64,{b64}" download="Prediction.csv">Download the output file</a>', unsafe_allow_html=True)
            st.balloons()
            
                  
    

    
    
    
    
   

