from transformers import AutoTokenizer, T5ForConditionalGeneration

model_name = "IlyaGusev/rut5_base_sum_gazeta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)


def generate_text(text: str, max_length: int):
    input_ids = tokenizer(
        [text],
        max_length=max_length,
        add_special_tokens=True,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    return summary

