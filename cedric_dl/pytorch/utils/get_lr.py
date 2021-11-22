def get_lr(optimizer, return_scalar=False):
    all_lr = {}
    for i, param_group in enumerate(optimizer.param_groups):
        all_lr[i] = param_group['lr']

    if return_scalar:
        return list(all_lr.values())[0]

    return all_lr
