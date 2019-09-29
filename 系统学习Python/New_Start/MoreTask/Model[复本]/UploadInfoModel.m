//
//  UploadInfoModel.m
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/14.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "UploadInfoModel.h"

@implementation UploadInfoModel
+ (NSDictionary *)modelCustomPropertyMapper {
    return @{
            @"portraitImg" :@"data.portraitImg",
            };
}

@end
