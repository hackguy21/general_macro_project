#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
recognize.py

특정 포트로 들어오는 영상 스트림을 캡쳐하여 이미지로 반환하는 모듈입니다.
OpenCV의 VideoCapture를 이용해 영상을 받아오고, matplotlib의 imshow를 통해 캡쳐한 이미지를 화면에 출력합니다.

사용 예:
    캡쳐된 이미지는 NumPy 배열 형태로 반환됩니다.

주의:
    - 포트 번호는 기본적으로 0으로 설정되어 있으며, 필요에 따라 변경할 수 있습니다.
    - 코드 실행 전, OpenCV와 matplotlib 패키지가 설치되어 있어야 합니다.
      (예: pip install opencv-python matplotlib)
"""

import cv2
import matplotlib.pyplot as plt

def recognize(port=0):
    """
    지정한 포트에서 영상 스트림을 받아와 한 프레임을 캡쳐합니다.
    
    매개변수:
        port (int 또는 str): VideoCapture의 입력 포트.
                             숫자(예: 0, 1, ...)는 기본 카메라 장치 번호를 의미하고,
                             문자열(URL 등)는 스트림 주소를 의미할 수 있습니다.
    
    반환값:
        frame (numpy.ndarray): 캡쳐된 영상 프레임. 캡쳐에 실패한 경우 None을 반환.
    """
    # VideoCapture 객체 생성 (포트가 카메라 장치 번호 또는 URL일 수 있음)
    cap = cv2.VideoCapture(port)
    
    if not cap.isOpened():
        print(f"[ERROR] 포트({port})에 연결할 수 없습니다.")
        return None

    # 한 프레임 읽어오기
    ret, frame = cap.read()
    
    # 리소스 해제
    cap.release()

    if not ret:
        print("[ERROR] 프레임을 읽어오지 못했습니다.")
        return None

    # OpenCV는 기본적으로 BGR 형식이므로, matplotlib에서 올바른 색상으로 보이도록 변환
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    
    # matplotlib의 imshow를 이용해 이미지 출력
    if __name__ == '__main__':
        plt.figure(figsize=(8, 6))
        plt.imshow(frame_rgb)
        plt.title("Captured Image")
        plt.axis("off")
        plt.show()




    return frame

if __name__ == '__main__':
    # 기본 포트 0에서 이미지 캡쳐 예제 실행
    captured_image = recognize(0)

    
