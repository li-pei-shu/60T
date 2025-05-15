# 🧘‍ 師徒之間 GPT 對話系統 | V4 語氣修正版

本專案模擬慈濟證嚴法師語氣，以《菩提心要2024》為唯一語調母語料，實現近似上人口說節奏、語助詞使用、收束語氣的智慧對話系統。

---

## ✨ V4 語氣修正版特色

- ✅ 去除「阿彌陀佛」等非自然開頭
- ✅ 主詞轉化（我／我們 → 師父）
- ✅ 避免第一人稱頻繁使用，改以無主體敘述
- ✅ 自動插入語助詞：「總是呢」「安捏──」「汝知道嗎？」
- ✅ 收尾語句自然如：「念若靜，事自明。」「慢慢來啊」
- ✅ 對佛經問句不附祝福語，僅給法義回答

---

## 🛠️ 使用方式（本地執行）

```bash
pip install -r requirements.txt
streamlit run streamlit_gpt_disciple_final_emotive_v4_fixed.py
```

---

## 📁 檔案結構說明

| 檔案 | 說明 |
|------|------|
| streamlit_gpt_disciple_final_emotive_v4_fixed.py | 主程式 |
| requirements.txt | 所需套件 |
| data/語尾庫_V4_fixed.json | 節奏語氣庫 |
| data/語氣模擬樣例_V4_fixed.txt | 語氣模擬測試範例 |
| data/E-gpt_demo_corpus_part*.json | GPT 使用語料庫 |

---

## 📜 授權聲明

本專案以人文教育、語氣重建為宗旨，所模擬語句非實際語錄，為基於慈濟開放語料之智慧語言模擬成果。嚴禁用於商業用途。