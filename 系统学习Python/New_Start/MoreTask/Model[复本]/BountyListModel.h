//
//  BountyListModel.h
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/3/13.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BaseModel.h"
#import "BountyModel.h"

@interface BountyListModel : BaseModel

@property (copy) NSString *totalCount;
@property (copy) NSString *totalPage;
@property (nonatomic, strong) NSMutableArray<BountyModel *> *data;

@end
