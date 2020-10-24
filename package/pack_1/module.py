# -*- coding: utf-8 -*-


""" 請注意，這是 import 錯誤示範，若將這行解開註解將會出錯
    因為 pack_1 會和 pack_2 形成 circular import（循環匯入）
    用白話來說的話，這是一種 "我不讓你，你不讓我" 的情況
    建立套件時，務必想好整個文件架構，才不會出現這種錯誤 """
# from ..pack_2.module import func3


def func1():
    print('pack_1 func1')

def func2():
    print('pack_1 func2')