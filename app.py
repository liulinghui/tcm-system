# app.py
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from config.data import (
    HEAVENLY_STEMS, 
    EARTHLY_BRANCHES,
    MALE_DISEASE_MAP, 
    FEMALE_DISEASE_MAP, 
    FLOW_MAP,
    TREATMENT_MAP
)
from config.prescriptions import PRESCRIPTION_DETAILS

app = Flask(__name__)

def calculate_base_ganzhi(year):
    """计算某年1月1日的日干支基数"""
    year_last_two = year % 100
    
    if 900 <= year <= 1999:
        base = (year_last_two + 3) * 5 + 55 + (year_last_two - 1) // 4
    elif 2000 <= year <= 2099:
        base = (year_last_two + 7) * 5 + 15 + (year_last_two + 19) // 4
    else:
        raise ValueError("年份必须在900-2099之间")
    
    return base % 60

def get_days_in_month(year, month):
    """获取某月的天数"""
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        return 28
    else:
        return 31

def calculate_days_from_new_year(year, month, day):
    """计算从当年1月1日到指定日期的天数"""
    days = 0
    for m in range(1, month):
        days += get_days_in_month(year, m)
    days += day
    return days

def get_stem_branch(date):
    """获取某一天的天干"""
    year = date.year
    month = date.month
    day = date.day
    
    base = calculate_base_ganzhi(year)
    days = calculate_days_from_new_year(year, month, day)
    final_number = (base + days - 1) % 60
    stem_index = (final_number % 10)
    
    return HEAVENLY_STEMS[stem_index]

def get_year_branch(year):
    """获取年份对应的地支"""
    base_year = 1984  # 1984年是子年
    year_diff = (year - base_year) % 12
    if year_diff < 0:
        year_diff += 12
    return EARTHLY_BRANCHES[year_diff]

def get_treatment_info(evil_qi, disease):
    """获取治疗方案信息"""
    treatments = []
    
    # 如果evil_qi是列表或元组（多个邪气类型）
    if isinstance(evil_qi, (list, tuple)):
        for qi in evil_qi:
            if qi in TREATMENT_MAP and disease in TREATMENT_MAP[qi]:
                treatments.append(TREATMENT_MAP[qi][disease])
            else:
                treatments.append({'加临': '未知', '用方': '未知'})
    # 如果是单个邪气类型
    else:
        if evil_qi in TREATMENT_MAP and disease in TREATMENT_MAP[evil_qi]:
            treatments.append(TREATMENT_MAP[evil_qi][disease])
        else:
            treatments.append({'加临': '未知', '用方': '未知'})
    
    return treatments

def get_prescription_details(treatments):
    """获取方剂详细信息列表"""
    prescription_details_list = []
    for treatment in treatments:
        prescription_name = treatment['用方']
        details = PRESCRIPTION_DETAILS.get(prescription_name, {
            'components': ['未知'],
            'usage': '未知',
            'description': '未知',
            'indications': '未知'
        })
        prescription_details_list.append(details)
    return prescription_details_list

def get_info(birth_year, illness_date, gender):
    """获取主病和行流信息"""
    try:
        birth_branch = get_year_branch(birth_year)
        illness_stem = get_stem_branch(illness_date)
        
        # 根据性别选择对应的主病表
        disease_map = MALE_DISEASE_MAP if gender == 'male' else FEMALE_DISEASE_MAP
        
        # 获取主病和行流信息
        disease = disease_map.get(birth_branch, {}).get(illness_stem, "未知")
        flow = FLOW_MAP.get(birth_branch, {}).get(illness_stem, "未知")
        
        # 确定邪气类型
        evil_qi = None
        if '木' in flow:
            evil_qi = '风邪'
        elif '火' in flow:
            evil_qi = ['热邪', '暑邪', '温邪']
        elif '土' in flow:
            evil_qi = '湿邪'
        elif '金' in flow:
            evil_qi = '燥邪'
        elif '水' in flow:
            evil_qi = '寒邪'

        # 获取治疗方案
        treatments = get_treatment_info(evil_qi, disease)
        
        # 获取方剂详情列表
        prescription_details_list = get_prescription_details(treatments)

        # 添加调试信息
        print(f"===== 诊断信息 =====")
        print(f"性别：{'男' if gender == 'male' else '女'}")
        print(f"出生年：{birth_year}年")
        print(f"出生年地支：{birth_branch}")
        print(f"发病日期：{illness_date.strftime('%Y年%m月%d日')}")
        print(f"发病日天干：{illness_stem}")
        print(f"主病：{disease}")
        print(f"行流：{flow}")
        print(f"邪气：{evil_qi}")
        print(f"治疗方案：{treatments}")
        print(f"==================")
        
        return {
            'birth_branch': birth_branch,
            'illness_stem': illness_stem,
            'disease': disease,
            'flow': flow,
            'evil_qi': evil_qi if not isinstance(evil_qi, list) else '、'.join(evil_qi),
            'treatments': treatments,
            'prescription_details_list': prescription_details_list
        }
    except Exception as e:
        print(f"获取信息时出错: {str(e)}")
        return {
            'birth_branch': "未知",
            'illness_stem': "未知",
            'disease': "未知",
            'flow': "未知",
            'evil_qi': "未知",
            'treatments': [{'加临': '未知', '用方': '未知'}],
            'prescription_details_list': [{
                'components': ['未知'],
                'usage': '未知',
                'description': '未知',
                'indications': '未知'
            }],
            'error': f"处理请求时出错: {str(e)}"
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        print("收到的数据:", data)
        
        birth_date = datetime.strptime(data['birthDate'], '%Y-%m-%d')
        illness_date = datetime.strptime(data['illnessDate'], '%Y-%m-%d')
        gender = data['gender']
        
        info = get_info(birth_date.year, illness_date, gender)
        
        result = {
            'birth_year': birth_date.year,
            'birth_branch': info['birth_branch'],
            'illness_date': data['illnessDate'],
            'illness_stem': info['illness_stem'],
            'disease': info['disease'],
            'flow': info['flow'],
            'evil_qi': info['evil_qi'],
            'treatments': info['treatments'],
            'prescription_details_list': info['prescription_details_list'],
            'gender': gender
        }
        
        print("返回结果:", result)
        return jsonify(result)
    except Exception as e:
        print("错误：", str(e))
        return jsonify({'error': f'处理请求时出错: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)