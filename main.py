import sys
from utils import read_file, calculate_similarity

def main():
    # 检查命令行参数数量
    if len(sys.argv) != 4:
        print("Usage: python main.py [原文件] [抄袭文件] [输出文件]")
        sys.exit(1)

    orig_path, copy_path, ans_path = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # 读取文件内容
        orig_text = read_file(orig_path)
        copy_text = read_file(copy_path)

        # 计算相似度
        similarity = calculate_similarity(orig_text, copy_text)

        # 写入结果文件
        with open(ans_path, 'w', encoding='utf-8') as f:
            f.write(f"{similarity:.2f}")
    except Exception as e:
        print(f"错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
