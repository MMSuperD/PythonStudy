//
//  BTSignModel.m
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/11/6.
//  Copyright © 2018 tlsw. All rights reserved.
//

#import "BTSignModel.h"

@implementation BTSignModel

+ (NSDictionary *)modelCustomPropertyMapper{
    return @{
             @"sdkUrl": @"data.sdkUrl"
             };
}

@end
