import streamlit as st
import tensorflow as tf
import numpy as np
from keras.utils import pad_sequences

MAX_LEN = 250

input = st.text_input("Enter text here: ")

vocab = {}

i = 0
try:
    with open('backend/vocab.txt') as f:
        content = f.read().replace('|', '\n')

    words = content.split()

    for i in range(len(words)):
        vocab[i] = words[i]
except Exception as e:
    print(f"Error creating vocabulary: {e}")

try:
    model = tf.keras.models.load_model('backend/sms_class_model')
except Exception as e:
    st.write(f"Error importing model: {e}")

def pred(input):
    reversed_dict = {value: key for key, value in vocab.items()}
    words = []
    for i in input.split():
        if i in reversed_dict and i.isalpha():
            words.append(reversed_dict[i])
    if len(words) != 0:
        padded_input = pad_sequences([words], MAX_LEN)
        padded_input = np.array(padded_input)
        pred = model.predict(padded_input)
        st.write(pred[0])
        pred = (pred[0] > 0.5).astype(int)
        st.write(f"I think this message is a {vocab[pred[0]]}")
    else:
        st.write("Input not received")

try:
    if input:
        pred(input)
except Exception as e:
    st.write(f"Error while making prediction: {e}")