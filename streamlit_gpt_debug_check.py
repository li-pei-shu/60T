import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="語料載入檢查", page_icon="🔍", layout="centered")
st.title("🛠️ 語料讀取 Debug 模式")

# 檢查語料目錄結構
base_path = Path(__file__).parent / "corpus"
tone_path = base_path / "tone" / "tone_dataset.jsonl"
knowledge_path = base_path / "knowledge"

# --- 擬態語料檢查 ---
st.header("1️⃣ 擬態語料載入檢查")
if tone_path.exists():
    try:
        tone_lines = tone_path.read_text(encoding="utf-8").strip().splitlines()
        st.success(f"✅ tone_dataset.jsonl 已讀取，共 {len(tone_lines)} 筆")
    except Exception as e:
        st.error(f"❌ 無法讀取 tone_dataset.jsonl：{e}")
else:
    st.warning("⚠️ 找不到 tone_dataset.jsonl，請確認檔案是否在 corpus/tone 資料夾中")

# --- 知識型語料檢查 ---
st.header("2️⃣ 知識型語料載入檢查")
categories = ["charity", "education", "humanism", "medical"]
for cat in categories:
    fpath = knowledge_path / f"{cat}_dataset.json"
    if fpath.exists():
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
                st.success(f"✅ {cat}_dataset.json 已讀取，共 {len(data)} 筆")
        except Exception as e:
            st.error(f"❌ 無法讀取 {cat}_dataset.json：{e}")
    else:
        st.warning(f"⚠️ 找不到 {cat}_dataset.json，請確認檔案是否已放置於 corpus/knowledge/")