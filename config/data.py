# 天干
HEAVENLY_STEMS = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

# 地支
EARTHLY_BRANCHES = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# 男性主病对应表
MALE_DISEASE_MAP = {
    '子': {  # 鼠
        '甲': '小肠火', '乙': '脾土', '丙': '大肠金', '丁': '肾水', '戊': '胆木',
        '己': '心火', '庚': '胃土', '辛': '肺金', '壬': '膀胱水', '癸': '肝木'
    },
    '丑': {  # 牛
        '甲': '心火', '乙': '胃土', '丙': '肺金', '丁': '膀胱水', '戊': '肝木',
        '己': '小肠火', '庚': '脾土', '辛': '大肠金', '壬': '肾水', '癸': '胆木'
    },
    '寅': {  # 虎
        '甲': '小肠火', '乙': '脾土', '丙': '大肠金', '丁': '肾水', '戊': '胆木',
        '己': '心火', '庚': '胃土', '辛': '肺金', '壬': '膀胱水', '癸': '肝木'
    },
    '卯': {  # 兔
        '甲': '心火', '乙': '大肠金', '丙': '肺金', '丁': '胆木', '戊': '肝木',
        '己': '胃土', '庚': '脾土', '辛': '膀胱水', '壬': '肾水', '癸': '小肠火'
    },
    '辰': {  # 龙
        '甲': '胃土', '乙': '心火', '丙': '膀胱水', '丁': '肺金', '戊': '小肠火',
        '己': '肝木', '庚': '大肠金', '辛': '脾土', '壬': '胆木', '癸': '肾水'
    },
    '巳': {  # 蛇
        '甲': '肝木', '乙': '膀胱水', '丙': '脾土', '丁': '小肠火', '戊': '肾水',
        '己': '大肠金', '庚': '心火', '辛': '胆木', '壬': '肺金', '癸': '胃土'
    },
    '午': {  # 马
        '甲': '大肠金', '乙': '肝木', '丙': '胆木', '丁': '脾土', '戊': '胃土',
        '己': '肾水', '庚': '膀胱水', '辛': '心火', '壬': '小肠火', '癸': '肺金'
    },
    '未': {  # 羊
        '甲': '肾水', '乙': '胆木', '丙': '心火', '丁': '胃土', '戊': '肺金',
        '己': '膀胱水', '庚': '肝木', '辛': '小肠火', '壬': '脾土', '癸': '大肠金'
    },
    '申': {  # 猴
        '甲': '膀胱水', '乙': '肾水', '丙': '小肠火', '丁': '心火', '戊': '大肠金',
        '己': '肺金', '庚': '胆木', '辛': '肝木', '壬': '胃土', '癸': '脾土'
    },
    '酉': {  # 鸡
        '甲': '肺金', '乙': '小肠火', '丙': '肝木', '丁': '大肠金', '戊': '脾土',
        '己': '胆木', '庚': '肾水', '辛': '胃土', '壬': '心火', '癸': '膀胱水'
    },
    '戌': {  # 狗
        '甲': '胆木', '乙': '肺金', '丙': '胃土', '丁': '肝木', '戊': '膀胱水',
        '己': '脾土', '庚': '小肠火', '辛': '肾水', '壬': '大肠金', '癸': '心火'
    },
    '亥': {  # 猪
        '甲': '脾土', '乙': '胃土', '丙': '肾水', '丁': '膀胱水', '戊': '心火',
        '己': '小肠火', '庚': '肺金', '辛': '大肠金', '壬': '肝木', '癸': '胆木'
    }
}

