# utils/date_utils.py
# 关于立春日期的函数

from datetime import datetime
from config.lichun_dates import LICHUN_DATES
from config.data import HEAVENLY_STEMS, EARTHLY_BRANCHES

def validate_date(date):
    """验证日期是否在支持的范围内"""
    if date.year < 1900 or date.year > 2100:
        raise ValueError("日期必须在1900年到2100年之间")
    return True

def is_after_lichun(date):
    """判断给定日期是否在当年立春之后"""
    year = date.year
    if year not in LICHUN_DATES:
        raise ValueError(f"没有{year}年的立春数据")
    
    lichun_month, lichun_day = LICHUN_DATES[year]
    lichun_date = datetime(year, lichun_month, lichun_day)
    
    return date >= lichun_date

def get_year_ganzhi(date):
    """根据日期获取年干支"""
    year = date.year
    
    # 如果在立春前，算作上一年
    if not is_after_lichun(date):
        year -= 1
        
    # 1984年是甲子年
    base_year = 1984
    year_diff = (year - base_year) % 60
    
    # 计算天干和地支的索引
    heavenly_stem_index = (year_diff % 10)
    earthly_branch_index = (year_diff % 12)
    
    return f"{HEAVENLY_STEMS[heavenly_stem_index]}{EARTHLY_BRANCHES[earthly_branch_index]}"

def get_year_branch(year, date=None):
    """获取年份对应的地支"""
    if date:
        # 如果还没到立春，算作上一年
        if not is_after_lichun(date):
            year -= 1
    
    # 1984年是子年
    base_year = 1984
    year_diff = (year - base_year) % 12
    return EARTHLY_BRANCHES[year_diff]