import json

class Equipment:
    """
    Equipment 类表示一件装备。
    """

    def __init__(self, name, haste_by_rank, is_weapon=False):
        """
        初始化 Equipment 实例。

        :param name: 装备名称
        :param haste_by_rank: 不同品阶下的加速值
        :param is_weapon: 是否为武器
        """
        self.name = name  # 装备名称
        self.haste_by_rank = haste_by_rank  # 不同品阶下的加速值
        self.is_weapon = is_weapon  # 是否为武器


class EquipmentManager:
    """
    EquipmentManager 类用于管理装备列表。
    """

    def __init__(self, json_file):
        """
        初始化 EquipmentManager 实例，并定义装备列表。

        :param json_file: JSON 文件路径
        """
        self.equipment_list = self.load_equipment(json_file)

    def load_equipment(self, json_file):
        """
        从 JSON 文件中加载装备数据。

        :param json_file: JSON 文件路径
        :return: 装备列表
        """
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Equipment(**item) for item in data]

    def get_equipment_list(self):
        """
        获取装备列表。

        :return: 装备列表
        """
        return self.equipment_list


# 创建 EquipmentManager 实例
equipment_manager = EquipmentManager('equipment.json')

# 获取装备列表
equipment_list = equipment_manager.get_equipment_list()
