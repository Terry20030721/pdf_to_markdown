# 📄 PDF to Markdown Converter

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pdftomarkdown-tjbcyqjbu4qb8qew6y3rzt.streamlit.app)

一個專業且直覺的 PDF 轉 Markdown 工具，專為 LLM 友善的格式化而設計。

## 🌟 特色功能

- **高品質轉換**：採用 `pymupdf4llm` 技術，精準提取 PDF 內容並轉換為 Markdown。
- **圖片自動提取**：自動識別並提取 PDF 中的圖片，並在 Markdown 中自動修正連結。
- **打包下載**：轉換完成後，可直接下載包含 Markdown 文件與 `images` 資料夾的 ZIP 壓縮檔。
- **簡潔介面**：基於 Streamlit 開發，操作簡單，支援即時預覽。

## 🚀 線上試用

直接造訪：[https://pdftomarkdown-tjbcyqjbu4qb8qew6y3rzt.streamlit.app](https://pdftomarkdown-tjbcyqjbu4qb8qew6y3rzt.streamlit.app)

## 🛠️ 本地開發與運行

### 1. 克隆專案
```bash
git clone https://github.com/Terry20030721/pdf_to_markdown.git
cd pdf_to_markdown
```

### 2. 安裝依萊
```bash
pip install -r requirements.txt
```

### 3. 啟動應用
```bash
streamlit run app.py
```

## 📂 專案結構

- `app.py`: Streamlit 應用程式的主進入點。
- `core/converter.py`: 核心轉檔邏輯，處理 PDF 解析與圖片路徑修正。
- `requirements.txt`: 專案所需的套件清單。

---

Made with ❤️ by [Terry](https://github.com/Terry20030721)
