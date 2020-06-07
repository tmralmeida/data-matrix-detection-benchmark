training_params = {
    "priors_info":{
        # "anchors" :[[[1.5972652, 2.063394], [2.7095582,3.3936112], [4.9832897, 6.391053]],
        #              [[0.66488904, 1.1158209], [1.0766983, 1.4735554], [1.15916838, 0.6244885]],
        #              [[0.179995492, 0.329541], [0.44646746, 0.7362717], [0.47200382, 0.37327695]]],
        # "anchors" :[[[ 2.7044, 3.4518788 ], [ 4.5835457, 5.7487273 ], [ 8.392909, 10.763879]],
        #              [[ 1.0589744, 1.822906], [ 1.7771316, 2.4889474 ], [ 2.0398571, 1.1201905 ]],
        #              [[ 0.3197612, 0.5627065 ], [ 0.7099294, 1.0341647 ], [ 1.0184706, 0.49756864]]],
        "anchors": [[[116, 90], [156, 198], [373, 326]],
                        [[30, 61], [62, 45], [59, 119]],
                        [[10, 13], [16, 30], [33, 23]]],
        "classes": 2, 
    },
    "hyper_params": {
        "backbone_lr": 0.001,
        "base_lr": 0.01,
        "freeze_backbone": False,
        "decay_gamma": 0.1,
        "decay_step": 20,
    },
    "input_shape": {
        "height": 512,
        "width": 512,
    },
    "export_onnx": False,
    
}