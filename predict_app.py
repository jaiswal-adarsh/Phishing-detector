import uvicorn
from fastapi import FastAPI
import joblib,os

app=FastAPI()

#pickle file

phish_model=open('phishing.pkl','rb')
phish_model_ls=joblib.load(phish_model)

#machine learning Aspect

@app.get('/predict/{feature}')

async def predict(features):
    x_predict=[]
    x_predict.append(str(features))
    y_predict=phish_model_ls.predict(x_predict)
    
    if y_predict=='bad':
        result="This is a Phishing Site"
        
    else:
        result="This is not a Phishing Site"
        
    return (features,result)

if __name__=='_main_':
    uvicorn.run(app,host="127.0.0.1",port=8000)
