def add_path_prefix_to_file(input_file_path, output_file_path, prefix):
    """
    为文本文件每一行添加指定路径前缀，并保存到新文件
    
    参数:
    input_file_path (str): 输入文件路径（原 train.txt 路径）
    output_file_path (str): 输出文件路径（处理后文件保存路径）
    prefix (str): 需添加的路径前缀
    """
    try:
        # 1. 读取原文件内容（按行读取，保留原始换行符）
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            # 读取所有行，去除每行首尾空白（避免空行或多余空格影响），过滤空行
            lines = [line.strip() for line in input_file if line.strip()]
        
        # 2. 为每一行添加路径前缀
        processed_lines = [f"{prefix}{line}\n" for line in lines]
        
        # 3. 将处理后的内容写入新文件
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.writelines(processed_lines)
        
        print(f"✅ 处理完成！")
        print(f"📥 原文件：{input_file_path}")
        print(f"📤 输出文件：{output_file_path}")
        print(f"📊 处理统计：共处理 {len(processed_lines)} 行数据，每行已添加前缀：{prefix}")
    
    except FileNotFoundError:
        print(f"❌ 错误：输入文件 '{input_file_path}' 未找到，请检查文件路径是否正确！")
    except PermissionError:
        print(f"❌ 错误：权限不足，无法读取输入文件或写入输出文件，请检查文件权限！")
    except Exception as e:
        print(f"❌ 处理过程中发生未知错误：{str(e)}")


if __name__ == "__main__":
    # -------------------------- 请根据实际情况修改以下路径 --------------------------
    INPUT_FILE = "nuscenes_test_depth_predicted.txt"          # 原文件路径（若文件不在脚本同目录，需写完整路径，如 "C:/data/train.txt" 或 "/home/user/train.txt"）
    OUTPUT_FILE = "nuscenes_test_depth_predicted.txt"  # 处理后文件保存路径（建议与原文件同目录）
    PATH_PREFIX = "/data/wwz/ZJU-4DRadarCam/data/radar_png/"  # 固定添加的路径前缀
    # -----------------------------------------------------------------------------
    
    # 调用函数执行处理
    add_path_prefix_to_file(INPUT_FILE, OUTPUT_FILE, PATH_PREFIX)