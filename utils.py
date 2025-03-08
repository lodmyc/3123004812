import re
import jieba
from simhash import Simhash

def read_file(file_path: str) -> str:
    """读取文件内容并处理IO异常"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件 {file_path} 不存在")
    except IOError:
        raise IOError(f"无法读取文件 {file_path}")

def preprocess(text: str) -> str:
    """文本预处理：去标点 + 分词"""
    text_clean = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', text)
    return ' '.join(jieba.lcut(text_clean))  # 分词后拼接为字符串

def calculate_similarity(orig_text: str, copy_text: str) -> float:
    """基于SimHash计算重复率"""
    # 空文件处理
    if not orig_text and not copy_text:
        return 1.0
    if not orig_text or not copy_text:
        return 0.0

    # 生成SimHash指纹
    orig_hash = Simhash(preprocess(orig_text))
    copy_hash = Simhash(preprocess(copy_text))

    # 计算汉明距离并转换为相似度
    distance = orig_hash.distance(copy_hash)
    return 1 - distance / 64  # SimHash指纹为64位
