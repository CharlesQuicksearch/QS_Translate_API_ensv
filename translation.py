from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate(input, src_lang, tgt_lang):
    if src_lang is "sv":
        model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-sv-en")
        tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-sv-en")
    else:
        model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-sv")
        tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-sv")

    if model is None:
        return "WRONG"

    input_ids = tokenizer(input, return_tensors="pt").input_ids
    outputs = model.generate(input_ids=input_ids, num_beams=5, num_return_sequences=3)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    translation = result[0]

    return translation
