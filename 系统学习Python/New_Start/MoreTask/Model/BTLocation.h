//
//  BTLocation.h
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/18.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface BTLocation : NSObject

@property (copy,nonatomic) void (^getAddressBlock)(NSString *latitude, NSString *longitude, NSMutableDictionary *addressDic); // 需要获取地址信息

@property (copy,nonatomic) void (^getLocationBlock)(NSString *latitude, NSString *longitude); // 需要获取经纬度信息

+(instancetype)location;

-(void)initLocation;

@end
