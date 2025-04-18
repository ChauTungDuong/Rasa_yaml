import yaml
import pandas as pd
import json

# Đọc file stories.yml
with open('stories.yml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)

# Lấy danh sách stories
stories = data.get('stories', [])

# Chuyển dữ liệu sang list phù hợp
rows = []
for story in stories:
    name = story.get('story', 'unnamed')
    steps = story.get('steps', [])

    # Giữ nguyên cấu trúc steps (kể cả entities), rồi chuyển thành chuỗi JSON
    steps_json = json.dumps(steps, ensure_ascii=False)

    rows.append({
        'name': name,
        'steps': steps_json
    })

# Ghi ra file Excel
df = pd.DataFrame(rows)
df.to_excel('stories_output.xlsx', index=False, engine='openpyxl')

print("✅ Đã chuyển file 'stories.yml' sang 'stories_output.xlsx' thành công.")
