import json
from pathlib import Path
from models import StudyRecord

base_directory = Path(__file__).resolve().parent
data_directory = base_directory / "data"
data_directory.mkdir(exist_ok=True)
json_file = data_directory / "study_record.json"

def save_records(records):
    records_to_json = []

    for record in records:
        record_dict = record.to_dict()
        records_to_json.append(record_dict)

    with json_file.open("w", encoding="utf-8") as file:
        json.dump(
            records_to_json,
            file,
            ensure_ascii=False,
            indent=4
        )

def load_records():
    records_from_json = []

    try:
        with json_file.open("r", encoding="utf-8") as file:
            for record_dict in json.load(file):
                record = StudyRecord(
                    record_dict["date"],
                    record_dict["subject"],
                    record_dict["study_time"]
                )
                records_from_json.append(record)

        return records_from_json

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("保存ファイルの内容が壊れています")
        return []