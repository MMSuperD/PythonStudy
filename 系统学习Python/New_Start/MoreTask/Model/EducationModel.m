//
//  EducationModel.m
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/23.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "EducationModel.h"

@implementation EducationModel

+ (NSDictionary *)modelCustomPropertyMapper {
    return @{
             @"dataList": @"data",
             };
}

+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass {
    return @{
             @"dataList": [EducationSubModel class],
             };
}


@end
