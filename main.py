import json
import uvicorn
import schedule

from Config_Logger import logger
from Config_Logger.logger import logging
from fastapi import FastAPI, HTTPException
from request_and_response import Request, Response
from translation import translate

app = FastAPI()

logger.config_logger()

logging.info("Application running.")

#Start writing logs in a new logging file
schedule.every().day.at("00:00").do(logger.config_logger)

@app.get("/home")
def home():
    return {"Translation API: Send a string, src_lang and tgt_lang"}

@app.post("/translate/", response_model= Response)
def translate_string(request_data: Request):
    logging.info(f"Request: {request_data.input}, {request_data.src_lang}, {request_data.tgt_lang}")
    try:
        translation = translate(request_data.input,
                                request_data.src_lang,
                                request_data.tgt_lang)

        if type(translation) is None:
            logging.error(HTTPException(status_code=500, detail=str("Model was not assigned.")))
            raise HTTPException(status_code=500, detail=str("Model was not assigned."))
#
        logging.info(f"200: {translation}")
        return Response(output=translation, score=0)

    except Exception as e:
        logging.error(HTTPException(status_code=500, detail=str(e)))
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)
    uvicorn.run(app, host=config.get("host"), port=int(config.get("port")))
