# -*- coding: utf-8 -*-
import requests
import time
from datetime import datetime, timedelta


file_name = "blacklist.txt" # for the CUSTOM LISTS tab on https://proxycheck.io/dashboard/
sleep_time = 24 * 60 * 60 # 초. 즉, 1일.
url = "http://www.vpngate.net/api/iphone/"
file_softether = "softether.txt"
file_asn_maglinant = "asn1.txt"
file_asn_game_hacker = "asn2.txt"
blacklist = []


# Softether VPN IP 리스트를 가져와서 정리 후 텍스트 파일로 저장하는 함수
def get_softether():
    print("공개 SoftEther VPN 목록을 {}로부터 가져옵니다.".format(url))
    softether_list = ["#******   %s   ******"%datetime.now()]
    softether_list.append("#/////    SoftEther VPN List    /////")
    #count = 0
    try:
        response = requests.get(url)
        data = response.text.encode('utf-8')
        garo = data.strip().split("\n")
        garo = garo[2:]
        print("공개 SoftEther VPN 목록을 가져오는 데 성공했습니다.")
        print("proxycheck.io CUSTOM LISTS에 맞게 변형합니다.")
        for x in xrange(len(garo)):
            garo_component = garo[x].split(",")
            try:
                ip = garo_component[1]
                if not ip.startswith('219.100.37.'):
                    softether_list.append(ip)
                    #print('Appended 가로_요소[%d].' % count)
            except IndexError as e:
                #print(e)
                print("더 이상 추가할 요소가 없으므로 다음 작업을 진행합니다.")
            #count += 1
        print("만들어진 SoftEther VPN List의 길이: "+str(len(softether_list)-2))
        print("만들어진 SoftEther VPN List를 txt 파일로 저장합니다.")
        try:
            with open(file_softether, 'w') as file:
                for item in softether_list:
                    file.write(str(item) + '\n')
            print("공개 SoftEther VPN 목록을 성공적으로 저장하였습니다.")
        except IOError as e:
            print("파일을 저장하는 동안 오류가 발생했습니다:", e)
            print("파일을 저장하지 않고 계속 진행합니다.")
        global blacklist
        blacklist = softether_list
    except Exception as e:
        print("공개 SoftEther VPN 목록을 가져오는 데 실패했습니다: {}".format(e))
        print("저장된 목록을 불러옵니다.")
        try:
            with open(file_softether, 'r') as file:
                lines = file.readlines()
                softether_list = [line.strip() for line in lines]
            print("%s 파일을 가져오는 데 성공했습니다."%file_softether)
            print("다음 작업을 수행합니다.")
        except IOError as e:
            print("파일을 읽는 동안 오류가 발생했습니다: {}".format(e))
            print("공개 SoftEther VPN 목록 없이 다음 작업을 수행합니다.")
        global blacklist
        blacklist = softether_list


# ASN 리스트를 가져오는 함수
def get_asn():
    print("차단할 ASN 리스트 파일을 가져옵니다.")
    try:
        with open(file_asn_maglinant, 'r') as file:
            lines = file.readlines()
            ASN1 = [line.strip() for line in lines]
            print("%s 파일 추출을 완료하였습니다."%file_asn_maglinant)
    except IOError:
        print("%s 파일을 찾을 수 없습니다."%file_asn_maglinant)
        print("다음 작업을 수행합니다.")
    try:
        with open(file_asn_game_hacker, 'r') as file:
            lines = file.readlines()
            ASN2 = [line.strip() for line in lines]
            print("%s 파일 추출을 완료하였습니다."%file_asn_game_hacker)
    except IOError:
        print("%s 파일을 찾을 수 없습니다."%file_asn_game_hacker)
        print("다음 작업을 수행합니다.")
    global blacklist
    blacklist = blacklist + [""] + ASN1 + ASN2 + [""]
    print("모든 리스트 취합 완료. 최종 리스트 파일을 업데이트 합니다.")


# 일정 시간마다 자동 실행하는 함수
def run_periodically():
    while True:
        get_softether()
        get_asn()
        try:
            with open(file_name, "w") as txtfile:
                for x in blacklist:
                    txtfile.write(x + "\n")
            print("성공적으로 %s 파일을 저장했습니다."%file_name)
        except Exception as e:
            print(e)
            print("%s 파일을 저장하지 못했습니다."%file_name)
        print( '현재 완료 시각: ' + str(datetime.now()) )
        print( '다음 실행 시각: ' + str(datetime.now()+timedelta(seconds=sleep_time)) + '까지 대기합니다.' )
        time.sleep(sleep_time)

# 주기적으로 실행하기
run_periodically()
