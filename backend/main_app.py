from fastapi import FastAPI,HTTPException
app = FastAPI()

@app.get("/")
async def root():
 return {"test":"test"}

@app.get("/testGET")
async def root():
 return {"testGET":"testGET"}