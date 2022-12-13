"""Metric 함수 정의
"""

import torch
import numpy as np
SMOOTH = 1e-6


def get_metric_function(metric_function_str):
    """
    Add metrics, weights for weighted score
    """

    if metric_function_str == 'miou':
        iou = Iou()
        return iou.get_miou

    elif metric_function_str == 'iou0':
        iou =Iou(class_num=0)
        return iou.get_iou
    
    elif metric_function_str == 'iou1':
        iou =Iou(class_num=1)
        return iou.get_iou 

        
class Iou:
    
    def __init__(self, class_num:int=0):
        self.class_num = class_num
        
    def get_iou(self, outputs: torch.Tensor, labels: torch.Tensor):
        mask_value = self.class_num

        batch_size = outputs.size()[0]
            
        intersection = ((outputs.int() == mask_value) & (labels.int() == mask_value) & (outputs.int() == labels.int())).float()
        intersection = intersection.view(batch_size, -1).sum(1)

        union = ((outputs.int() == mask_value) | (labels.int() == mask_value)).float()
        union = union.view(batch_size, -1).sum(1)

        iou = (intersection + SMOOTH) / (union + SMOOTH)
            
        return iou.mean()

    def get_miou(self, outputs: torch.Tensor, labels: torch.Tensor):
        self.class_num = 0
        negative_iou = self.get_iou(outputs, labels)

        self.class_num = 1
        positive_iou = self.get_iou(outputs, labels)
    
        return (negative_iou + positive_iou) / 2

