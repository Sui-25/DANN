import torch, sys
print("torch:", torch.__version__)
print("compiled CUDA:", getattr(torch.version, "cuda", None))
print("cuda available:", torch.cuda.is_available())
print("cuda device count:", torch.cuda.device_count())
if torch.cuda.is_available():
    print("current device:", torch.cuda.current_device(), torch.cuda.get_device_name(torch.cuda.current_device()))
    