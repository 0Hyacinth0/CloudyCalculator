from enchantments import enchantment_list
from equipment import equipment_list
from utils import HasteCalculator


def print_result(result):
    """
    打印计算结果。

    :param result: 计算结果字典，包含总加速等级、溢出值、选择的品阶、武器类型、装备和附魔
    """
    print(f"总加速等级: {result['total_haste']}")
    print(f"溢出值: {result['overflow']}")
    print(f"选择的品阶: {result['rank']}")
    print(f"选择的武器类型: {result['weapon_type']}")

    print("最优配装（套装鞋子无根骨孔）:")
    for equip_name, haste in result['selected_equipment']:
        print(f"  - {equip_name}: {haste}")

    print("附魔选择:")
    for enchant_name, haste in result['selected_enchantments']:
        print(f"  - {enchant_name}: {haste}")

    print("注：由于暗器附魔存在根骨附魔，所以暂不考虑使用暗器加速附魔。")


class HasteOptimizer:
    """
    HasteOptimizer 类用于优化加速装备和附魔的选择，以达到或超过设定的加速阈值。
    """

    def __init__(self, threshold, rank, weapon_type):
        """
        初始化 HasteOptimizer 实例。

        :param threshold: 加速阈值
        :param rank: 品阶，可以是 "普通" 或 "英雄"
        :param weapon_type: 武器类型，可以是 "加速武器", "橙武", "无加速武器"
        """
        self.threshold = threshold
        self.rank = rank
        self.weapon_type = weapon_type
        self.haste_calculator = HasteCalculator(equipment_list, enchantment_list)

    def calculate_and_print(self):
        """
        计算最优的加速装备和附魔组合，并打印结果。
        """
        try:
            # 调用 HasteCalculator 的 calculate 方法进行计算
            result = self.haste_calculator.calculate(self.threshold, self.rank, self.weapon_type)
            # 打印计算结果
            print_result(result)
        except ValueError as e:
            # 捕获并打印异常
            print(f"Error: {e}")


if __name__ == "__main__":
    # 定义加速阈值和品阶
    THRESHOLD = 46160  # 设定的加速阈值
    RANK = "普通"  # 可以选择 "普通" 或 "英雄" 品阶

    # 手动指定武器类型
    weapon_type = "无加速武器"  # 可以选择 "加速武器", "橙武", "无加速武器"

    # 创建 HasteOptimizer 实例并执行计算
    optimizer = HasteOptimizer(THRESHOLD, RANK, weapon_type)
    optimizer.calculate_and_print()