# 女性主病对应表
FEMALE_DISEASE_MAP = {
    '子': {  # 鼠
        '甲': '胃土', '乙': '脾土', '丙': '膀胱水', '丁': '肾水', '戊': '小肠火',
        '己': '心火', '庚': '大肠金', '辛': '肺金', '壬': '胆木', '癸': '肝木'
    },
    '丑': {  # 牛
        '甲': '心火', '乙': '胃土', '丙': '肺金', '丁': '膀胱水', '戊': '肝木',
        '己': '小肠火', '庚': '脾土', '辛': '大肠金', '壬': '肾水', '癸': '胆木'
    },
    '寅': {  # 虎
        '甲': '小肠火', '乙': '脾土', '丙': '大肠金', '丁': '肾水', '戊': '胆木',
        '己': '心火', '庚': '胃土', '辛': '肺金', '壬': '膀胱水', '癸': '肝木'
    },
    '卯': {  # 兔
        '甲': '心火', '乙': '胃土', '丙': '肺金', '丁': '膀胱水', '戊': '肝木',
        '己': '小肠火', '庚': '脾土', '辛': '大肠金', '壬': '肾水', '癸': '胆木'
    },
    '辰': {  # 龙
        '甲': '小肠火', '乙': '肺金', '丙': '大肠金', '丁': '肝木', '戊': '胆木',
        '己': '脾土', '庚': '胃土', '辛': '肾水', '壬': '膀胱水', '癸': '心火'
    },
    '巳': {  # 蛇
        '甲': '脾土', '乙': '小肠火', '丙': '肾水', '丁': '大肠金', '戊': '心火',
        '己': '胆木', '庚': '肺金', '辛': '胃土', '壬': '肝木', '癸': '膀胱水'
    },
    '午': {  # 马
        '甲': '胆木', '乙': '肾水', '丙': '胃土', '丁': '心火', '戊': '膀胱水',
        '己': '肺金', '庚': '小肠火', '辛': '肝木', '壬': '大肠金', '癸': '脾土'
    },
    '未': {  # 羊
        '甲': '肺金', '乙': '胆木', '丙': '肝木', '丁': '胃土', '戊': '脾土',
        '己': '膀胱水', '庚': '肾水', '辛': '小肠火', '壬': '心火', '癸': '大肠金'
    },
    '申': {  # 猴
        '甲': '膀胱水', '乙': '肝木', '丙': '小肠火', '丁': '脾土', '戊': '大肠金',
        '己': '肾水', '庚': '胆木', '辛': '心火', '壬': '胃土', '癸': '肺金'
    },
    '酉': {  # 鸡
        '甲': '肾水', '乙': '膀胱水', '丙': '心火', '丁': '小肠火', '戊': '肺金',
        '己': '大肠金', '庚': '肝木', '辛': '胆木', '壬': '脾土', '癸': '胃土'
    },
    '戌': {  # 狗
        '甲': '大肠金', '乙': '心火', '丙': '胆木', '丁': '肺金', '戊': '胃土',
        '己': '肝木', '庚': '膀胱水', '辛': '脾土', '壬': '小肠火', '癸': '肾水'
    },
    '亥': {  # 猪
        '甲': '肝木', '乙': '大肠金', '丙': '脾土', '丁': '胆木', '戊': '肾水',
        '己': '胃土', '庚': '心火', '辛': '膀胱水', '壬': '肺金', '癸': '小肠火'
    }
}

