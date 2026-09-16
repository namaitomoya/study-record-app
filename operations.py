from datetime import datetime
from study_record_app.models import StudyRecord
from storage import save_records







def add_record(records):
    while True:
        input_date = input("日付をYYYY-MM-DD形式で入力してください：").strip()

        if input_date == "":
            print("日付を入力してください")
        else:
            try:
                datetime.strptime(input_date, "%Y-%m-%d")
                break
            except ValueError:
                print("正しい日付を入力してください")

    while True:
        input_subject = input("科目を入力してください：").strip()

        if input_subject == "":
            print("科目を入力してください")
        else:
            break

    while True:
        input_study_time = input("勉強時間を入力してください：")

        try:
            input_study_time = int(input_study_time)

            if input_study_time < 1:
                raise ValueError

            break
        except ValueError:
            print("1以上の整数を入力してください")

    new_record = StudyRecord(
        input_date,
        input_subject,
        input_study_time
    )

    records.append(new_record)
    save_records(records)
    print("記録が完了しました")


def show_records(records):
    if records == []:
        print("記録がありません")
    else:
        for index, record in enumerate(records):
            print(
                f"{index + 1}.\n"
                f"日付：{record.date}\n"
                f"科目：{record.subject}\n"
                f"勉強時間：{record.study_time}分"
            )


def delete_record(records):
    if records == []:
        print("削除できる記録がありません")
    else:
        show_records(records)

        try:
            delete_number = int(input("削除する番号を入力してください："))

            if 1 <= delete_number <= len(records):
                records.pop(delete_number - 1)
                save_records(records)
                print("削除しました")
            else:
                raise IndexError("存在する記録番号を入力してください")

        except IndexError as error:
            print(error)
        except ValueError:
            print("整数で入力してください")


def total_time(records):
    total = 0

    if records == []:
        print("記録がありません")
    else:
        for record in records:
            total += record.study_time

        print(f"合計学習時間：{total}分")


def subject_total(records):
    total = 0
    subject_found = False

    if records == []:
        print("記録がありません")
    else:
        input_subject = input("科目を選択してください：").strip()

        for record in records:
            if record.subject == input_subject:
                total += record.study_time
                subject_found = True

        if subject_found:
            print(f"{input_subject}の合計時間：{total}分")
        else:
            print("その科目の記録はありません")