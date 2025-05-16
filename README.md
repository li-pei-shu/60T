# 上人AI 語料總庫（corpus）

本資料庫分為兩大語料組，用於上人語風模擬與知識性對話建構。

## 📘 語料分類結構

```
/corpus/
├── tone/
│   └── tone_dataset.jsonl              # 擬態語料組
└── knowledge/
    ├── charity_dataset.json           # 慈善類
    ├── education_dataset.json         # 教育類
    ├── humanism_dataset.json          # 人文類
    └── medical_dataset.json           # 醫療類（空佔位）
```

## 📊 筆數摘要與 SHA256 驗證

| 類別 | 檔案名稱 | 筆數 | SHA256 雜湊碼 |
|------|------------|------|--------------------------------------------------|
| 擬態 | tone_dataset.jsonl | 9034 | 22237846ffcf3ee677e20b60ec1d79d3bc4e4eb7d4c674dbe2b1d58f8ee2f1ba |
| 慈善 | charity_dataset.json | 130317 | 417b3a1e6859668b634c147b5ebda42fb2441fcf2b4cc63bf8a77a26e7635f08 |
| 教育 | education_dataset.json | 2197 | c1ee795f95c091ef6eb8398340918cd9b3a7bde3c52669f74e6fd8c92905a0cd |
| 人文 | humanism_dataset.json | 10674 | 460eb8bcab2cc2603413e34bbaf8d38dc571324cff44d09a672525f414ae0459 |
| 醫療 | medical_dataset.json | 0 | d751713988987e9331980363e24189ce |

## 🧾 用途說明

- `tone/` 下資料用於 GPT 擬態語風（prompt-completion 訓練）
- `knowledge/` 下語料用於主題式知識回答與查詢
- 所有語料皆帶 `metadata.category` 方便檢索與語意處理