# 行流对应表（出生年地支 + 发病日天干）
FLOW_MAP = {
    '子': {  # 鼠
        '甲': '癸水', '己': '癸水',  # 甲己同列
        '乙': '乙木', '庚': '乙木',  # 乙庚同列
        '丙': '丁火', '辛': '丁火',  # 丙辛同列
        '丁': '己土', '壬': '己土',  # 丁壬同列
        '戊': '辛金', '癸': '辛金'   # 戊癸同列
    },
    '丑': {  # 牛
        '甲': '乙木', '己': '乙木',
        '乙': '丁火', '庚': '丁火',
        '丙': '己土', '辛': '己土',
        '丁': '辛金', '壬': '辛金',
        '戊': '癸水', '癸': '癸水'
    },
    '寅': {  # 虎
        '甲': '丙火', '己': '丙火',
        '乙': '戊土', '庚': '戊土',
        '丙': '庚金', '辛': '庚金',
        '丁': '壬水', '壬': '壬水',
        '戊': '甲木', '癸': '甲木'
    },
    '卯': {  # 兔
        '甲': '丙火', '己': '丙火',
        '乙': '戊土', '庚': '戊土',
        '丙': '庚金', '辛': '庚金',
        '丁': '壬水', '壬': '壬水',
        '戊': '甲木', '癸': '甲木'
    },
    '辰': {  # 龙
        '甲': '丙火', '己': '丙火',
        '乙': '戊土', '庚': '戊土',
        '丙': '庚金', '辛': '庚金',
        '丁': '壬水', '壬': '壬水',
        '戊': '甲木', '癸': '甲木'
    },
    '巳': {  # 蛇
        '甲': '丁火', '己': '丁火',
        '乙': '己土', '庚': '己土',
        '丙': '辛金', '辛': '辛金',
        '丁': '癸水', '壬': '癸水',
        '戊': '乙木', '癸': '乙木'
    },
    '午': {  # 马
        '甲': '丁火', '己': '丁火',
        '乙': '己土', '庚': '己土',
        '丙': '辛金', '辛': '辛金',
        '丁': '癸水', '壬': '癸水',
        '戊': '乙木', '癸': '乙木'
    },
    '未': {  # 羊
        '甲': '己土', '己': '己土',
        '乙': '辛金', '庚': '辛金',
        '丙': '癸水', '辛': '癸水',
        '丁': '乙木', '壬': '乙木',
        '戊': '丁火', '癸': '丁火'
    },
    '申': {  # 猴
        '甲': '庚金', '己': '庚金',
        '乙': '壬水', '庚': '壬水',
        '丙': '甲木', '辛': '甲木',
        '丁': '丙火', '壬': '丙火',
        '戊': '戊土', '癸': '戊土'
    },
    '酉': {  # 鸡
        '甲': '庚金', '己': '庚金',
        '乙': '壬水', '庚': '壬水',
        '丙': '甲木', '辛': '甲木',
        '丁': '丙火', '壬': '丙火',
        '戊': '戊土', '癸': '戊土'
    },
    '戌': {  # 狗
        '甲': '壬水', '己': '壬水',
        '乙': '甲木', '庚': '甲木',
        '丙': '丙火', '辛': '丙火',
        '丁': '戊土', '壬': '戊土',
        '戊': '庚金', '癸': '庚金'
    },
    '亥': {  # 猪
        '甲': '癸水', '己': '癸水',
        '乙': '乙木', '庚': '乙木',
        '丙': '丁火', '辛': '丁火',
        '丁': '己土', '壬': '己土',
        '戊': '辛金', '癸': '辛金'
    }
}

