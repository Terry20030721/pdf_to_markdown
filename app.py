import streamlit as st
import tempfile
import os
import shutil
import zipfile
from core.converter import process_pdf_with_images # 假設你更新了核心邏輯名

st.set_page_config(page_title="PDF 轉 Markdown 工具", layout="wide")
st.title("📄 專業 PDF 轉檔工具 (含圖片提取)")

uploaded_file = st.file_uploader("請上傳 PDF 檔案", type="pdf")

if uploaded_file:
    # 1. 建立一個專屬的任務工作目錄
    # 使用 session_id 或隨機碼確保多使用者同時操作時不會互相干擾
    with tempfile.TemporaryDirectory() as tmp_dir:
        input_path = os.path.join(tmp_dir, "input.pdf")
        output_folder = os.path.join(tmp_dir, "output")
        os.makedirs(output_folder, exist_ok=True)
        
        # 寫入上傳的 PDF
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        if st.button("🚀 開始轉換並準備下載"):
            with st.spinner("正在解析 PDF 並提取圖片..."):
                try:
                    # 2. 呼叫核心功能 (確保你的 core 邏輯會把圖片存到 output_folder/images)
                    # 我們假設這個 function 會回傳 Markdown 文字
                    md_text = process_pdf_with_images(input_path, output_folder)
                    
                    # 將 Markdown 內容存成檔案
                    md_filename = f"{os.path.splitext(uploaded_file.name)[0]}.md"
                    with open(os.path.join(output_folder, md_filename), "w", encoding="utf-8") as f:
                        f.write(md_text)
                    
                    # 3. 將整個 output 資料夾打包成 ZIP
                    zip_path = os.path.join(tmp_dir, "converted_files.zip")
                    shutil.make_archive(os.path.join(tmp_dir, "converted_files"), 'zip', output_folder)
                    
                    st.success("轉換完成！")
                    
                    # 4. 介面呈現與下載
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("### 📄 Markdown 預覽")
                        st.text_area("內容", md_text, height=400)
                    
                    with col2:
                        st.markdown("### 📦 下載結果")
                        with open(zip_path, "rb") as fp:
                            st.download_button(
                                label="💾 下載全部檔案 (ZIP)",
                                data=fp,
                                file_name=f"{os.path.splitext(uploaded_file.name)[0]}_converted.zip",
                                mime="application/zip"
                            )
                        st.info("ZIP 檔內包含 Markdown 文件與自動提取的 images 資料夾。")

                except Exception as e:
                    st.error(f"發生錯誤：{e}")