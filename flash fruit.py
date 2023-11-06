import os

# 存储文本的文件
storage_file = "text_storage.txt"

# 创建存储文件（如果不存在）
if not os.path.exists(storage_file):
    with open(storage_file, "w") as file:
        file.write("")

def save_text(text):
    # 追加文本到存储文件
    with open(storage_file, "a") as file:
        file.write(text + "\n")
    print("文本已保存。")

def retrieve_text():
    # 从存储文件中检索所有文本
    with open(storage_file, "r") as file:
        text = file.read()
    return text

def main():
    while True:
        print("文字存储系统")
        print("1. 存储文本")
        print("2. 检索文本")
        print("3. 退出")
        choice = input("请选择操作 (1/2/3): ")

        if choice == "1":
            text = input("请输入要存储的文本: ")
            save_text(text)
        elif choice == "2":
            stored_text = retrieve_text()
            if stored_text:
                print("存储的文本:")
                print(stored_text)
            else:
                print("没有存储的文本。")
        elif choice == "3":
            break
        else:
            print("无效的选项，请重新选择。")

if __name__ == "__main__":
    main()