//
//  BTUserDefault.h
//  BalanceTransfer
//
//  Created by HeCode on 2018/2/1.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "BTAccountModel.h"


@interface BTUserDefault : NSObject
+(instancetype)standardUserDefaluts;

@property (nonatomic, copy) NSString *tokenMemberId;
@property (nonatomic, copy) NSString *token;



// 存账号
-(void)saveAccount:(BTAccountModel *)model;

// 取账号
-(BTAccountModel *)currentAccount;

//清除账号信息
- (void)deleteAccount;

// 存储当前最新网络状态
- (void)setNetWorkState:(NSString *)netWorkState;

- (NSString *)getNetWorkState;


@end
