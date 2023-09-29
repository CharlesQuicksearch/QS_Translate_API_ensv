from fastapi import FastAPI, HTTPException
from request_and_response import Request, Response
from translation import translate
from Config_Logger import logger
import schedule

app = FastAPI()
logger.config_logger()

#Start writing logs in a new logging file
schedule.every().day.at("00:00").do(logger.config_logger)

@app.get("/home")
def home():
    return {"Translation API: Send a string, src_lang and tgt_lang"}

@app.post("/translate/", response_model= Response)
def translate_string(request_data: Request):
    logger.logging.info(f"Request: {request_data.input}, {request_data.src_lang}, {request_data.tgt_lang}")
    try:
        translation = translate(request_data.input,
                                request_data.src_lang,
                                request_data.tgt_lang)

        if type(translation) is None:
            logger.logging.error(HTTPException(status_code=500, detail=str("Model was not assigned.")))
            raise HTTPException(status_code=500, detail=str("Model was not assigned."))
#
        logger.logging.info(f"Response: {translation}")
        return Response(output=translation, score=0)

    except Exception as e:
        logger.logging.error(HTTPException(status_code=500, detail=str(e)))
        raise HTTPException(status_code=500, detail=str(e))
