import torch


def get_loader(
    dts,
    batch_size=256,
    pin_memory=True,
    num_workers=10,
    shuffle=False,
    drop_last=False,
    sampler=None,
    batch_sampler=None,
    **kwargs,
):
    if batch_sampler is not None:
        batch_size = None

    return torch.utils.data.DataLoader(
        dts,
        batch_size=batch_size,
        pin_memory=pin_memory,
        num_workers=num_workers,
        shuffle=shuffle,
        drop_last=drop_last,
        sampler=sampler,
        batch_sampler=batch_sampler,
        **kwargs,
    )
