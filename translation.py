from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate(input, src_lang, tgt_lang):
    print(src_lang)
    if src_lang == "sv":
        model = AutoModelForSeq2SeqLM.from_pretrained("models/sv_en/sv_en_model")
        tokenizer = AutoTokenizer.from_pretrained("models/sv_en/sv_en_tokenizer")
    else:
        model = AutoModelForSeq2SeqLM.from_pretrained("models/en_sv/en_sv_model")
        tokenizer = AutoTokenizer.from_pretrained("models/en_sv/en_sv_tokenizer")

    if model is None:
        return "WRONG"

    input_ids = tokenizer(input, return_tensors="pt").input_ids
    outputs = model.generate(input_ids=input_ids, num_beams=5, num_return_sequences=3)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    translation = result[0]

    return translation
