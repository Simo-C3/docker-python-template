import torch

print(f"Torchバージョン：{torch.__version__}")
print(f"GPUの利用可否：{torch.cuda.is_available()}")
print(f"GPU数：{torch.cuda.device_count()}")
print(f"デフォルトGPU：{torch.cuda.current_device()}")
