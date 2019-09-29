//
//  PersonIndoModel.h
//  BalanceTransfer
//
//  Created by HeCode on 2018/2/26.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BaseModel.h"

@interface PersonIndoModel : BaseModel

@property (nonatomic, assign) long memerId;
@property (nonatomic, copy) NSString *status;
@property (nonatomic, copy) NSString *name;
@property (nonatomic, copy) NSString *idCardNo;
@property (nonatomic, copy) NSString *facePhoto;
@property (nonatomic, copy) NSString *idCardFront;
@property (nonatomic, copy) NSString *gender;
@property (nonatomic, copy) NSString *age;
@property (nonatomic, copy) NSString *birthday;
@property (nonatomic, copy) NSString *mobile;
@property (nonatomic, copy) NSString *education;
@property (nonatomic, copy) NSString *career;
@property (nonatomic, copy) NSString *idCardBack;
@property (nonatomic, copy) NSString *memberId;





@end
