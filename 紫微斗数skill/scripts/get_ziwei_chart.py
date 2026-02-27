import sys
import json
import os

# 添加当前目录到路径，确保能导入算命模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from 算命 import start

def main():
    if len(sys.argv) != 3:
        print(json.dumps({"error": "参数错误，需要提供出生时间(格式：YYYYMMDDHH)和性别(M/F)"}))
        return
    
    try:
        birth_time = int(sys.argv[1])
        gender = sys.argv[2]
        
        if gender not in ["M", "F"]:
            print(json.dumps({"error": "性别参数错误，应为M(男)或F(女)"}))
            return
        
        # 调用算命模块获取命盘
        chart_data = start(birth_time, gender)
        
        # 输出结果
        print(json.dumps({"success": True, "chart": chart_data}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()