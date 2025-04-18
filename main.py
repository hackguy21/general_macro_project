#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General Macro Project - main.py

이 스크립트는 다음 단계를 순서대로 수행합니다:
1. 화면 인식 (recognize): PyAutoGUI 등을 활용해 게임 화면 캡쳐 후, 필요한 정보를 추출합니다.
2. 행동 계획 생성 (action): 인식된 정보를 바탕으로 캐릭터의 행동(키 입력 시퀀스 등)을 결정합니다.
3. 통신 (com): 생성된 행동 시퀀스를 PySerial 등을 통해 외부 하드웨어 또는 해당 기기로 전송합니다.
"""

import time
import recognize
import action
import com, com_inside

def main():
    print("==== General Macro Project 시작 ====")
    

    while True:

        ####################################

        # 1. 인식 단계: 화면 캡쳐 및 데이터 추출
        print("1단계: 화면 인식 진행 중...")
        # recognize.recognize() 함수는 캡쳐 및 이미지 분석을 수행하여 필요한 정보를 리턴합니다.
        recognized_info = recognize.recognize()  
        # print(f"인식 결과: {recognized_info}")
        
        # (옵션) 간단한 딜레이를 둘 수 있습니다.
        time.sleep(0.5)
        
        ###################################


        # 2. 행동 계획 생성: 인식된 정보를 바탕으로 실행할 액션 시퀀스를 생성합니다.
        print("2단계: 행동 시퀀스 생성 중...")
        # action.create_action_sequence() 함수는 인식 정보를 기반으로 키 입력 등 실행할 행동을 리턴합니다.
        action_sequence = action.create_action_sequence(recognized_info)
        print(f"생성된 행동 시퀀스: {action_sequence}")
        
        time.sleep(0.5)
        
        # 3. 통신 단계: 생성된 행동 시퀀스를 하드웨어로 전송합니다.
        print("3단계: 하드웨어로 행동 시퀀스 전송 중...")

        target_output = "com_inside" 

        # 하드웨어로 출력하는 경우
        if target_output == "com":

            # com.send_actions(action: Action)# 함수는 전송에 성공할 경우 True를 반환합니다.
            if com.send_actions(action_sequence):
                print("하드웨어 전송 성공.")
            else:
                print("하드웨어 전송 실패.")
        # PyAutoGUI를 이용한 내부키입력으로 출력하는 경우
        elif target_output == "com_inside":
            if com_inside.send_actions(action_sequence):
                print("하드웨어 전송 성공.")
            else:
                print("하드웨어 전송 실패.")




        ######################################


    print("==== 프로그램 종료 ====")

if __name__ == '__main__':
    main()