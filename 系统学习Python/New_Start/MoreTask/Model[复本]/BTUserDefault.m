//
//  BTUserDefault.m
//  BalanceTransfer
//
//  Created by HeCode on 2018/2/1.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BTUserDefault.h"
#import "BTAccountModel.h"
#define ACCOUNT @"account"

@implementation BTUserDefault

+(instancetype)standardUserDefaluts{
    static BTUserDefault *instance;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        instance = [[BTUserDefault alloc]init];
    });
    return instance;
}

// 存账号
-(void)saveAccount:(BTAccountModel *)model{
    
    NSDictionary *dic =[model yy_modelToJSONObject];
    NSUserDefaults *userDefault = [NSUserDefaults standardUserDefaults];
    [userDefault setObject:dic forKey:ACCOUNT];
    [userDefault synchronize];
}

// 取账号
-(BTAccountModel *)currentAccount{
    NSUserDefaults *userDef = [NSUserDefaults standardUserDefaults];
    NSDictionary *dic = [userDef objectForKey:ACCOUNT];
    BTAccountModel *account = [BTAccountModel yy_modelWithJSON:dic];
    return account;
}

//删除账号
- (void)deleteAccount{
    
    NSUserDefaults *userDef = [NSUserDefaults standardUserDefaults];
    [userDef removeObjectForKey:ACCOUNT];
    NSDictionary *dict = @{};
    [userDef setObject:dict forKey:ACCOUNT];
    [userDef synchronize];
    
    [self currentAccount].personInfoModel = nil;
//    [JUserDefault standardUserDefaults].mineBankCardBindCacheModel = nil;
}

- (void)setValue:(id)value forKey:(NSString *)key
{
    NSUserDefaults *userDef = [NSUserDefaults standardUserDefaults];
    [userDef setObject:value forKey:key];
    [userDef synchronize];
}

- (id)valueForKey:(NSString *)key
{
    NSUserDefaults *userDef = [NSUserDefaults standardUserDefaults];
    return  [userDef objectForKey:key];
}

// 存储当前最新网络状态
- (void)setNetWorkState:(NSString *)netWorkState{
    [[NSUserDefaults standardUserDefaults] setObject:netWorkState forKey:@"netWorkState"];
    [[NSUserDefaults standardUserDefaults] synchronize];
}

- (NSString *)getNetWorkState{
    NSString *netWorkState = [[NSUserDefaults standardUserDefaults] objectForKey:@"netWorkState"];
    return netWorkState;
}


@end
