import pymupdf4llm
import os
import re
import shutil

def process_pdf_with_images(pdf_path, output_dir):
    """
    pdf_path: PDF 檔案路徑
    output_dir: 轉換結果要存放的資料夾
    """
    # 指定圖片存放的子資料夾名稱
    image_subdir = "images"
    image_full_path = os.path.join(output_dir, image_subdir)
    
    # 如果資料夾不存在就建立它
    if not os.path.exists(image_full_path):
        os.makedirs(image_full_path)

    # 【強制手段】
    # 1. 記錄轉換前專案根目錄下的所有檔案
    project_root = os.getcwd()
    files_before = set(os.listdir(project_root))

    # 2. 執行轉換，此時圖片會被錯誤地儲存到 project_root
    md_text = pymupdf4llm.to_markdown(
        pdf_path,
        write_images=True,
        # 即使 image_dest 可能失效，依然保留以防萬一
        image_dest=image_full_path,
    )

    # 3. 記錄轉換後的檔案列表，找出新增的圖片
    files_after = set(os.listdir(project_root))
    new_files = files_after - files_before

    # 4. 將這些新圖片移動到正確的目的地
    for filename in new_files:
        # 透過副檔名判斷是否為圖片，避免移動到其他非預期檔案
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            src_path = os.path.join(project_root, filename)
            dest_path = os.path.join(image_full_path, filename)
            shutil.move(src_path, dest_path)

    # 5. 後處理 Markdown 文字，修正圖片路徑 (此步驟依然重要)
    def replace_path(match):
        alt_text = match.group(1)
        filename = os.path.basename(match.group(2))
        return f"![{alt_text}]({image_subdir}/{filename})"

    md_text = re.sub(r"!\[(.*?)\]\(file://(.*?)\)", replace_path, md_text)
    
    return md_text
