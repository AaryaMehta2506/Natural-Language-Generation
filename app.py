import streamlit as st
import numpy as np
import tensorflow as tf

# Load model and mappings
model = tf.keras.models.load_model("nlg_model.h5")

# Load text and rebuild mappings
with open("dataset.txt", "r", encoding="utf-8") as f:
    text = f.read()

chars = sorted(list(set(text)))
char_to_int = {c: i for i, c in enumerate(chars)}
int_to_char = {i: c for i, c in enumerate(chars)}
seq_length = 100

# Text generation function
def generate_text(seed_text, gen_length=300):
    input_seq = [char_to_int.get(c, 0) for c in seed_text[-seq_length:]]
    for _ in range(gen_length):
        X_pred = np.array([input_seq[-seq_length:]])
        preds = model.predict(X_pred, verbose=0)[0]
        next_index = np.random.choice(len(preds), p=preds)
        input_seq.append(next_index)
    generated = ''.join(int_to_char[i] for i in input_seq)
    return generated

# Streamlit interface
st.title("Natural Language Generation App")
st.write("Enter a starting phrase, and the model will generate text based on it.")

seed_text = st.text_input("Enter seed text:", "ROMEO:")
gen_length = st.slider("Select generation length (characters)", 100, 1000, 300)

if st.button("Generate Text"):
    st.write("Generating text...")
    generated_text = generate_text(seed_text, gen_length)
    st.text_area("Generated Output:", generated_text, height=300)
