from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-large"

print("Loading model, please wait...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def explain_text(text, level="10"):
    prompt = f"Explain the following text like I am {level} years old:\n{text}"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(
        **inputs,
        max_length=300,
        temperature=0.7,
    )
    explanation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return explanation

# --- Simple CLI loop ----

print("\n=== EXPLAIN LIKE I'M 10 ===")
while True:
    text = input("\nPaste your text (or type 'exit'): ")

    if text.lower() == "exit":
        break

    level = input("Explain like I'm (5 / 10 / 15): ")
    if level not in ["5", "10", "15"]:
        level = "10"

    print("\n📘 Explanation:")
    print(explain_text(text, level=level))
