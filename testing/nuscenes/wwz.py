def add_png_suffix(input_file, output_file):
    """
    为txt文件每一行末尾添加.png后缀（若未存在），并保存到新文件
    
    参数:
    input_file (str): 输入txt文件路径（如train.txt）
    output_file (str): 输出txt文件路径（处理后保存的文件）
    """
    try:
        # 读取原文件内容
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]  # 去空行+去首尾空白
        
        # 处理每一行：添加.png后缀（避免重复添加）
        processed_lines = []
        for line in lines:
            if not line.endswith('.png'):
                processed_line = f"{line}.png"
            else:
                processed_line = line  # 已存在后缀则保留原内容
            processed_lines.append(processed_line)
        
        # 写入新文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(processed_lines))
        
        print(f"✅ 处理完成！")
        print(f"📥 原文件：{input_file}")
        print(f"📤 输出文件：{output_file}")
        print(f"📊 处理统计：共处理 {len(processed_lines)} 行，每行已添加/保留.png后缀")
    
    except FileNotFoundError:
        print(f"❌ 错误：文件 '{input_file}' 未找到，请检查路径！")
    except PermissionError:
        print(f"❌ 错误：权限不足，无法读取/写入文件！")
    except Exception as e:
        print(f"❌ 未知错误：{str(e)}")


if __name__ == "__main__":
    # -------------------------- 请修改以下路径 --------------------------
    INPUT_TXT = "nuscenes_test_depth_predicted.txt"       # 你的原始txt文件路径（如：/data/wwz/train.txt）
    OUTPUT_TXT = "nuscenes_test_depth_predicted.txt"  # 处理后的输出文件路径
    # -------------------------------------------------------------------
    
    add_png_suffix(INPUT_TXT, OUTPUT_TXT)