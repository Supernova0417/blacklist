# -*- coding: utf-8 -*-
import requests
import time
from datetime import datetime, timedelta

file_name = "blacklist.txt" # for the CUSTOM LISTS tab on https://proxycheck.io/dashboard/
sleep_time = 24 * 60 * 60 # 초. 즉, 1일.

# IP와 ASN을 가져와서 리스트로 묶고 텍스트 파일로 저장하는 함수
def save_ips_to_txt():
    url = "http://www.vpngate.net/api/iphone/"
    response = requests.get(url)
    data = response.text.encode('utf-8')
    del response
    garo = data.strip().split("\n")
    del data
    garo = garo[2:]

    asn_list = [
        "",
        "#/////    Manually Blocked ISP List    /////",
        "AS5391  #Hrvatski Telekom d.d. [Croatia]",
        "AS8048  #CANTV Servicios, Venezuela [Venezuela]",
        "AS29357 #NATIONAL MOBILE TELECOMMUNICATIONS COMPANY K.S.C. (Ooredoo Kuwait) [Kuwait]",
        "AS7623  #Gyeongbuk Cable TV (주식회사 HCN 경북방송) [South Korea]",
        "",
        "AS9457  #DREAMLINE CO. (드림라인(주)) [South Korea]",
        "AS4664  #Shinbiro Onse Telecommunication Co.,Ltd. (온세텔레콤) [South Korea]",
        "AS9963  #BITNET ((주)비트넷 - (구) 네트로피 (Netropy)) [South Korea]",
        "AS46011 #LX (엘엑스(IP주소 인터넷 서비스 업체)) [South Korea]",
        "AS38661 #abcle (에이비클 - (구) 퍼플스톤즈 (HCLC)) [South Korea]",
        "AS9844  #Duruan (두루안) [South Korea]",
        "AS10068 #ILINKKOREA (아이링크코리아(주) (INDICLUB)) [South Korea]",
        "AS18301 #ILINKKOREA (아이링크코리아(주) (INDICLUB)) [South Korea]",
        "AS10048 #ILINKKOREA (아이링크코리아(주) (INDICLUB)) [South Korea]",
        "AS38662 #JND Communication (주식회사 제이엔디통신 (JNDINFO)) [South Korea]",
        "AS38086 #IP4NETASKR IP4 Networks Inc. (아이이포넷 (IP4NET)) [South Korea]",
        "AS10195 #HAIonNet (하이온넷(주)) [South Korea]",
        ""
    ]
    # 참고: https://wiki.kldp.org/wiki.php/PrivateVPN-Range
    ip_list = ["#******   %s   ******"%datetime.now()]
    ip_list.append("#/////    SoftEther VPN List    /////")
    count = 0

    for x in xrange(len(garo)):
        garo_component = garo[x].split(",")
        try:
            ip = garo_component[1]
            if not ip.startswith('219.100.37.'):
                ip_list.append(ip)
                print('Appended 가로_요소[%d].' % count)
        except IndexError as e:
            print(e)
            print('Keep progressing...')
        count += 1
    print('Length of the created IP list: '+str(len(ip_list)))
    del x, count, garo_component

    ip_list = ip_list + asn_list
    print('Finished appending ISP list to IP list.')

    with open(file_name, "w") as txtfile:
        for ip in ip_list:
            txtfile.write(ip + "\n")
    print("Saved %s successfully."%file_name)
    del ip_list, asn_list


# 일정 시간마다 자동 실행하는 함수
def run_periodically():
    while True:
        save_ips_to_txt()
        print( '현재 완료 시각: ' + str(datetime.now()) )
        print( '다음 실행 시각: ' + str(datetime.now()+timedelta(seconds=sleep_time)) )
        time.sleep(sleep_time)

# 주기적으로 실행하기
run_periodically()
