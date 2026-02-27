# 在这里，您可以通过 'args'  获取节点中的输入变量，并通过 'ret' 输出结果
# 'args' 已经被正确地注入到环境中
# 下面是一个示例，首先获取节点的全部输入参数params，其次获取其中参数名为'input'的值：
# params = args.params;
# input = params['input'];
# 下面是一个示例，输出一个包含多种数据类型的 'ret' 对象：
# ret: Output =  { "name": '小明', "hobbies": ["看书", "旅游"] };

import requests


def get_time_from_input(input_int: int):
    # 2026021104
    # 判断input_str是否为int
    if not isinstance(input_int, int):
        return None
    input_str = str(input_int)
    if len(input_str) != 10:
        return None
    year = input_str[0:4]
    month = input_str[4:6]
    day = input_str[6:8]
    hour = input_str[8:10]
    hour = get_chinese_time_from_time(int(hour))
    return year, month, day, hour


def get_chinese_time_from_time(hour: int):
    if hour >= 23 or hour < 1:
        return "子"
    elif hour >= 1 and hour < 3:
        return "丑"
    elif hour >= 3 and hour < 5:
        return "寅"
    elif hour >= 5 and hour < 7:
        return "卯"
    elif hour >= 7 and hour < 9:
        return "辰"
    elif hour >= 9 and hour < 11:
        return "巳"
    elif hour >= 11 and hour < 13:
        return "午"
    elif hour >= 13 and hour < 15:
        return "未"
    elif hour >= 15 and hour < 17:
        return "申"
    elif hour >= 17 and hour < 19:
        return "酉"
    elif hour >= 19 and hour < 21:
        return "戌"
    elif hour >= 21 and hour < 23:
        return "亥"
    else:
        return "子"


def start(input_time, sex):
    """
    sex: M/F male/female
    """
    year, month, day, hour = get_time_from_input(input_time)
    cookies = {
        "locale": "zh-cn",
        "Hm_lvt_2b63d86124773aa67d7ceadaa32c6808": "1770644983",
        "HMACCOUNT": "9496C41E015F31A8",
        "DORA_SESS": "GPuelMOirw1zCtDc9N0S50BTfolQkM5j45fcN1onNZXr-YveuMtDc5oxbgyd0MoWEB8405vqM1YpdrIC6o5c_W3oZSQfFpu-ePFjZexZhjHXPI9Z6ePkrJoTL-gVxXYbloDvshrwUm331cruzw9kbg==",
        "Hm_lpvt_2b63d86124773aa67d7ceadaa32c6808": "1770794570",
    }

    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ru;q=0.5",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.shenjige.cn",
        "priority": "u=1, i",
        "referer": "https://www.shenjige.cn/ziwei/base",
        "sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144", "Microsoft Edge";v="144"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }

    data = {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "genderValue": sex,
        "settings[sihua]": "D",
        "settings[brightness]": "D",
        "settings[isShowDStarBright]": "NO",
        "settings[JKXK]": "D",
        "settings[RYType]": "M",
        "settings[RYTypeM45]": "false",
        "zzpAnalysis": "N",
    }

    response = requests.post(
        "https://www.shenjige.cn/api/ziwei/getPlateArrangement",
        headers=headers,
        cookies=cookies,
        data=data,
    )
    print("Response:", response.json())
    raw_data = response.json()["data"]["zw"]

    # 提取关键信息
    simplified_data = []
    for item in raw_data:
        simplified_item = {
            "宫位": item["MangB"],
            "主星": item["StarA"],
            "凶星": item["StarB"],
            "辅星": item["StarC"] + item["Star6"]+ item["StarD"],
            "状态": item["StarF"],
        }
        if item["MangC"]:
            simplified_item["特殊标记"] = item["MangC"]
        simplified_data.append(simplified_item)

    print(simplified_data)
    return simplified_data


#
# async def main(args: Args) -> Output:
#     params = start(2000101114, "M")
#     # 构建输出对象
#     ret: Output = {
#         "zw": params
#     }
#     return ret
if __name__ == "__main__":
    start(2004101119, "M")
