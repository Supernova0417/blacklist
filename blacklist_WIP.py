# -*- coding: UTF-8 -*-
import logging
import requests
import time
from datetime import datetime, date, timedelta


file_name = "blacklist.txt" # for the CUSTOM LISTS tab on https://proxycheck.io/                                                                                                             dashboard/
sleep_time = 60 * 60 * 6 # 초. 즉, 6시간.
url = "http://www.vpngate.net/api/iphone/"
file_softether = "softether.txt"
file_asn_maglinant = "asn1.txt"
file_asn_game_hacker = "asn2.txt"
blacklist = []

'''
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
↑ for under python 3.8
"force = True" is the same for more than or equal to python 3.8
'''
logging.basicConfig(
    format = '[%(levelname)s] %(asctime)s : %(message)s',
    #filemod = "w",
    filename = 'error.log_%s'%date.today().strftime('%Y_%m_%d'),
    level = logging.WARNING,
    force = True
    )

# https://nongnongai.tistory.com/28
# https://www.google.com/search?q=python2+logging&oq=python2+logging&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIPCAEQABgKGIMBGLEDGIAEMgwIAhAAGAoYsQMYgAQyDAgDEAAYChixAxiABDIMCAQQABgKGLEDGIAEMgwIBRAAGAoYsQMYgAQyCQgGEAAYChiABDIJCAcQABgKGIAEMg8ICBAAGAoYgwEYsQMYgAQyDAgJEAAYChixAxiABNIBCDMwMTJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8


# Softether VPN IP 리스트를 가져와서 정리 후 텍스트 파일로 저장하는 함수
def get_softether():
    global blacklist
    print("공개 SoftEther VPN 목록을 {}로부터 가져옵니다.".format(url))
    softether_list_new = ["#******   %s   ******"%datetime.now(),""]
    softether_list_new.append("#/////    SoftEther VPN List    /////")
    softether_list_new.append("#아이피                #적용일")
    try:
        response = requests.get(url)
        data = response.text.encode('utf-8')
        data = data.decode('utf-8')
        garo = data.strip().split("\n")
        garo = garo[2:]
        print("공개 SoftEther VPN 목록을 가져오는 데 성공했습니다.")
        for x in range(len(garo)):
            garo_component = garo[x].split(",")
            try:
                ip = garo_component[1]
                if not ip.startswith("219.100.37."):
                    #softether_list_new.append((ip + "/24").ljust(20) + "#%s"%datetime.now().date())
                    #원래는 위의 형식으로 저장해야하지만 기존 리스트와 IP를 비교해야하니까 IP만 있게 해보자
                    softether_list_new.append(ip)
            except IndexError as e:
                #print("더 이상 추가할 요소가 없으므로 다음 작업을 진행합니다.")
                pass
        del response, data, garo, garo_component, ip
        '''
        1. 기존의 리스트를 가져온다.
            ㄴ 기존 리스트 파일이 없으면 그냥 새 파일을 만든다.
            ㄴ 기존 리스트를 가져왔는데 (저장 형식이 다르거나 하는 이유로) 후에 에러가 발생하면 그냥 새 것을 덮어씌운다.
            ㄴ 위 두 경우가 아니면 2번으로 넘어간다.
        2. 기존의 것에서 날짜 기준으로 기록된지 "1년" 이상 된 IP는 지운다.
            그 IP들이 지워진 상태로 기존의 것을 기억하고 있는다.
        3. 새 리스트에서 IP만 추출해서 기존의 것에 있는지 검사한다.
            ㄴ 기존의 것에 이미 있는 IP면 새 리스트에서 해당 IP를 지운다.
            이렇게 새 리스트에서 모든 IP를 검사하고 바뀐 새 리스트를 기존 리스트와 합친다.
        4. 파일로 저장한다.
        '''
        try:
            with open(file_softether, 'r') as file:
                lines = file.readlines()
                softether_list_old = [line.strip() for line in lines]
            for x in range(len(softether_list_old)-4):
                softether_list_old_component = softether_list_old[x+4].replace(" ","").split("#")
                if 
            for x in range(len(softether_list_new)-4):
                softether_list_new[x+4] = softether_list_new[x+4].replace(" ","")
                softether_list_new_component = softether_list_old[x+4].split("#")
                ip_new_component = softether_list_new_component[0][:softether_list_new_component[0].rfind(".")]
                

                
            print("%s 파일을 가져오는 데 성공했습니다."%file_softether)
            print("다음 작업을 수행합니다.")
        except IOError as e:
            print("파일을 읽는 동안 오류가 발생했습니다: {}".format(e))
            print("공개 SoftEther VPN 목록 없이 다음 작업을 수행합니다.")
        blacklist = softether_list
        del softether_list
        print("만들어진 SoftEther VPN List의 길이: "+str(len(softether_list)-5))
        print("만들어진 SoftEther VPN List를 txt 파일로 저장합니다.")
        try:
            with open(file_softether, 'w') as file:
                for item in softether_list:
                    file.write(str(item) + "\n")
            print("공개 SoftEther VPN 목록을 성공적으로 저장하였습니다.")
        except IOError as e:
            print("파일을 저장하는 동안 오류가 발생했습니다:", e)
            print("파일을 저장하지 않고 계속 진행합니다.")
        blacklist = softether_list
        del softether_list
    except Exception as e:
        logging.WARNING("공개 SoftEther VPN 목록을 가져오는 데 실패했습니다: {}".format(e)                                                                                                             )
        logging.WARNING("저장된 목록을 불러옵니다.")
        try:
            with open(file_softether, 'r') as file:
                lines = file.readlines()
                softether_list = [line.strip() for line in lines]
            print("%s 파일을 가져오는 데 성공했습니다."%file_softether)
            print("다음 작업을 수행합니다.")
        except IOError as e:
            logging.ERROR("파일을 읽는 동안 오류가 발생했습니다: {}".format(e))
            logging.ERROR("공개 SoftEther VPN 목록 없이 다음 작업을 수행합니다.")
        blacklist = softether_list
        del softether_list


# ASN 리스트를 가져오는 함수
def get_asn():
    print("차단할 ASN 리스트 파일을 가져옵니다.")
    try:
        with open(file_asn_maglinant, 'r') as file:
            lines = file.readlines()
            ASN1 = [line.strip() for line in lines]
            print("%s 파일 추출을 완료하였습니다."%file_asn_maglinant)
    except IOError:
        logging.ERROR("%s 파일을 찾을 수 없습니다."%file_asn_maglinant)
        logging.ERROR("다음 작업을 수행합니다.")
    try:
        with open(file_asn_game_hacker, 'r') as file:
            lines = file.readlines()
            ASN2 = [line.strip() for line in lines]
            print("%s 파일 추출을 완료하였습니다."%file_asn_game_hacker)
    except IOError:
        logging.ERROR("%s 파일을 찾을 수 없습니다."%file_asn_game_hacker)
        logging.ERROR("다음 작업을 수행합니다.")
    global blacklist
    blacklist = blacklist + [""] + ASN1 + [""] + ASN2 + [""]
    del ASN1, ASN2, lines
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
            logging.ERROR(e)
            logging.ERROR("%s 파일을 저장하지 못했습니다."%file_name)
        print( "현재 완료 시각: " + str(datetime.now()) )
        print( "다음 실행 시각: " + str(datetime.now()+timedelta(seconds=sleep_time)) + "까지 대기합니다." )
        print( "" )
        time.sleep(sleep_time)

# 주기적으로 실행하기
run_periodically()