//
//  PersonIndoModel.m
//  BalanceTransfer
//
//  Created by HeCode on 2018/2/26.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "PersonIndoModel.h"

@implementation PersonIndoModel
+ (NSDictionary *)modelCustomPropertyMapper {
    return @{
             @"memberId" :@"data.memberId",
             @"idCardBack" :@"data.idCardBack",
             @"mobile" :@"data.mobile",
             @"name" :@"data.name",
             @"career" :@"data.career",
             @"education" :@"data.education",
             @"birthday" :@"data.birthday",
             @"age" :@"data.age",
             @"gender" :@"data.gender",
             @"idCardFront" :@"data.idCardFront",
             @"facePhoto" :@"data.facePhoto",
             @"idCardNo" :@"data.idCardNo",
             };
}

@end
