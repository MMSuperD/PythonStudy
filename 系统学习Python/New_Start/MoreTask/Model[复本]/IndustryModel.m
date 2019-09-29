//
//  IndustryModel.m
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/23.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "IndustryModel.h"

@implementation IndustryModel

+ (NSDictionary *)modelCustomPropertyMapper{
    return @{
//             @"advancedId" :@"data.id",
//             @"group" :@"data.group",
//             @"codeStr" :@"data.code",
//             @"value" :@"data.value",
//             @"level" :@"data.level",
//             @"children" :@"data.children",
             @"dataList" :@"data"
             };
}


+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass{
    return @{
             @"dataList":[IndustrySubModel class],
             };
}

@end
