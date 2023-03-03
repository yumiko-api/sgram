from fastapi import FastAPI 
import random 

API = FastAPI()

@app.get('/')
async def root():
    return {'Api Powered by': 'Yumiko Team', 'Api Owner': 'Santhu Tech'}
	     
@app.get('sgram')
async def root():
    return {'Api Powered by': 'Yumiko Team', 'Api Owner': 'Santhu Tech'}
