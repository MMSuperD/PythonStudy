//
//  HelpCenterTypeModel.m
//  BalanceTransfer
//
//  Created by zhangmeijia on 2019/3/12.
//  Copyright © 2019 tlsw. All rights reserved.
//

#import "HelpCenterTypeModel.h"

@implementation HelpCenterTypeModel

+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass {
    return @{
             @"questionList":[HelpCenterQuestionModel class],
             };
}

@end
