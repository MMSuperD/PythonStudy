//
//  HelpCenterModel.m
//  BalanceTransfer
//
//  Created by zhangmeijia on 2019/3/12.
//  Copyright © 2019 tlsw. All rights reserved.
//

#import "HelpCenterModel.h"

@implementation HelpCenterModel

+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass {
    return @{
             @"dataList":[HelpCenterTypeModel class],
             };
}

@end
