import zipfile
import shutil
from pathlib import Path

# Your folder of SurveyMonkey zips goes here...
# ========================================================
zips_dir = Path(r"E:\local-pytyon-projects\bullets-chunks-paragraphs\data\2026-April9-SurveyData\zips")

for zip_path in sorted(zips_dir.glob("*.zip")):
    extract_dir = zips_dir / zip_path.stem

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_dir)

    # Find the "Review these" CSV inside the CSV subfolder
    csv_matches = list(extract_dir.glob("CSV/Review these*.csv"))
    if not csv_matches:
        print(f"WARNING: No 'Review these' CSV found in {zip_path.name}, skipping.")
        shutil.rmtree(extract_dir)
        continue

    source_csv = csv_matches[0]
    dest_csv = zips_dir / (zip_path.stem + ".csv")
    shutil.move(str(source_csv), dest_csv)
    print(f"{zip_path.name} -> {dest_csv.name}")

    shutil.rmtree(extract_dir)

print("Done.")
