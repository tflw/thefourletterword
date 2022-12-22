import pandas as pnd  
import numpy as nmp  
from joblib import load
import streamlit as smt  
from PIL import Image
from audio_recorder_streamlit import audio_recorder
    
# loading in the model to predict on the data  
model = load("profanitymodel.joblib")
vectorizer = load("profanityvectorizer.joblib")
    
def welcome():  
    return 'welcome you all'  
    

        
    
# Here, this is the main function in which we will be defining our webpage   
def main():  
    html_temp = """  
    <div style = "background-colour: #FFFF00; padding: 16px">  
    <h1 style = "color: black; text-align: centre; "> T.F.L.W</h1>
    <h1 style = "color: black; text-align: centre; "> The Four Letter Word</h1>  
    
    </div>  
    """  

    
    col1, col2= smt.columns([4,6])
    image = Image.open('Logo.jpg')
    image = image.resize((250,250),Image.ANTIALIAS)
    

    

    with col1:
        smt.image(image)

    with col2:
        smt.markdown(html_temp, unsafe_allow_html = True) 

    
    
   
 
        
    # Here, the following lines will create the text boxes in which the user can     # enter the data which is required for making the prediction  
    text = smt.text_input ("Enter text: ", " Type Here")  
    # audio_bytes = audio_recorder()
    # smt.audio(audio_bytes, format="audio/wav")
    
    result = " "  
        
    # here, the below line will ensure that whenever the button named 'Predict' # is clicked, the prediction function that is defined earlier is called for making   # the prediction and it will also store it in the variable result  
    if smt.button ("Predict"):  
        input=text.split()

        tin=vectorizer.transform(input)
        for i in range(len(input)):
            prediction= model.predict(tin[i])
            if(prediction==[1]):
                result+="*#$% "
            else:
                result+=input[i]+" "

          
    smt.success (result)  
if __name__== '__main__':  
    main()  