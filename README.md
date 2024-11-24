# ml-deploy-test

A neural network based classifier to detect whether an input message is likely spam or not. To access visit: https://sms-class-test.streamlit.app/

Receives input from the user via the textbox, and makes a prediction on whether:
1. the message was spam, labelled appropriately
2. or not spam, labeled 'ham'

The main purpose of this project was to understand the workflow behind serving models and deploying for end users to test.

# Local Setup

Here are the steps for running locally, if required.

```bash
git clone 'https://github.com/Abimanyu-Nayagam/ml-deploy-test.git'
```
```bash
cd ml-deploy-test
```
```bash
pip install virtualenv
```
```bash
python -m venv venv
```
```bash
./venv/scripts/activate
```
```bash
pip install -r requirements.txt
```
```bash
streamlit run .\\frontend.\\app.py
```