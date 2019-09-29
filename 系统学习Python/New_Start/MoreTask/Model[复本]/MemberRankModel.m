//
//  MemberRankModel.m
//  BalanceTransfer
//
//  Created by zhangmeijia on 2019/4/9.
//  Copyright © 2019 tlsw. All rights reserved.
//

#import "MemberRankModel.h"

@implementation MemberRankModel

+ (NSDictionary *)modelCustomPropertyMapper{
    return @{
             @"rank": @"data.rank"
             };
}

@end
