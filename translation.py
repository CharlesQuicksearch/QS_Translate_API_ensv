from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate(input, src_lang, tgt_lang):
    if src_lang is "sv":
        sv_eng_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-sv-en")
        sv_en_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-sv-en")
    else:
        en_sv_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-sv")
        en_sv_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-sv")
