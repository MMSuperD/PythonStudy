//
//  SupplementModel.m
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/20.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "SupplementModel.h"

@implementation SupplementModel

+ (NSDictionary *)modelCustomPropertyMapper{
    return @{
             @"emContactPhone": @"data.emContactPhone",
             @"emContactName": @"data.emContactName",
             @"career": @"data.career",
             @"income": @"data.income",
             @"education": @"data.education"
            };
}

+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass {
    return @{
             @"emContactPhone": [MapSupModel class],
             @"emContactName": [MapSupModel class],
             @"career": [MapSupModel class],
             @"income": [MapSupModel class],
             @"education": [MapSupModel class],
             };
}


@end
