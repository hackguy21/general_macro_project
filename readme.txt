"""
250418

python 3.9 기준으로 개발

General Macro Project - main.py

이 스크립트는 다음 단계를 순서대로 수행합니다:
1. 화면 인식 (recognize): PyAutoGUI 등을 활용해 게임 화면 캡쳐 후, 필요한 정보를 추출합니다.
2. 행동 계획 생성 (action): 인식된 정보를 바탕으로 캐릭터의 행동(키 입력 시퀀스 등)을 결정합니다.
3. 통신 (com): 생성된 행동 시퀀스를 PySerial 등을 통해 외부 하드웨어 또는 해당 기기로 전송합니다.
"""

프로그램 구조

Main 문

(1) Capture.py
캡처보드로 부터 화면을 캡쳐하고, Region of Interest를 설정합니다.
(2) Recognize.py
해당 캡쳐 이미지를 바탕으로 판단을 수행합니다.
(3) Action.py
판단으로부터 입력할 키보드 신호, 키보드 신호의 시퀀스를 설정합니다.
(4-1, 보류) Com.py
출력하드웨어(아두이노 레오나르도)로 신호를 전달합니다.
(4-2) Com_inside.py
PyAutoGui API를 이용하여 키보드 신호를 직접 입력합니다.

"""
library는 requirement 참조

opencv-python
matplotlib
pyautogui
