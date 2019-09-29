//
//  BTLocation.m
//  BalanceTransfer
//
//  Created by HeCode on 2018/3/18.
//  Copyright © 2018年 tlsw. All rights reserved.
//

#import "BTLocation.h"
#import <CoreLocation/CoreLocation.h>
#import <UIKit/UIKit.h>
#import "AppNotification.h"
#import "NSDictionary+Null.h"
#import <AFNetworking/AFNetworking.h>
#import "NSDictionary+Null.h"

@interface BTLocation ()<CLLocationManagerDelegate>

@property (nonatomic,strong) CLLocationManager *locationManager;

@end

static BTLocation *location = nil;

@implementation BTLocation

+ (instancetype)location {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        location = [[self alloc] init];
    });
    return location;
}

- (void)initLocation
{
    self.locationManager = [[CLLocationManager alloc] init];
    self.locationManager.delegate = self;
    self.locationManager.desiredAccuracy = kCLLocationAccuracyKilometer;
    self.locationManager.distanceFilter = 10000.0f;
    [self.locationManager requestWhenInUseAuthorization];
    [self.locationManager startUpdatingLocation];
}

// 定位代理；
- (void)locationManager:(CLLocationManager *)manager didChangeAuthorizationStatus:(CLAuthorizationStatus)status
{
    NSLog(@"定位权限：%d",status);
    switch (status) {
        case kCLAuthorizationStatusNotDetermined:
            if ([self.locationManager respondsToSelector:@selector(requestWhenInUseAuthorization)])
            {
                [self.locationManager requestWhenInUseAuthorization];
            }
            break;
        case kCLAuthorizationStatusDenied:
            /*定位拒绝后统一按定位失败处理*/
            [self postAlertView];
            break;
        default:
            break;
    }
    
}
- (void)locationManager:(CLLocationManager *)manager didUpdateToLocation:(CLLocation *)newLocation fromLocation:(CLLocation *)oldLocation
{
    NSLog(@"纬度:%f", newLocation.coordinate.latitude);
    NSLog(@"经度:%f", newLocation.coordinate.longitude);
    NSString *latitude = [NSString stringWithFormat:@"%f", newLocation.coordinate.latitude];
    NSString *longitude = [NSString stringWithFormat:@"%f", newLocation.coordinate.longitude];
    if (self.getLocationBlock) {
        _getLocationBlock(latitude, longitude);
    }
    [self SwithLocation:newLocation];
    [self.locationManager stopUpdatingLocation];
    self.locationManager.delegate = nil;
}

-(void)SwithLocation:(CLLocation *)location{
    __weak typeof(self) weakSelf = self;
    NSString *latitude = [NSString stringWithFormat:@"%f",location.coordinate.latitude];
    NSString *longitude = [NSString stringWithFormat:@"%f",location.coordinate.longitude];
    AFHTTPSessionManager *manager = [self getHTTPRequestManager];
    NSString *appkey = @"GtraeDNFNWwZZjndaXFHuBmOun3x5vGL";
    NSString *URL = [NSString stringWithFormat:@"http://api.map.baidu.com/geocoder/v2/?callback=%@&location=%@,%@&output=json&pois=1&ak=%@", @"", latitude, longitude, appkey];
    [manager GET:URL parameters:nil progress:nil success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject) {
        NSData *responseData = responseObject;
        NSString *responseDataString = [[NSString alloc] initWithData:responseData encoding:NSUTF8StringEncoding];
        NSData *convertData = [responseDataString dataUsingEncoding:NSUTF8StringEncoding];
        NSError *error;
        NSDictionary *lastDic = [NSJSONSerialization JSONObjectWithData:convertData options:NSJSONReadingMutableLeaves error:&error];
        long status = [[lastDic objectForKey:@"status"] longValue];
        if (status == 0 && lastDic) {
            NSDictionary *resultDict = [lastDic objectForKey:@"result"];
            NSString *formattedAddress = [resultDict stringForKey:@"formatted_address"];
            NSDictionary *addressComponent = [resultDict objectForKey:@"addressComponent"];
            NSMutableDictionary *addressDict = [[NSMutableDictionary alloc] initWithDictionary:addressComponent];
            [addressDict setObject:formattedAddress forKey:@"formatted_address"];
            if (weakSelf.getAddressBlock) {
                _getAddressBlock(latitude, longitude, addressDict);
            }
        } else {
            NSMutableDictionary *addressDict = [[NSMutableDictionary alloc] initWithDictionary:@{
                                                                                                 @"formatted_address": @"",
                                                                                                 @"province": @"",
                                                                                                 @"city": @"",
                                                                                                 @"district": @""}];
            if (weakSelf.getAddressBlock) {
                _getAddressBlock(latitude, longitude, addressDict);
            }
        }
    } failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error) {
        NSLog(@"error==%@",error);
        NSMutableDictionary *addressDict = [[NSMutableDictionary alloc] initWithDictionary:@{
                                                                                             @"formatted_address": @"",
                                                                                             @"province": @"",
                                                                                             @"city": @"",
                                                                                             @"district": @""}];
        if (weakSelf.getAddressBlock) {
            _getAddressBlock(latitude, longitude, addressDict);
        }
    }];
}

