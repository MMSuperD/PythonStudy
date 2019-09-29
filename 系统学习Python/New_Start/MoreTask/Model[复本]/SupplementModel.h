//
//  SupplementModel.h
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/20.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BaseModel.h"
#import "MapSupModel.h"

@interface SupplementModel : BaseModel

@property (strong, nonatomic) MapSupModel *emContactPhone;
@property (strong, nonatomic) MapSupModel *emContactName;
@property (strong, nonatomic) MapSupModel *career;
@property (strong, nonatomic) MapSupModel *income;
@property (strong, nonatomic) MapSupModel *education;

@end
