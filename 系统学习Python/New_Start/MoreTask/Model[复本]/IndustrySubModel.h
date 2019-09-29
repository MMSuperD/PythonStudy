//
//  IndustrySubModel.h
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/23.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "IndustrySubSubModel.h"

@interface IndustrySubModel : NSObject

@property (strong, nonatomic) NSString *status;
@property (strong, nonatomic) NSString *codeStr;
@property (strong, nonatomic) NSString *level;
@property (strong, nonatomic) NSMutableArray <IndustrySubSubModel *> *children;
@property (strong, nonatomic) NSString *value;
@property (strong, nonatomic) NSString *group;
@property (strong, nonatomic) NSString *priority;
@property (strong, nonatomic) NSString *advancedId;

@end
