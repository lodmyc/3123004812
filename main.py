# main.py
import sys
from utils import calculate_similarity

def main():
    # 参数校验
    if len(sys.argv) != 4:
        print("Usage: python main.py [orig_path] [copy_path] [ans_path]")
        sys.exit(1)
    
    orig_path, copy_path, ans_path = sys.argv[1], sys.argv[2], sys.argv[3]
    
    try:
        # 计算相似度并写入结果
        similarity = calculate_similarity(orig_path, copy_path)
        with open(ans_path, 'w') as f:
            f.write(f"{similarity:.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
