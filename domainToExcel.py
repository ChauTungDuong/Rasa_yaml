import yaml
import pandas as pd
import json

# Đọc file domain.yml
with open('domain.yml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)

# Xử lý responses
responses = data.get('responses', {})
response_rows = []
for name, examples in responses.items():
    texts = []
    for item in examples:
        if isinstance(item, dict) and 'text' in item:
            texts.append(item['text'])
        elif isinstance(item, str):
            texts.append(item)
    response_rows.append({
        'name': name,
        'examples': ' ; '.join(texts)
    })

# Ghi responses ra file Excel
df_responses = pd.DataFrame(response_rows)
df_responses.to_excel('response.xlsx', index=False, engine='openpyxl')
# Xử lý entities
entities = data.get('entities', [])
entity_rows = []
for entity in entities:
    # Nếu entity là chuỗi đơn giản
    if isinstance(entity, str):
        entity_rows.append({
            'name': entity,
            'type': '',
            'examples': '',
            'regexPattern': ''
        })
    elif isinstance(entity, dict):  # Nếu entity có chi tiết như type, examples, regexPattern
        for name, details in entity.items():
            regexPattern = details.get('regexPattern', '')
            examples = details.get('examples', '')
            entity_rows.append({
                'name': name,
                'type': details.get('type', ''),
                'examples': examples,
                'regexPattern': regexPattern
            })

# Ghi entities ra file Excel
df_entities = pd.DataFrame(entity_rows)
df_entities.to_excel('entity.xlsx', index=False, engine='openpyxl')

print("✅ Đã ghi ra file 'response.xlsx' và 'entity.xlsx' thành công.")
