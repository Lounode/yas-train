config = {
    "height": 32,
    "train_width": 384,
    "batch_size": 32,
    "epoch": 10,
    "print_per": 100,
    "save_per": 300,

    "train_size": 20000,
    "validate_size": 10000,

    "pretrain": False,
    "pretrain_name": "chs_all.pt",

    # Set according to your CPU
    "dataloader_workers": 4,
    # Generate data online for train/val
    "online_train": False,
    "online_val": False,
}
