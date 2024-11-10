# config/prescriptions.py 方剂详情配置

PRESCRIPTION_DETAILS = {

    # 风邪类方剂
    '小柴胡汤': {
        'components': ['柴胡半斤 黄芩三两 人参三两 半夏半升 炙甘草三两 生姜三两（切） 大枣十二枚（擘）'],
        'usage': '右七味，以水一斗二升，煮取六升，去滓，再煎取三升，温服一升，日三服。',
        'description': '',
        'indications': '风病，头痛，多汗，恶风，腋下痛，不可转侧，脉浮弦而数，此风邪干肝也，小柴胡汤主之；若流于腑，则困苦，呕逆，腹胀，善太息，柴胡枳实芍药甘草汤主之。'
    },
    '柴胡芍药枳实甘草汤': {
        'components': ['柴胡八两 芍药三两 枳实四枚（炙） 甘草三两（炙）'],
        'usage': '右四味，以水一斗，煮取六升，去滓，再煎取三升，温服一升，日三服。',
        'description': '',
        'indications': '风病，头痛，多汗，恶风，腋下痛，不可转侧，脉浮弦而数，此风邪干肝也，小柴胡汤主之；若流于腑，则困苦，呕逆，腹胀，善太息，柴胡枳实芍药甘草汤主之。'
    },
    '黄连黄芩麦冬桔梗甘草汤': {
        'components': ['黄连一两半 黄芩三两 麦门冬二两 桔梗三两 炙甘草二两'],
        'usage': '右五味，以水六升，煮取三升，去滓，温服一升，日三服。',
        'description': '',
        'indications': '风病，胸中痛，胁支满，膺背肩胛间痛，嗌干，善噫，咽肿，喉痹，脉浮洪而数，此风邪乘心也，黄连黄芩麦冬桔梗甘草汤主之。'
    },
    '桂枝去桂加茯苓白术汤': {
        'components': ['芍药三两 甘草二两（炙） 茯苓三两 白术三两 生姜三两（切） 大枣十二枚（擘）'],
        'usage': '右六味，以水八升，煮取三升，去滓，温服一升，日三服。',
        'description': '',
        'indications': '风病，四肢懈惰，体重，不能胜衣，胁下痛引肩背，脉浮而弦涩，此风邪乘脾也，桂枝去桂加茯苓白术汤主之；若流于腑，则腹满而胀，不嗜食，枳实厚朴白术甘草汤主之。'
    },
    '枳实厚朴白术甘草汤': {
        'components': ['枳实四枚（炙） 厚朴二两（炙去皮）白术三两 甘草一两（炙）'],
        'usage': '右四味，以水六升，煮取三升，去滓，温服一升，日三服。',
        'description': '',
        'indications': '风病，四肢懈惰，体重，不能胜衣，胁下痛引肩背，脉浮而弦涩，此风邪乘脾也，桂枝去桂加茯苓白术汤主之；若流于腑，则腹满而胀，不嗜食，枳实厚朴白术甘草汤主之。'
    },
    '桔梗甘草枳实芍药汤': {
        'components': ['桔梗三两 甘草二两 枳实四枚 芍药三两'],
        'usage': '右四味，以水六升，煮取三升，去滓，温服一升，日三服。',
        'description': '',
        'indications': '风病，咳而喘息有音，甚则唾血，嗌干，肩背痛，脉浮弦而数，此风邪乘肺也，桔梗甘草枳实芍药汤主之；若流于大肠，则大便燥结，或下血，桔梗甘草枳实芍药加地黄桔梗牡丹汤主之。'
    },
     '桔梗甘草枳实芍加地黄牡丹汤': {
        'components': ['桔梗三两 甘草二两 枳实四枚 芍药三两 地黄三两 牡丹皮二两'],
        'usage': '右六味，以水六升，煮取三升，去滓，温服一升，日三服。',
        'description': '',
        'indications': '风病，咳而喘息有音，甚则唾血，嗌干，肩背痛，脉浮弦而数，此风邪乘肺也，桔梗甘草枳实芍药汤主之；若流于大肠，则大便燥结，或下血，桔梗甘草枳实芍药加地黄桔梗牡丹汤主之。'
    },
      '柴胡桂枝汤': {
        'components': ['桂枝一两半 芍药一两半 甘草一两（炙）柴胡四两 半夏二合半 人参一两半 黄芩一两半 生姜一两半 大枣六枚（擘）'],
        'usage': '右九味，以水七升，煮取三升，去滓，温服一升，日三服。',
        'description': '',
        'indications': '风病，面目浮肿，脊痛不能正立，隐曲不利，甚则骨痿，脉沉而弦，此风邪乘肾也，柴胡桂枝汤主之。'
    },

    
    

    
    # 热邪类方剂
    '黄连黄芩半夏猪胆汁汤': {
        'components': ['黄连', '黄芩', '半夏', '猪胆汁'],
        'usage': '水煎服，每日1剂，分2次服用',
        'description': '清热化痰，降逆止呕',
        'indications': '热邪犯胃，胆火上逆'
    },
    '黄连黄芩泻心汤': {
        'components': ['黄连', '黄芩', '干姜', '人参', '甘草'],
        'usage': '水煎服，每日1剂，分3次温服',
        'description': '清热降逆，温中和胃',
        'indications': '心下痞，心烦喜呕'
    },
    
    # 湿邪类方剂
    '理中汤': {
        'components': ['人参', '白术', '干姜', '甘草'],
        'usage': '水煎服，每日1剂，分2-3次温服',
        'description': '温中降逆，健脾燥湿',
        'indications': '脾阳虚衰，寒湿内盛'
    },
    '小青龙汤': {
        'components': ['麻黄', '桂枝', '白芍', '细辛', '干姜', '甘草', '五味子', '半夏'],
        'usage': '水煎服，每日1剂，分2次温服',
        'description': '发散风寒，化饮止咳',
        'indications': '寒饮咳喘，恶寒发热'
    },
    
    # 其他常用方剂
    '白虎汤': {
        'components': ['石膏', '知母', '甘草', '粳米'],
        'usage': '水煎服，每日1剂，分2-3次温服',
        'description': '清热生津，除烦止渴',
        'indications': '阳明气分热盛，壮热烦渴'
    }
    # ... 可以继续添加更多方剂 ...
}