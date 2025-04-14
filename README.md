# 🌍 French2English Translator

This is a **French to English** machine translation app powered by **OpenNMT** and deployed using **Streamlit**.  
The model is hosted on [Hugging Face](https://huggingface.co/IngWalker/french2english-translator) and was trained on a bilingual dataset from Europarl.

---

## 🚀 Demo

👉 [Launch the Streamlit App](https://french2english.streamlit.app/) 

---

## 🧠 Model Info

- **Framework**: [OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py)  
- **Architecture**: Seq2Seq Transformer  
- **Training steps**: 100,000  
- **Data**: The model was trained on the **Europarl v7 parallel corpus**, a collection of proceedings from the European Parliament in both French and English.  
- **Source**: [Europarl Corpus](https://www.statmt.org/europarl/)  
- **Hosted on**: [Hugging Face Hub](https://huggingface.co/IngWalker/french2english-translator)

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/WalkerStanislas/French2English-traductor-app.git
cd French2English-traductor-app
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run app manually
```bash
streamlit run app.py
```
