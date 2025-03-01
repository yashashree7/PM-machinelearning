-name: Deploy Streamlit App

on:
  push:
    branches:
      - master  # Runs on code push to the master branch
  pull_request:
    branches:
      - master  # Runs on PR to master

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Deploy to Streamlit
        run: |
          streamlit run streamlit_app.py
