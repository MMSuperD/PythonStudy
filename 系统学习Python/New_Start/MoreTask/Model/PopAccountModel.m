//
//  PopAccountModel.m
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/3/23.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "PopAccountModel.h"

@implementation PopAccountModel

+ (NSDictionary *)modelCustomPropertyMapper {
    return @{
            @"popCodeId" :@"data.popCodeId",
            @"promoterId" :@"data.promoterId",
            @"promoterType" :@"data.promoterType",
            @"promoterName" :@"data.promoterName",
            @"promoterSonId" :@"data.promoterSonId",
            @"popCode" :@"data.popCode",
            @"accountId" :@"data.accountId",
            @"accountType" :@"data.accountType",
            @"cardNo" :@"data.cardNo",
            @"bankCode" :@"data.bankCode",
            @"bankName" :@"data.bankName",
            @"beCountAmount" :@"data.beCountAmount",
            @"switchs" :@"data.switchs",
            @"isDelete" :@"data.isDelete",
            @"createBy" :@"data.createBy",
            @"createDate" :@"data.createDate",
            @"updateBy" :@"data.updateBy",
            @"updateDate" :@"data.updateDate"
            };
}

@end
