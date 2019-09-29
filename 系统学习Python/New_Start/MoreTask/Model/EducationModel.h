//
//  EducationModel.h
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/23.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BaseModel.h"
#import "EducationSubModel.h"

@interface EducationModel : BaseModel

@property (strong, nonatomic) NSMutableArray <EducationSubModel *> *dataList;

@end
