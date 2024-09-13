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

    def __init__(self):
        """
        初始化 EquipmentManager 实例，并定义装备列表。
        """
        self.equipment_list = [
            Equipment("散件帽子", {"普通": 8149, "英雄": 9379}),
            Equipment("散件上衣", {"普通": 9054, "英雄": 10422}),
            Equipment("散件腰带", {"普通": 6338, "英雄": 7295}),
            Equipment("套装护手", {"普通": 6338, "英雄": 7295}),
            Equipment("散件下装", {"普通": 9054, "英雄": 10422}),
            Equipment("套装鞋子", {"普通": 6338, "英雄": 7295}),
            Equipment("加速项链", {"普通": 4527, "英雄": 5211}),
            Equipment("加速腰坠", {"普通": 4527, "英雄": 5211}),
            Equipment("加速戒指上", {"普通": 4527, "英雄": 5211}),
            Equipment("加速戒指下", {"普通": 4527, "英雄": 5211}),
            Equipment("加速暗器", {"普通": 5432, "英雄": 6253}),
            Equipment("加速武器", {"普通": 10865, "英雄": 12507}, is_weapon=True),
            Equipment("橙武", {"普通": 8228 "英雄": 8228}, is_weapon=True),
            Equipment("无加速武器", {"普通": 0, "英雄": 0}, is_weapon=True)
        ]

    def get_equipment_list(self):
        """
        获取装备列表。

        :return: 装备列表
        """
        return self.equipment_list


# 创建 EquipmentManager 实例
equipment_manager = EquipmentManager()

# 获取装备列表
equipment_list = equipment_manager.get_equipment_list()
