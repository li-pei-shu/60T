import streamlit as st
import json
from pathlib import Path
import random

st.set_page_config(page_title="師徒之間 AI", page_icon="📜", layout="centered")

# --- 載入語料 ---
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
                tone_data.append(json.loads(line.strip()))
    corpus["tone"] = tone_data
    return corpus

corpus = load_corpus()

# --- Logo 與標題 ---
st.image("jingsi_converted.png", width=200)
st.title("師徒之間｜AI 對話測試")
st.caption("請輸入問題或對話內容，我會以上人語風或慈濟知識回應")

# --- 使用者輸入 ---
query = st.text_input("請輸入問題", "")

# --- 模擬回答（tone or knowledge） ---
if query:
    if any(kw in query for kw in ["如何說話", "如何回應", "語氣", "開場", "慈悲"]):
        tone = random.choice(corpus["tone"])
        st.subheader("語風模擬回答")
        st.markdown(f"**Prompt:** {tone['prompt']}")
        st.markdown(f"**Completion:** {tone['completion']}")
    else:
        results = []
        for category, entries in corpus.items():
            if category == "tone": continue
            for e in entries:
                if query in e["text"]:
                    results.append((category, e["text"]))
        if results:
            st.subheader("知識語料回應")
            for cat, text in results[:3]:
                st.markdown(f"- [{cat}] {text}")
        else:
            st.warning("找不到相關語料，請重新輸入或擴充語料庫。")