#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
紫微斗数 Skill 打包脚本
将 skill 目录打包成 .skill 文件（ZIP 格式）
"""

import os
import zipfile
import sys


def main():
    skill_dir = "紫微斗数skill"
    output_file = "紫微斗数.skill"
    
    print("=" * 50)
    print("紫微斗数 Skill 打包工具")
    print("=" * 50)
    print()
    
    # 检查目录是否存在
    if not os.path.exists(skill_dir):
        print(f"错误: 找不到 '{skill_dir}' 目录")
        return 1
    
    # 检查 SKILL.md 是否存在
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(skill_md):
        print("错误: 找不到 'SKILL.md' 文件")
        return 1
    
    # 删除已存在的 .skill 文件
    if os.path.exists(output_file):
        print(f"删除已存在的文件: {output_file}")
        os.remove(output_file)
    
    print("正在打包 Skill 文件...")
    print(f"源目录: {skill_dir}")
    print(f"输出文件: {output_file}")
    print()
    
    try:
        # 创建 ZIP 文件
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 遍历目录
            for root, dirs, files in os.walk(skill_dir):
                for file in files:
                    # 构建相对路径
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, skill_dir)
                    
                    # 添加文件到 ZIP
                    zipf.write(file_path, arcname)
        
        # 检查文件大小
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            file_size_kb = file_size / 1024
            
            print("=" * 50)
            print("打包成功!")
            print("=" * 50)
            print(f"输出文件: {output_file}")
            print(f"文件大小: {file_size_kb:.2f} KB")
            print()
            return 0
        else:
            print("错误: 打包失败，输出文件不存在")
            return 1
            
    except Exception as e:
        print(f"错误: 打包失败 - {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
