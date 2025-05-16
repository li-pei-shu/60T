import streamlit as st
import json
from pathlib import Path
import random
import difflib

st.set_page_config(page_title="師父語風 AI", page_icon="📿", layout="centered")
st.image("jingsi_converted.png", width=120)
st.title("🧘‍♂️ 與師父對話 · AI模擬上人口氣")

@st.cache_resource
def load_corpus():
    corpus = {}
    base_path = Path(__file__).parent / "corpus"
    for category in ["charity", "education", "humanism", "medical"]:
        fpath = base_path / "knowledge" / f"{category}_dataset.json"
        if fpath.exists():
            with open(fpath, "r", encoding="utf-8") as f:
                corpus[category] = json.load(f)
    tone_path = base_path / "tone" / "tone_dataset.jsonl"
    tone_data = []
    if tone_path.exists():
        with open(tone_path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    item = json.loads(line.strip())
                    if isinstance(item, dict) and "text" in item:
                        tone_data.append(item)
                except:
                    continue
    corpus["tone"] = tone_data
    return corpus

def replace_first_person(text):
    return text.replace("我", "師父").replace("大家", "你")

def find_best_match(text, entries):
    results = []
    for e in entries:
        score = difflib.SequenceMatcher(None, text, e["text"]).ratio()
        if score > 0.4:
            results.append((score, e["text"]))
    results.sort(reverse=True)
    return results[0][1] if results else ""

corpus = load_corpus()

query = st.text_input("請問你想與師父談什麼？", "")

if query:
    tone_entries = corpus.get("tone", [])
    tone_choices = [t for t in tone_entries if isinstance(t, dict) and "text" in t]
    tone_intro = random.choice(tone_choices)["text"] if tone_choices else "師父說啊…"

    knowledge_response = ""
    for category in ["charity", "education", "humanism", "medical"]:
        entries = corpus.get(category, [])
        match = find_best_match(query, entries)
        if match:
            knowledge_response = match
            break

    if knowledge_response:
        st.markdown("## 🗣️ 師父回應")
        full_response = f"{tone_intro}\n{replace_first_person(knowledge_response)}"
        st.markdown(full_response)
    else:
        st.warning("⚠️ 查無語料對應，請擴充語料庫。")