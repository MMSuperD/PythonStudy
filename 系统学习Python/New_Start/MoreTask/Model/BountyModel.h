//
//  BountyModel.h
//  BalanceTransfer
//
//  Created by zhangmeijia on 2018/3/13.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface BountyModel : NSObject

@property (copy) NSString *popHistoryId;       //主键ID
@property (copy) NSString *popMode;            //推广模型
@property (copy) NSString *promoterId;         //推广者ID
@property (copy) NSString *promoterType;       //推广者类型
@property (copy) NSString *promoterName;       //推广者名称
@property (copy) NSString *promoterSonId;      //推广者子ID
@property (copy) NSString *bePromoterId;       //被推广人ID
@property (copy) NSString *popCode;            //推广码
@property (copy) NSString *sourceId;           //来源ID
@property (copy) NSString *sourceType;         //来源类型
@property (copy) NSString *transAmount;        //交易金额
@property (copy) NSString *costAmount;         //成本金额
@property (copy) NSString *shareAmount;        //分润金额
@property (copy) NSString *orderNo;            //订单号
@property (copy) NSString *promoterPhone;      //推广者联系方式
@property (copy) NSString *bePromoterPhone;    //被推广者联系方式
@property (copy) NSString *rewardType;         //奖励类型
@property (copy) NSString *rewardDesc;         //奖励描述
@property (copy) NSString *cardNo;             //借记卡卡号
@property (copy) NSString *bankName;           //银行名称
@property (copy) NSString *createBy;           //创建用户
@property (copy) NSString *createDate;         //创建时间
@property (copy) NSString *updateBy;           //修改用户
@property (copy) NSString *updateDate;         //修改时间

@end
