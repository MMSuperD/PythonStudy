//
//  HelpCenterModel.h
//  BalanceTransfer
//
//  Created by zhangmeijia on 2019/3/12.
//  Copyright © 2019 tlsw. All rights reserved.
//

#import "BaseModel.h"
#import "HelpCenterTypeModel.h"

NS_ASSUME_NONNULL_BEGIN

@interface HelpCenterModel : BaseModel

@property (nonatomic, strong) NSArray<HelpCenterTypeModel *> *dataList;

@end

NS_ASSUME_NONNULL_END
