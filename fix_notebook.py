import json
import os

filename = 'HCNNVIT_ADF.ipynb'

print(f"🔧 Attempting to fix {filename}...")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Clean Top-Level Metadata (where the error usually lives)
    if 'widgets' in data.get('metadata', {}):
        del data['metadata']['widgets']
        print(" - Removed top-level widget metadata.")
    
    # 2. Clean Cell-Level Metadata (just in case)
    cleaned_cells = 0
    for cell in data.get('cells', []):
        if 'widgets' in cell.get('metadata', {}):
            del cell['metadata']['widgets']
            cleaned_cells += 1
    
    if cleaned_cells > 0:
        print(f" - Removed widget metadata from {cleaned_cells} cells.")

    # 3. Save it back
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1)
    
    print("✅ Done! File saved. You can now git push.")

except Exception as e:
    print(f"❌ Error: {e}")
