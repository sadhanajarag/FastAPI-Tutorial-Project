from fastapi import FastAPI,Depends

app  = FastAPI()

#Dependancy Function
def get_db():
    db = {'connection' : 'mock_db_connection'}
    try:
        yield db
    finally:
        db.close()


#Endpoints

@app.get('/home')
def home(db = Depends(get_db)):
    return {'db_status': db['connection']}