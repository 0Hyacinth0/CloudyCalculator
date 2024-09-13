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

    def __init__(self):
        """
        初始化 EnchantmentManager 实例，并定义附魔列表。
        """
        self.enchantment_list = [
            Enchantment("帽子紫色附魔", 2089, ["散件帽子"]),
            Enchantment("鞋子紫色附魔", 2089, ["套装鞋子"]),
            Enchantment("武器五彩石", 2925, ["加速武器", "橙武", "无加速武器"]),
            # Enchantment("暗器附魔", 974, ["加速暗器"])
        ]

    def get_enchantment_list(self):
        """
        获取附魔列表。

        :return: 附魔列表
        """
        return self.enchantment_list


# 创建 EnchantmentManager 实例
enchantment_manager = EnchantmentManager()

# 获取附魔列表
enchantment_list = enchantment_manager.get_enchantment_list()
