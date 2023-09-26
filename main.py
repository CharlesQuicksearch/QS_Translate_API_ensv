from fastapi import FastAPI, HTTPException
from request_and_response import Request, Response
from translation import translate

app = FastAPI()

@app.get("/")
def home():
    return {"Translation API: Send a string, src_lang and tgt_lang"}

@app.post("/translate/", response_model= Response)
async def translate(request_data: Request):
    try:
        translation = await translate(request_data.input,
                                request_data.src_lang,
                                request_data.tgt_lang)
        return Response(output=translation, score=0)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
