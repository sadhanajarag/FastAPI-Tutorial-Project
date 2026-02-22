from fastapi import FastAPI, HTTPException
import asyncio


app = FastAPI()
@app.get('/wait')
async def wait():
    await asyncio.sleep(3)
    return{"meaage" : "Finished waiting"}

