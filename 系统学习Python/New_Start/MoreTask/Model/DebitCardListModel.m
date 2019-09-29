//
//  DebitCardListModel.m
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/3/20.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "DebitCardListModel.h"

@implementation DebitCardListModel

+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass {
    return @{
             @"data":[DebitCardModel class]
             };
}

@end
