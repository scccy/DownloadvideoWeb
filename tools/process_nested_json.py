# 导入 json 模块，用来处理 json 格式的数据
import json


# 定义一个函数，用来从原始数据中提取结果
def process_nested_json(raw_data, key_path):
    # 定义一个空字典，用来存储最终的结果
    final_result = {}

    # 遍历 key 的路径数据，对每个元素进行处理
    for key in key_path:
        # 如果 key 是 "null"，则直接将其作为结果的一个键，值为 "null"
        if key == "null":
            final_result[key] = "null"
        # 否则，将 key 按照 "." 分割，得到一个列表
        else:
            key_list = key.split(".")
            # 定义一个临时变量，用来存储当前的数据
            temp_data = raw_data
            # 遍历 key 列表，对每个子键进行访问，更新临时数据
            for sub_key in key_list:
                temp_data = temp_data[sub_key]
            # 将最后一个子键作为结果的一个键，值为临时数据
            final_result[key_list[-1]] = temp_data

    # 将结果转换为 json 格式，并返回
    final_result = json.dumps(final_result, indent=4)
    return final_result
