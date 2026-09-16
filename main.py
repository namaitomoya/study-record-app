from storage import save_records,load_records
from operations import add_record,show_records,delete_record,total_time,subject_total


def main():
    records = load_records()

    while True:
        print()
        print("===== 学習記録アプリ =====")
        print("1. 記録を追加")
        print("2. 記録を一覧表示")
        print("3. 記録を削除")
        print("4. 合計時間を表示")
        print("5. 科目別の合計時間を表示")
        print("6. 終了")

        chosen_number = input("番号を選択してください：")

        if chosen_number == "1":
            add_record(records)
        elif chosen_number == "2":
            show_records(records)
        elif chosen_number == "3":
            delete_record(records)
        elif chosen_number == "4":
            total_time(records)
        elif chosen_number == "5":
            subject_total(records)
        elif chosen_number == "6":
            save_records(records)
            print("終了します")
            break
        else:
            print("1から6を選択してください")


if __name__ == "__main__":
    main()



    




