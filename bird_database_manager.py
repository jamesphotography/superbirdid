#!/usr/bin/env python3
"""
鸟类数据库管理器
使用SQLite数据库替代JSON文件，提供完整的鸟类信息和eBird映射
"""
import sqlite3
import os
from typing import List, Dict, Optional, Tuple, Set
import json

class BirdDatabaseManager:
    def __init__(self, db_path: str = None):
        """
        初始化鸟类数据库管理器
        
        Args:
            db_path: SQLite数据库路径，默认为当前目录下的bird_reference.sqlite
        """
        if db_path is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(script_dir, 'bird_reference.sqlite')
        
        self.db_path = db_path
        
        # 检查数据库文件是否存在
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"数据库文件不存在: {db_path}")
        
        # 测试数据库连接
        self._test_connection()
        
        print(f"BirdDatabaseManager initialized with database: {db_path}")
    
    def _test_connection(self):
        """测试数据库连接"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM BirdCountInfo")
                count = cursor.fetchone()[0]
                print(f"数据库连接成功，包含 {count} 条鸟类记录")
        except Exception as e:
            raise ConnectionError(f"数据库连接失败: {e}")
    
    def get_bird_by_class_id(self, class_id: int) -> Optional[Dict]:
        """
        根据模型类别ID获取鸟类信息

        Args:
            class_id: 鸟类类别ID（对应模型输出的索引）

        Returns:
            包含鸟类信息的字典，如果未找到返回None
        """
        # class_id对应数据库中的model_class_id字段
        query = """
        SELECT id, english_name, chinese_simplified, chinese_traditional,
               scientific_name, ebird_code, short_description_zh, full_description_zh
        FROM BirdCountInfo
        WHERE model_class_id = ?
        """

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query, (class_id,))
                result = cursor.fetchone()

                if result:
                    return {
                        'id': result[0],
                        'english_name': result[1],
                        'chinese_simplified': result[2],
                        'chinese_traditional': result[3],
                        'scientific_name': result[4],
                        'ebird_code': result[5],
                        'short_description_zh': result[6],
                        'full_description_zh': result[7]
                    }
                return None
        except Exception as e:
            print(f"查询鸟类信息失败 (class_id: {class_id}): {e}")
            return None
    
    def get_ebird_code_by_english_name(self, english_name: str) -> Optional[str]:
        """
        根据英文名获取eBird代码
        
        Args:
            english_name: 英文鸟类名称
            
        Returns:
            eBird代码，如果未找到返回None
        """
        query = """
        SELECT ebird_code 
        FROM BirdCountInfo 
        WHERE english_name = ? AND ebird_code IS NOT NULL
        """
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query, (english_name,))
                result = cursor.fetchone()
                return result[0] if result else None
        except Exception as e:
            print(f"查询eBird代码失败 (名称: {english_name}): {e}")
            return None
    
    def get_birds_by_ebird_codes(self, ebird_codes: Set[str]) -> List[Dict]:
        """
        根据eBird代码集合获取鸟类信息
        
        Args:
            ebird_codes: eBird代码集合
            
        Returns:
            匹配的鸟类信息列表
        """
        if not ebird_codes:
            return []
        
        # 构建IN查询的占位符
        placeholders = ','.join('?' * len(ebird_codes))
        query = f"""
        SELECT id, english_name, chinese_simplified, ebird_code
        FROM BirdCountInfo 
        WHERE ebird_code IN ({placeholders})
        """
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query, list(ebird_codes))
                results = cursor.fetchall()
                
                return [
                    {
                        'id': row[0],
                        'english_name': row[1],
                        'chinese_simplified': row[2],
                        'ebird_code': row[3]
                    }
                    for row in results
                ]
        except Exception as e:
            print(f"批量查询eBird代码失败: {e}")
            return []
    
    def search_birds(self, query: str, limit: int = 10) -> List[Dict]:
        """
        搜索鸟类（支持中英文名称和学名）
        
        Args:
            query: 搜索查询
            limit: 返回结果数量限制
            
        Returns:
            匹配的鸟类信息列表
        """
        search_query = """
        SELECT id, english_name, chinese_simplified, ebird_code, scientific_name
        FROM BirdCountInfo 
        WHERE english_name LIKE ? 
           OR chinese_simplified LIKE ? 
           OR scientific_name LIKE ?
        LIMIT ?
        """
        
        search_term = f"%{query}%"
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(search_query, (search_term, search_term, search_term, limit))
                results = cursor.fetchall()
                
                return [
                    {
                        'id': row[0],
                        'english_name': row[1],
                        'chinese_simplified': row[2],
                        'ebird_code': row[3],
                        'scientific_name': row[4]
                    }
                    for row in results
                ]
        except Exception as e:
            print(f"搜索鸟类失败: {e}")
            return []
    
    def get_all_ebird_codes(self) -> Set[str]:
        """
        获取所有eBird代码
        
        Returns:
            所有eBird代码的集合
        """
        query = """
        SELECT DISTINCT ebird_code 
        FROM BirdCountInfo 
        WHERE ebird_code IS NOT NULL AND ebird_code != ''
        """
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
                return {row[0] for row in results}
        except Exception as e:
            print(f"获取所有eBird代码失败: {e}")
            return set()
    
    def get_bird_data_for_model(self) -> List[List[str]]:
        """
        获取模型所需的鸟类数据格式（兼容原有的birdinfo.json格式）
        
        Returns:
            List[List[str]]: [[中文名, 英文名], ...] 格式的数据
        """
        query = """
        SELECT chinese_simplified, english_name
        FROM BirdCountInfo 
        ORDER BY id
        """
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
                return [[row[0], row[1]] for row in results]
        except Exception as e:
            print(f"获取模型数据失败: {e}")
            return []
    
    def get_statistics(self) -> Dict:
        """
        获取数据库统计信息
        
        Returns:
            统计信息字典
        """
        queries = {
            'total_birds': "SELECT COUNT(*) FROM BirdCountInfo",
            'birds_with_ebird_codes': "SELECT COUNT(*) FROM BirdCountInfo WHERE ebird_code IS NOT NULL AND ebird_code != ''",
            'unique_ebird_codes': "SELECT COUNT(DISTINCT ebird_code) FROM BirdCountInfo WHERE ebird_code IS NOT NULL AND ebird_code != ''",
            'birds_with_descriptions': "SELECT COUNT(*) FROM BirdCountInfo WHERE short_description_zh IS NOT NULL",
        }
        
        stats = {}
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                for key, query in queries.items():
                    cursor.execute(query)
                    stats[key] = cursor.fetchone()[0]
        except Exception as e:
            print(f"获取统计信息失败: {e}")
            return {}
        
        return stats
    
    def check_species_in_region(self, scientific_name: str, region: str = None) -> bool:
        """
        检查物种是否在指定区域出现（简化版本，仅检查物种是否存在于数据库）

        Args:
            scientific_name: 物种学名
            region: 地理区域（暂未使用，保留用于未来扩展）

        Returns:
            True如果物种存在于数据库，否则False
        """
        query = """
        SELECT COUNT(*)
        FROM BirdCountInfo
        WHERE scientific_name = ?
        """

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(query, (scientific_name,))
                count = cursor.fetchone()[0]
                return count > 0
        except Exception as e:
            print(f"检查物种区域失败 (学名: {scientific_name}): {e}")
            return False

    def validate_ebird_codes_with_country(self, ebird_species_set: Set[str]) -> Dict:
        """
        验证eBird代码与国家物种列表的匹配情况

        Args:
            ebird_species_set: 国家物种eBird代码集合

        Returns:
            验证结果字典
        """
        if not ebird_species_set:
            return {"error": "Empty eBird species set"}

        # 获取数据库中的所有eBird代码
        db_codes = self.get_all_ebird_codes()

        # 计算匹配情况
        matched_codes = ebird_species_set.intersection(db_codes)
        unmatched_in_country = ebird_species_set - db_codes
        unmatched_in_db = db_codes - ebird_species_set

        return {
            "country_species_total": len(ebird_species_set),
            "database_species_total": len(db_codes),
            "matched_species": len(matched_codes),
            "match_rate": len(matched_codes) / len(ebird_species_set) * 100 if ebird_species_set else 0,
            "unmatched_in_country": len(unmatched_in_country),
            "unmatched_in_database": len(unmatched_in_db),
            "sample_matched": list(matched_codes)[:10],
            "sample_unmatched_country": list(unmatched_in_country)[:10]
        }


def test_bird_database_manager():
    """测试鸟类数据库管理器"""
    try:
        # 初始化管理器
        db_manager = BirdDatabaseManager()
        
        print("\n=== 数据库统计信息 ===")
        stats = db_manager.get_statistics()
        for key, value in stats.items():
            print(f"{key}: {value}")
        
        print("\n=== 测试根据英文名获取eBird代码 ===")
        test_names = ["Australian Magpie", "House Sparrow", "Laughing Kookaburra", "Galah"]
        for name in test_names:
            code = db_manager.get_ebird_code_by_english_name(name)
            print(f"{name}: {code}")
        
        print("\n=== 测试搜索功能 ===")
        search_results = db_manager.search_birds("magpie", limit=5)
        for bird in search_results:
            print(f"ID: {bird['id']}, 中文: {bird['chinese_simplified']}, 英文: {bird['english_name']}, eBird: {bird['ebird_code']}")
        
        print("\n=== 测试根据类别ID获取鸟类信息 ===")
        bird_info = db_manager.get_bird_by_class_id(1)
        if bird_info:
            print(f"类别ID 1: {bird_info['chinese_simplified']} ({bird_info['english_name']}) - {bird_info['ebird_code']}")
        
        print("\n=== 测试模型数据格式 ===")
        model_data = db_manager.get_bird_data_for_model()
        print(f"模型数据样例 (前5条): {model_data[:5]}")
        
    except Exception as e:
        print(f"测试失败: {e}")


if __name__ == "__main__":
    test_bird_database_manager()