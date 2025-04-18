#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
com.py

Action 시퀀스를 외부 하드웨어(예: Leonardo 보드)로 전송하는 모듈입니다.
PySerial을 사용하여 시리얼 포트로 "event:key" 형태의 명령을 전송합니다.

함수:
    init_serial(port: str, baudrate: int, timeout: float) -> None
    send_action(action: Action) -> bool
    send_actions(actions: List[Action]) -> bool

테스트:
    __main__에서 keydown/keyup 이벤트와 a, s, d, f 키를 순차적으로 전송합니다.
"""

import time
from typing import List

import serial
from action import Action

# 기본 시리얼 포트 설정 — 환경에 맞게 수정하세요.
# Windows: 'COM3', Linux/macOS: '/dev/ttyACM0' 또는 '/dev/ttyUSB0' 등
SERIAL_PORT = 'COM3'
BAUDRATE    = 115200
TIMEOUT     = 1.0  # seconds

ser = None

def init_serial(port: str = SERIAL_PORT,
                baudrate: int = BAUDRATE,
                timeout: float = TIMEOUT) -> None:
    """
    전역 ser 객체를 열어둡니다. send_action 호출 전에 반드시 초기화하세요.
    """
    global ser
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"[INFO] Opened serial port {port} @ {baudrate}bps")
    except serial.SerialException as e:
        print(f"[ERROR] Cannot open serial port {port}: {e}")
        ser = None

def send_action(action: Action) -> bool:
    """
    단일 Action을 전송합니다.
    
    포맷: "<event>:<key>\n" 예) "keydown:a\n"
    """
    if ser is None:
        print("[ERROR] Serial port not initialized. Call init_serial() first.")
        return False

    cmd = f"{action.event}:{action.key}\n"
    try:
        ser.write(cmd.encode('utf-8'))
        return True
    except serial.SerialException as e:
        print(f"[ERROR] Failed to send {cmd.strip()}: {e}")
        return False

def send_actions(actions: List[Action]) -> bool:
    """
    Action 리스트를 순차적으로 전송하고, 각 Action.duration만큼 대기합니다.
    """
    ok = True
    for act in actions:
        if not send_action(act):
            ok = False
        time.sleep(act.duration)
    return ok

if __name__ == '__main__':
    # 테스트 시리얼 초기화
    init_serial()

    # 테스트: keydown/keyup 이벤트와 a, s, d, f 키 전송
    test_keys = ['a', 's', 'd', 'f']
    events   = ['keydown', 'keyup']

    for key in test_keys:
        for ev in events:
            action = Action(event=ev, key=key, duration=0.1)
            print(f"Sending {ev} {key} …", end=' ')
            success = send_action(action)
            print("OK" if success else "FAIL")
            time.sleep(0.2)