// 定位失误时触发
- (void)locationManager:(CLLocationManager *)manager didFailWithError:(NSError *)error
{
    NSLog(@"错误error:%@",error);
}

-(void)postAlertView{
    BOOL AuditMode = [[[NSUserDefaults standardUserDefaults] objectForKey:BTAuditMode] boolValue];
    NSString *sureStr = AuditMode ? @"取消": @"好";
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"提示" message:@"请到设置->隐私->位置->95193->授权95193的访问权限，以获取地理位置。" delegate:self cancelButtonTitle:sureStr otherButtonTitles:nil];
    [alert show];
}

- (void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex {
    BOOL auditMode = [[[NSUserDefaults standardUserDefaults] objectForKey:BTAuditMode] boolValue];
    if (auditMode == NO) {
        NSURL *url = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
        if ( [[UIApplication sharedApplication] canOpenURL:url] ) {
            NSURL*url = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
            [[UIApplication sharedApplication] openURL:url];
        }
    }
}

-(AFHTTPSessionManager *)getHTTPRequestManager
{
    AFHTTPSessionManager *tool = [AFHTTPSessionManager manager];
    tool.requestSerializer.timeoutInterval = 60.0;
    tool.requestSerializer = [AFJSONRequestSerializer serializer];
    tool.responseSerializer = [AFHTTPResponseSerializer serializer];

    [tool.requestSerializer setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];
   // tool.requestSerializer = [AFJSONRequestSerializer serializer];
    tool.responseSerializer.acceptableContentTypes = [NSSet setWithObjects:@"application/json", @"text/html", @"text/plain", @"text/javascript",nil];
//    AFJSONResponseSerializer *responseSerializer = [AFJSONResponseSerializer serializerWithReadingOptions:NSJSONReadingAllowFragments];


    
    // [tool setSecurityPolicy:[self customSecurityPolicy]];
    
    // 2.设置证书模式
    //    NSString * cerPath = [[NSBundle mainBundle] pathForResource:@"www.wx.starcredit.cn" ofType:@"cer"];
    //    NSData * cerData = [NSData dataWithContentsOfFile:cerPath];
    //
    //    tool.securityPolicy = [AFSecurityPolicy policyWithPinningMode:AFSSLPinningModeCertificate withPinnedCertificates:[[NSSet alloc] initWithObjects:cerData, nil]];
    //    // 客户端是否信任非法证书
    //    tool.securityPolicy.allowInvalidCertificates = YES;
    //    // 是否在证书域字段中验证域名
    //    [tool.securityPolicy setValidatesDomainName:NO];
    
    return tool ;
}

@end
