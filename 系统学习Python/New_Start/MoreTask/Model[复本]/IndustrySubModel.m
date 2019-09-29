//
//  IndustrySubModel.m
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/23.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "IndustrySubModel.h"

@implementation IndustrySubModel

+ (NSDictionary *)modelCustomPropertyMapper{
    return @{
             @"advancedId" :@"id",
             @"codeStr" :@"code",
             };
}

+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass {
    return @{
             @"children":[IndustrySubSubModel class],
             };
}


@end
