import json

class Enchantment:
    """
    Enchantment 类表示一个附魔。
    """

    def __init__(self, name, haste, applicable_equipment):
        """
        初始化 Enchantment 实例。

        :param name: 附魔名称
        :param haste: 附魔提供的加速值
        :param applicable_equipment: 附魔适用的装备类型
        """
        self.name = name  # 附魔名称
        self.haste = haste  # 附魔提供的加速值
        self.applicable_equipment = applicable_equipment  # 附魔适用的装备类型


class EnchantmentManager:
    """
    EnchantmentManager 类用于管理附魔列表。
    """

    def __init__(self, json_file):
        """
        初始化 EnchantmentManager 实例，并定义附魔列表。
        """
        self.enchantment_list = self.load_enchantments(json_file)

    def load_enchantments(self, json_file):
        """
        从 JSON 文件中加载附魔数据。
        """
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Enchantment(**item) for item in data]

    def get_enchantment_list(self):
        """
        获取附魔列表。

        :return: 附魔列表
        """
        return self.enchantment_list


# 创建 EnchantmentManager 实例
enchantment_manager = EnchantmentManager('enchantments.json')

# 获取附魔列表
enchantment_list = enchantment_manager.get_enchantment_list()
