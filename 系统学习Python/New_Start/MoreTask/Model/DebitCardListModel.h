//
//  DebitCardListModel.h
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/3/20.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BaseModel.h"
#import "DebitCardModel.h"

@interface DebitCardListModel : BaseModel

@property (nonatomic, strong) NSMutableArray<DebitCardModel *> *data;

@end
