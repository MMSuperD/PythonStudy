//
//  BountyListModel.m
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/3/13.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BountyListModel.h"

@implementation BountyListModel

+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass {
    return @{
             @"data":[BountyModel class]
             };
}

+ (NSDictionary *)modelCustomPropertyMapper {
    return @{
             @"data":@"data.records",
             @"totalCount":@"data.totalCount",
             @"totalPage":@"data.totalPage"
             };
}

@end
