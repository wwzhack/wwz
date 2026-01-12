import torch
import os

print("="*50)
print(f"CUDA_VISIBLE_DEVICES: {os.environ.get('CUDA_VISIBLE_DEVICES', '未设置')}")
print(f"PyTorch CUDA可用: {torch.cuda.is_available()}")
print(f"可用GPU数量: {torch.cuda.device_count()}")
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i} 名称: {torch.cuda.get_device_name(i)}")
print("="*50)