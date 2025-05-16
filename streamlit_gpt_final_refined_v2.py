import streamlit as st
import json
from pathlib import Path
import difflib

st.set_page_config(page_title="師徒之間 AI", page_icon="🧘", layout="centered")
st.title("師徒之間｜語氣擬態 × 慈濟知識")

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

# --- 使用者輸入 ---
query = st.text_input("請輸入問題", "")

# --- 主功能 ---
if query:
    st.markdown("## 🔍 搜尋結果")

    # --- Tone 語風應用 ---
    if any(kw in query for kw in ["語氣", "開場", "收束", "語助詞", "說話方式"]):
        if corpus["tone"]:
            import random
            tone = random.choice(corpus["tone"])
            st.subheader("🗣️ 擬態語氣模擬")
            st.markdown(f"**Prompt:** {tone['prompt']}")
            st.markdown(f"**Completion:** {tone['completion']}")
        else:
            st.warning("⚠️ 擬態語料尚未載入")

    # --- Knowledge 語意模糊搜尋 ---
    else:
        results = []
        for category, entries in corpus.items():
            if category == "tone":
                continue
            for e in entries:
                score = difflib.SequenceMatcher(None, query, e["text"]).ratio()
                if score > 0.4:
                    results.append((score, category, e["text"]))
        results = sorted(results, reverse=True)[:3]

        if results:
            st.subheader("📚 最相近語料段落")
            for score, cat, text in results:
                st.markdown(f"- [{cat}] {text}")
        else:
            st.info("⚠️ 未找到類似語料，請嘗試其他問題或擴充語料庫。")