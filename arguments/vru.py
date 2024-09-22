ModelParams = dict(
    loader = "dynerf"
)

ModelHiddenParams = dict(
    defor_depth = 1,
    net_width = 128,
    no_ds = False,
    no_do = False,
    no_dc = False,
    
    use_coarse_temporal_embedding = True,
    c2f_temporal_iter = 10000,
    deform_from_iter = 5000,
    total_num_frames = 250,
)

OptimizationParams = dict(
    dataloader = True,
    batch_size = 1,
    iterations = 80_000,
    maxtime = 250,

    densify_from_iter = 5000,    
    pruning_from_iter = 5000,

    densify_grad_threshold_fine_init = 0.0003,
    densify_grad_threshold_after = 0.0003,

    opacity_threshold_fine_init = 0.005,
    opacity_threshold_fine_after = 0.005,
    
    densify_until_iter = 80_000,
    position_lr_max_steps = 80_000,
    deformation_lr_max_steps = 80_000,

    lambda_dssim = 1,
    num_multiview_ssim = 5,
    use_colmap = True,
    reg_coef = 1.,

    # deformation_lr_init = 0.0016,
    # deformation_lr_final = 0.00016,
    # deformation_lr_delay_mult = 0.01, 
)