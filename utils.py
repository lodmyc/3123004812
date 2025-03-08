# utils.py
import re
import jieba
from simhash import Simhash

def read_file(path: str) -> str:
    """安全读取文件内容"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().replace('\n', '')
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
    except Exception as e:
        raise RuntimeError(f"Error reading {path}: {str(e)}")

def preprocess(text: str) -> list:
    """文本预处理：清洗+分词"""
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', text)
    return list(jieba.cut(text))

def get_simhash(text: str) -> Simhash:
    """生成Simhash指纹"""
    features = [' '.join(ngram) for ngram in zip(*[text[i:] for i in range(3)])]
    return Simhash(features)

def calculate_similarity(orig_path: str, copy_path: str) -> float:
    """计算两文件相似度"""
    orig_text = read_file(orig_path)
    copy_text = read_file(copy_path)
    
    # 空文件处理
    if not orig_text and not copy_text:
        return 1.0
    if not orig_text or not copy_text:
        return 0.0
    
    # 生成指纹
    orig_hash = get_simhash(preprocess(orig_text))
    copy_hash = get_simhash(preprocess(copy_text))
    
    # 计算汉明距离
    distance = orig_hash.distance(copy_hash)
    return 1 - distance / 64  # Simhash位数为64
