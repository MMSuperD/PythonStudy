//
//  IndustrySubSubModel.m
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/23.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "IndustrySubSubModel.h"

@implementation IndustrySubSubModel

+ (NSDictionary *)modelCustomPropertyMapper{
    return @{
             @"advancedId": @"id",
             @"codeStr": @"code"
            };
}

@end