# 治疗方案映射配置
TREATMENT_MAP = {
    '风邪': {
        '肝木': {'加临': '风邪袭肝', '用方': '小柴胡汤'},
        '心火': {'加临': '风邪袭心', '用方': '黄连黄芩麦冬桔梗甘草汤'},
        '脾土': {'加临': '风邪乘脾', '用方': '桂枝去桂加茯苓白术汤'},
        '肺金': {'加临': '风邪乘肺', '用方': '桔梗甘草枳实芍药汤'},
        '肾水': {'加临': '风邪乘肾', '用方': '柴胡桂枝汤'},
        '小肠火': {'加临': '风邪乘小肠', '用方': '黄连黄芩麦冬桔梗甘草汤'},
        '胃土': {'加临': '风邪乘胃', '用方': '枳实厚朴白术甘草汤'},
        '大肠金': {'加临': '风邪袭大肠', '用方': '桔梗甘草枳实芍药加地黄牡丹汤'},
        '膀胱水': {'加临': '风邪乘膀胱', '用方': '柴胡桂枝汤'},
        '胆木': {'加临': '风邪乘胆', '用方': '柴胡芍药枳实甘草汤'}
    },
    '热邪': {
        '肝木': {'加临': '热邪袭肝', '用方': '黄连黄芩半夏猪胆汁汤'},
        '心火': {'加临': '热邪袭心', '用方': '黄连黄芩泻心汤'},
        '脾土': {'加临': '热邪乘脾', '用方': '大黄厚朴甘草汤'},
        '肺金': {'加临': '热邪乘肺', '用方': '黄连石膏半夏甘草汤'},
        '肾水': {'加临': '热邪移肾', '用方': '地黄黄柏黄连半夏汤'},
        '小肠火': {'加临': '热邪袭小肠', '用方': '黄连黄芩泻心汤'},
        '胃土': {'加临': '热邪乘胃', '用方': '大黄厚朴甘草汤'},
        '大肠金': {'加临': '热邪乘大肠', '用方': '黄连石膏半夏甘草汤'},
        '膀胱水': {'加临': '热邪移膀胱', '用方': '地黄黄柏黄连半夏汤'},
        '胆木': {'加临': '热邪袭胆', '用方': '黄连黄芩半夏猪胆汁'}
    },
    '湿邪': {
        '肝木': {'加临': '湿邪犯肝', '用方': '待补充'},
        '心火': {'加临': '湿邪犯心', '用方': '待补充'},
        '脾土': {'加临': '湿邪干脾', '用方': '理中汤'},
        '肺金': {'加临': '湿邪干肺', '用方': '小青龙汤'},
        '肾水': {'加临': '湿邪移肾', '用方': '五苓散'},
        '小肠火': {'加临': '湿邪犯小肠', '用方': '待补充'},
        '胃土': {'加临': '湿邪干胃', '用方': '白术茯苓厚朴汤'},
        '大肠金': {'加临': '湿邪干大肠', '用方': '小青龙汤'},
        '膀胱水': {'加临': '湿邪移膀胱', '用方': '五苓散'},
        '胆木': {'加临': '湿邪犯胆', '用方': '待补充'}
    },
    '燥邪': {
        '肝木': {'加临': '燥邪乘肝', '用方': '黄芩牡丹皮瓜蒌半夏枳实汤'},
        '心火': {'加临': '燥邪乘心', '用方': '栀子连翘甘草栝蒌汤'},
        '脾土': {'加临': '燥邪乘脾', '用方': '白虎汤'},
        '肺金': {'加临': '燥邪乘肺', '用方': '竹叶石膏杏子甘草汤'},
        '肾水': {'加临': '燥邪干肾', '用方': '地黄黄柏茯苓栝蒌汤'},
        '小肠火': {'加临': '燥邪乘小肠', '用方': '栀子连翘甘草栝蒌汤'},
        '胃土': {'加临': '燥邪乘胃', '用方': '白虎汤'},
        '大肠金': {'加临': '燥邪乘大肠', '用方': '麻仁白蜜煎'},
        '膀胱水': {'加临': '燥邪干膀胱', '用方': '地黄黄柏茯苓栝蒌汤'},
        '胆木': {'加临': '燥邪乘胆', '用方': '黄芩牡丹皮瓜蒌半夏枳实汤'}
    },
    '寒邪': {
        '肝木': {'加临': '寒邪乘肝', '用方': '小柴胡汤'},
        '心火': {'加临': '寒邪乘心', '用方': '通脉四逆汤'},
        '脾土': {'加临': '寒邪乘脾', '用方': '理中汤'},
        '肺金': {'加临': '寒邪乘肺', '用方': '甘草干姜汤'},
        '肾水': {'加临': '寒邪干肾', '用方': '桂枝加葛根汤'},
        '小肠火': {'加临': '寒邪乘小肠', '用方': '甘草泻心汤'},
        '胃土': {'加临': '寒邪乘胃', '用方': '枳实白术茯苓甘草汤'},
        '大肠金': {'加临': '寒邪乘大肠', '用方': '枳实橘皮桔梗半夏生姜甘草汤'},
        '膀胱水': {'加临': '寒邪干膀胱', '用方': '甘草干姜茯苓白术汤'},
        '胆木': {'加临': '寒邪乘胆', '用方': '柴胡黄芩芍药半夏甘草汤'}
    },
    '暑邪': {
        '肝木': {'加临': '暑邪袭肝', '用方': '黄连黄芩半夏猪胆汁汤'},
        '心火': {'加临': '暑邪袭心', '用方': '黄连半夏石膏甘草汤'},
        '脾土': {'加临': '暑邪乘脾', '用方': '待补充'},
        '肺金': {'加临': '暑邪乘肺', '用方': '竹叶石膏汤'},
        '肾水': {'加临': '暑邪移肾', '用方': '待补充'},
        '小肠火': {'加临': '暑邪袭小肠', '用方': '黄连半夏石膏甘草汤'},
        '胃土': {'加临': '暑邪乘胃', '用方': '待补充'},
        '大肠金': {'加临': '暑邪乘大肠', '用方': '百合地黄加牡蛎汤'},
        '膀胱水': {'加临': '暑邪移大肠', '用方': '甘草干姜茯苓白术汤'},
        '胆木': {'加临': '寒邪乘胆', '用方': '柴胡黄芩芍药半夏甘草汤'}
    }
}
