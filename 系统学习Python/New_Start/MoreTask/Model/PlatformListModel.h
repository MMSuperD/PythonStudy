//
//  PlatformListModel.h
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/3/25.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BaseModel.h"
#import "PlatformModel.h"

@interface PlatformListModel : BaseModel

@property (nonatomic, strong) NSMutableArray<PlatformModel *> *data;

@end
