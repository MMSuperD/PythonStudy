//
//  BTSmsSignModel.m
//  BalanceTransfer
//
//  Created by zhangmeijia on 2019/3/5.
//  Copyright © 2019 tlsw. All rights reserved.
//

#import "BTSmsSignModel.h"

@implementation BTSmsSignModel

+ (NSDictionary *)modelCustomPropertyMapper{
    return @{
             @"smsSignNo": @"data.smsSignNo"
             };
}

@end
