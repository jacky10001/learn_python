# -*- coding: utf-8 -*-


from .pack_1.module import func1
from .pack_2.module import func2


""" 請注意，這是 import 錯誤示範，若將這行解開註解將會出錯
    將會出現類似下面的錯誤訊息
    -----
    ValueError: attempted relative import beyond top-level package
    -----
    
    top-level package 就是所執行的 package 中最高的那層
    超過這一層的 relative import 是不被 Python 所允許的
    而下面那行 ..pack_1 嘗試跳一層上去而超過 package 了 """
# from ..pack_1.module import func1