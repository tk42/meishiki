#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from datetime import datetime
from meishiki.consts import Sex
from meishiki.meishiki import build_meishiki, calculate_naion


class TestNaion:
    """納音機能のテストクラス"""

    def test_calculate_naion_basic(self):
        """基本的な納音計算のテスト"""
        # 甲子 (0, 0) -> 海中金 (0)
        assert calculate_naion(0, 0) == 0
        
        # 乙丑 (1, 1) -> 海中金 (0) 
        assert calculate_naion(1, 1) == 0
        
        # 丙寅 (2, 2) -> 爐中火 (1)
        assert calculate_naion(2, 2) == 1
        
        # 丁卯 (3, 3) -> 爐中火 (1)
        assert calculate_naion(3, 3) == 1

    def test_calculate_naion_edge_cases(self):
        """納音計算の境界値テスト"""
        # 壬戌 (8, 10) -> 大海水 (29)
        assert calculate_naion(8, 10) == 29
        
        # 癸亥 (9, 11) -> 大海水 (29)
        assert calculate_naion(9, 11) == 29

    def test_meishiki_naion_integration(self):
        """Meishikiオブジェクトでの納音統合テスト"""
        # テスト用の誕生日 (1990年12月17日 0時0分)
        birthday = datetime(1990, 12, 17, 0, 0)
        sex = Sex.MALE
        
        meishiki = build_meishiki(birthday, sex)
        
        # 納音が単一の値であることを確認
        assert isinstance(meishiki.naion, int)
        
        # 納音が有効な範囲内（0-29）であることを確認
        assert 0 <= meishiki.naion <= 29

    def test_naion_consistency(self):
        """納音計算の一貫性テスト"""
        # 複数の異なる誕生日で納音が正しく計算されることを確認
        test_dates = [
            datetime(1989, 10, 28, 12, 0),
            datetime(1998, 5, 21, 0, 0), 
            datetime(2000, 1, 1, 12, 0),
        ]
        
        for birthday in test_dates:
            meishiki = build_meishiki(birthday, Sex.FEMALE)
            
            # 手動計算と自動計算の結果が一致することを確認（日柱のみ）
            expected_naion = calculate_naion(meishiki.tenkan[2], meishiki.chishi[2])  # 日柱は index 2
            assert meishiki.naion == expected_naion

    def test_naion_constants_availability(self):
        """納音定数の利用可能性テスト"""
        from meishiki.consts import kd
        
        # 納音定数が30個存在することを確認
        assert len(kd.naion) == 30
        
        # 各納音名が文字列であることを確認
        for naion_name in kd.naion:
            assert isinstance(naion_name, str)
            assert len(naion_name) > 0
        
        # 特定の納音名が正しく含まれていることを確認
        assert "海中金" in kd.naion
        assert "爐中火" in kd.naion
        assert "大海水" in kd.naion