//
//  PlatformListModel.m
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/3/25.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "PlatformListModel.h"

@implementation PlatformListModel

+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass{
    return @{
             @"data":[PlatformModel class],
             };
}

@end
