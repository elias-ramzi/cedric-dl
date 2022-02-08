import torch


def mask_logsumexp(tens, mask, *args, **kwargs):
    tens[~mask] = -float('inf')
    return torch.logsumexp(tens, *args, **kwargs)
