//
//  HelpCenterTypeModel.h
//  BalanceTransfer
//
//  Created by zhangmeijia on 2019/3/12.
//  Copyright © 2019 tlsw. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "HelpCenterQuestionModel.h"

NS_ASSUME_NONNULL_BEGIN

@interface HelpCenterTypeModel : NSObject

@property (nonatomic, strong) NSString *typeTitle;
@property (nonatomic, strong) NSArray<HelpCenterQuestionModel *> *questionList;

@end

NS_ASSUME_NONNULL_END
