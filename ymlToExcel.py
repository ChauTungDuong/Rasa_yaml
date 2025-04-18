import yaml
import pandas as pd
import re
import os

# === ⚙️ Cấu hình: Chỉnh đường dẫn tại đây ===
input_yml_path = r"data\nlu.yml"       # 📥 Đường dẫn file YAML đầu vào
output_excel_path = r"C:\Users\duong\Downloads\abc\intent.xlsx"  # 📤 Đường dẫn file Excel đầu ra

# === 🏷️ Tên cột bạn muốn có trong Excel ===
columns = ["name", "examples"]

# === ✅ Kiểm tra file tồn tại ===
if not os.path.exists(input_yml_path):
    print(f"❌ File không tồn tại: {input_yml_path}")
    exit()

# === 📖 Đọc file YAML ===
with open(input_yml_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# === 🧹 Xử lý dữ liệu từ phần 'nlu' ===
records = []
for item in data.get("nlu", []):
    row = {}
    row["name"] = item.get("intent", "")
    
    # Gộp các dòng examples thành một dòng, ngăn cách bởi ';'
    examples_raw = item.get("examples", "")
    if isinstance(examples_raw, str):
        lines = re.findall(r"-\s*(.+)", examples_raw)
        row["examples"] = ";".join([line.strip() for line in lines])
    else:
        row["examples"] = ""
    
    records.append(row)

# === 📤 Ghi dữ liệu ra file Excel ===
df = pd.DataFrame(records, columns=columns)
df.to_excel(output_excel_path, index=False)

print(f"✅ Đã chuyển YAML thành Excel: {output_excel_path}")
