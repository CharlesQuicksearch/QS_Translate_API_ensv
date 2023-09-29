import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from Config_Logger import logger

with open('config.json', 'r') as f:
    config = json.load(f)

en_sv_model_path = config.get("en_to_sv_model_path")
en_sv_tokenizer_path = config.get("en_to_sv_tokenizer_path")
sv_en_model_path = config.get("sv_to_en_model_path")
sv_en_tokenizer_path = config.get("sv_to_en_tokenizer_path")

def translate(input, src_lang, tgt_lang):
    if src_lang == "sv":
        model = AutoModelForSeq2SeqLM.from_pretrained(sv_en_model_path)
        tokenizer = AutoTokenizer.from_pretrained(sv_en_tokenizer_path)
        logger.logging.info("Using sv-en translation model.")
    else:
        model = AutoModelForSeq2SeqLM.from_pretrained(en_sv_model_path)
        tokenizer = AutoTokenizer.from_pretrained(en_sv_tokenizer_path)
        logger.logging.info("Using en-sv translation model")

    if model is None:
        return None

    input_ids = tokenizer(input, return_tensors="pt").input_ids
    outputs = model.generate(input_ids=input_ids, num_beams=5, num_return_sequences=3)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    translation = result[0]

    return translation
