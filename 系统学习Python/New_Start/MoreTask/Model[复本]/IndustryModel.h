//
//  IndustryModel.h
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/23.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BaseModel.h"
#import "IndustrySubModel.h"

@interface IndustryModel : BaseModel

//@property (strong, nonatomic) NSString *group;
//@property (strong, nonatomic) NSString *codeStr;
//@property (strong, nonatomic) NSString *value;
//@property (strong, nonatomic) NSString *level;
//@property (strong, nonatomic) NSString *status;
//@property (strong, nonatomic) NSString *advancedId;
@property (strong, nonatomic) NSMutableArray <IndustrySubModel *> *dataList;

@end
