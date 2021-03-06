# -*- coding: UTF-8 -*-

from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectMultipleField, SubmitField, \
    validators, SelectField, StringField
from DbConsole import get_lingyu_data, get_caiwu_data, \
    get_location_data, get_management_data, get_purity_data, \
    get_meet_data, get_interest_data, get_basic_data


# 推荐表
class RecommendForm(FlaskForm):
    # 是否查询历史记录
    meet = BooleanField(u"是否调取过往资助记录？", [validators.Optional()], default='n')

    # 是否查询感兴趣的基金
    interest = BooleanField(u"是否输入感兴趣的运作方？", [validators.Optional()], default='n')

    # 输入名称
    meet_name_choice = get_meet_data()
    meet_name = SelectField(u"资助者名称", [validators.Optional()],
                            choices=meet_name_choice, default=None)

    # 感兴趣的基金
    interest_name_choice = get_interest_data()
    interest_name = SelectMultipleField(u"感兴趣基金名称", [validators.Optional()],
                                        choices=interest_name_choice, default=[u"北京康盟慈善基金会",
                                                                               u"中国光彩事业基金会"])

    # 业务领域
    lingyu_choices = get_lingyu_data()
    lingyu = SelectMultipleField(u"感兴趣投资领域", [validators.Optional()],
                                 choices=lingyu_choices, default=['22', '23'])

    # 财务
    caiwu_choice = get_caiwu_data()

    # 净资产
    jingzichane_choice = caiwu_choice['jingzichan']
    jingzichan = SelectField(u"净资产", choices=jingzichane_choice)
    jingzichan_x = StringField(u"净资产详细", [validators.Optional()], default=None)

    # 收入比列
    shouru_choice = caiwu_choice['shouru']
    shouru = SelectField(u"收入比例", choices=shouru_choice)
    shouru_x = StringField(u"收入比例详细", [validators.Optional()], default=None)

    # 支出比列
    zhichu_choice = caiwu_choice['zhichu']
    zhichu = SelectField(u"支出比例", choices=zhichu_choice)
    zhichu_x = StringField(u"支出比例详细", [validators.Optional()], default=None)

    # 费用比列
    feiyong_choice = caiwu_choice['feiyong']
    feiyong = SelectField(u"费用比例", choices=feiyong_choice)
    feiyong_x = StringField(u"费用比例详细", [validators.Optional()], default=None)

    # 地理位置
    location_choice = get_location_data()
    location = SelectMultipleField(u"所在地", choices=location_choice, default=None)

    # 主管单位
    management_choice = get_management_data()
    management = SelectMultipleField(u"主管单位", choices=management_choice, default=None)

    # 透明度
    purity_choice = get_purity_data()
    purity = SelectField(u"透明度", choices=purity_choice, default=None)

    submit = SubmitField(u"提交")


# 查找表
class InfoForm(FlaskForm):
    # 基金名称
    name_choice = get_basic_data()
    name = SelectField(u"基金名称", choices=name_choice, default=None)

    submit = SubmitField(u"查找")
