#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
action.py

인식 결과를 바탕으로 키 입력 액션 시퀀스를 생성하는 모듈입니다.
각 액션은 event(“keydown” 또는 “keyup”), key(“keyleft”, “keyright”, “a”, “s”, “d”, “f”, “z”, “x”, “c”, “v”, “1”…“6”), duration(초)로 정의됩니다.
"""

from dataclasses import dataclass, field
from typing import List

# 허용되는 이벤트 타입과 키 목록 수정
EVENTS = {"keydown", "keyup"}
KEYS   = {
    "left", "right", "up", "down",
    "a", "s", "d", "f",
    "z", "x", "c", "v",
    "1", "2", "3", "4", "5", "6",
}

@dataclass
class Action:
    event: str
    key: str
    duration: float = field(default=0.0)

    def __post_init__(self):
        if self.event not in EVENTS:
            raise ValueError(f"Invalid event '{self.event}'. Must be one of {EVENTS}.")
        if self.key not in KEYS:
            raise ValueError(f"Invalid key '{self.key}'. Must be one of {KEYS}.")
        if self.duration < 0:
            raise ValueError("Duration must be non‑negative.")

DEFAULT_HORIZON = 5.0  # 미리 계획할 총 시간(초)

def create_action_sequence(recognized_info, horizon=DEFAULT_HORIZON):
    """
    recognized_info 기반으로 'horizon' 초 동안 실행할 Action 리스트를 반환.
    """
    seq = []
    elapsed = 0.0

    # 간단 예시: HP 체크 → 이동/공격 주기 반복
    while elapsed < horizon:
        # (1) HP가 낮으면 회복
        if isinstance(recognized_info, dict) and recognized_info.get("hp", 1.0) < 0.3:
            seq.append(Action(event="keydown", key="1", duration=0.1))
            seq.append(Action(event="keyup",   key="1", duration=0.0))
            elapsed += 0.1
            continue

        # (2) 몬스터가 멀리 있으면 접근
        #    – 여기선 무작정 오른쪽으로만 접근 예시
        seq.append(Action(event="keydown", key="keyright", duration=0.5))
        seq.append(Action(event="keyup",   key="keyright", duration=0.0))
        elapsed += 0.5

        # (3) 공격 스킬
        seq.append(Action(event="keydown", key="z", duration=0.2))
        seq.append(Action(event="keyup",   key="z", duration=0.0))
        elapsed += 0.2

    return seq

if __name__ == "__main__":
    # 테스트 코드
    dummy_info = {}
    seq = create_action_sequence(dummy_info)
    for a in seq:
        print(f"{a.event:>7} {a.key:>8} for {a.duration:.2f}s")