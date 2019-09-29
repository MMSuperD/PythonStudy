//
//  PopAccountModel.h
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/3/23.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BaseModel.h"

@interface PopAccountModel : BaseModel

@property (copy) NSString *popCodeId;
@property (copy) NSString *promoterId;
@property (copy) NSString *promoterType;
@property (copy) NSString *promoterName;
@property (copy) NSString *promoterSonId;
@property (copy) NSString *popCode;
@property (copy) NSString *accountId;
@property (copy) NSString *accountType;
@property (copy) NSString *cardNo;
@property (copy) NSString *bankCode;
@property (copy) NSString *bankName;
@property (copy) NSString *beCountAmount;
@property (copy) NSString *switchs;
@property (copy) NSString *isDelete;
@property (copy) NSString *createBy;
@property (copy) NSString *createDate;
@property (copy) NSString *updateBy;
@property (copy) NSString *updateDate;

@end
