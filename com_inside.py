#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
com_inside.py

로컬에서 PyAutoGUI를 사용해 Action(event, key, duration)을 실행합니다.
- event: 'keydown' 또는 'keyup'
- key:  'left', 'right', 'up', 'down', 'a'...'f', 'z'...'v', '1'...'6'
"""

import time
import pyautogui
from action import Action

def init_serial(*args, **kwargs):
    # 하드웨어 대신 내부 키 제어모드
    print("[INFO] 내부 키보드 모드 활성화")

def send_action(action: Action) -> bool:
    """
    단일 Action 실행:
      - keydown  → pyautogui.keyDown(key)
      - keyup    → pyautogui.keyUp(key)
    """
    try:
        if action.event == "keydown":
            pyautogui.keyDown(action.key)
            if __name__ == "__main__":
                print(f"{action.key} key Downed")
        elif action.event == "keyup":
            pyautogui.keyUp(action.key)
            if __name__ == "__main__":
                print(f"{action.key} keyUped")
        else:
            raise ValueError(f"Unknown event: {action.event}")
        # 동작 후 duration 만큼 대기
        time.sleep(action.duration)
        return True

    except Exception as e:
        print(f"[ERROR] send_action 실패 ({action}): {e}")
        return False

def send_actions(actions):
    """
    Action 리스트를 순차 실행
    """
    ok = True
    for act in actions:
        if not send_action(act):
            ok = False
    return ok

if __name__ == "__main__":
    init_serial()
    # 테스트: 왼쪽/오른쪽 화살표와 a,s,d,f 키

    time.sleep(0.5)
    print("test를 시작합니다.")
    time.sleep(5)

    tests = [
        Action("keydown", "left", 1),
        Action("keyup",   "left", 1),
        Action("keydown", "1",1),
        Action("keyup",   "1",1),
        Action("keydown", "2",    1),
        Action("keyup",   "2",    1),
        # … 추가 테스트 …
    ]
    send_actions(tests)
    print("테스트 완료")
