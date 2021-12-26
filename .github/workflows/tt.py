import torch_cluster as tc

try:
    print(tc.cuda_version)
except AttributeError as err:
    print("Att no cuda")
