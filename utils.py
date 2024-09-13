def calculate_haste(equipment_list, enchantment_list, threshold, rank):
    """
    使用回溯算法计算最优的加速装备和附魔组合。

    :param equipment_list: 装备列表
    :param enchantment_list: 附魔列表
    :param threshold: 加速阈值
    :param rank: 品阶
    :return: 最优的总加速值、选择的装备和附魔
    """
    # 按照品阶的加速值对装备列表进行排序，并优先选择套装护手
    def equipment_priority(equip):
        if equip.name == "套装护手":
            return 1, -equip.haste_by_rank.get(rank, 0)
        elif equip.name == "套装鞋子":
            return 2, -equip.haste_by_rank.get(rank, 0)
        elif equip.name == "散件腰带":
            return 3, -equip.haste_by_rank.get(rank, 0)
        else:
            return 0, -equip.haste_by_rank.get(rank, 0)

    equipment_list.sort(key=equipment_priority)
    # 按照加速值对附魔列表进行排序，优先考虑非帽子和鞋子的附魔
    enchantment_list.sort(key=lambda x: (x.applicable_equipment[0] not in ["帽子", "鞋子"], -x.haste))

    # 使用字典缓存已经计算过的状态
    memo = {}

    def backtrack(index, current_haste, current_equipment, current_enchantments, weapon_selected):
        """
        回溯算法的实现。

        :param index: 当前索引
        :param current_haste: 当前总加速值
        :param current_equipment: 当前选择的装备
        :param current_enchantments: 当前选择的附魔
        :param weapon_selected: 是否已经选择了武器
        """
        nonlocal best_haste, best_equipment, best_enchantments

        # 如果当前加速值已经达到阈值并且选择了武器，更新最优解
        if current_haste >= threshold and weapon_selected:
            if current_haste < best_haste or best_haste == 0:
                best_haste = current_haste
                best_equipment = current_equipment[:]
                best_enchantments = current_enchantments[:]
            return

        # 缓存当前状态
        state = (index, current_haste, tuple(current_equipment), tuple(current_enchantments), weapon_selected)
        if state in memo:
            return
        memo[state] = True

        # 如果索引超出范围，返回
        if index >= len(equipment_list) + len(enchantment_list):
            return

        # 选择装备
        if index < len(equipment_list):
            equip = equipment_list[index]
            if rank in equip.haste_by_rank:
                haste = equip.haste_by_rank[rank]
                current_equipment.append((equip.name, haste))
                backtrack(index + 1, current_haste + haste, current_equipment, current_enchantments, weapon_selected or equip.is_weapon)
                current_equipment.pop()

        # 选择附魔
        if len(equipment_list) <= index < len(equipment_list) + len(enchantment_list):
            enchant = enchantment_list[index - len(equipment_list)]
            applicable = True
            for equip_name, _ in current_equipment:
                if equip_name in enchant.applicable_equipment:
                    for existing_enchant_name, _ in current_enchantments:
                        if existing_enchant_name.startswith(equip_name):
                            applicable = False
                            break
                    if applicable:
                        current_enchantments.append((enchant.name, enchant.haste))
                        backtrack(index + 1, current_haste + enchant.haste, current_equipment, current_enchantments, weapon_selected)
                        current_enchantments.pop()
                    break

        # 跳过当前装备或附魔
        backtrack(index + 1, current_haste, current_equipment, current_enchantments, weapon_selected)

    # 初始化最优解
    best_haste = 0
    best_equipment = []
    best_enchantments = []

    # 开始回溯
    backtrack(0, 0, [], [], False)

    return best_haste, best_equipment, best_enchantments


class HasteCalculator:
    """
    HasteCalculator 类用于计算最优的加速装备和附魔组合。
    """
    def __init__(self, equipment_list, enchantment_list):
        """
        初始化 HasteCalculator 实例。

        :param equipment_list: 装备列表
        :param enchantment_list: 附魔列表
        """
        self.equipment_list = equipment_list
        self.enchantment_list = enchantment_list

    def calculate(self, threshold, rank, weapon_type):
        """
        计算最优的加速装备和附魔组合。

        :param threshold: 加速阈值
        :param rank: 品阶，可以是 "普通" 或 "英雄"
        :param weapon_type: 武器类型，可以是 "加速武器", "橙武", "无加速武器"
        :return: 计算结果字典，包含总加速等级、溢出值、选择的品阶、武器类型、装备和附魔
        """
        # 查找指定的武器类型
        selected_weapon = next((equip for equip in self.equipment_list if equip.name == weapon_type), None)
        if selected_weapon is None:
            raise ValueError(f"指定的武器类型 '{weapon_type}' 不存在于装备列表中。")

        # 过滤掉所有武器类型的装备，并添加选定的武器
        filtered_equipment_list = [equip for equip in self.equipment_list if not equip.is_weapon]
        filtered_equipment_list.append(selected_weapon)

        # 计算总加速值和选择的装备、附魔
        total_haste, selected_equipment, selected_enchantments = calculate_haste(filtered_equipment_list, self.enchantment_list, threshold, rank)
        overflow = total_haste - threshold

        # 过滤掉无加速的装备
        selected_equipment = [equip for equip in selected_equipment if equip[1] > 0]

        return {
            'total_haste': total_haste,
            'overflow': overflow,
            'rank': rank,
            'weapon_type': weapon_type,
            'selected_equipment': selected_equipment,
            'selected_enchantments': selected_enchantments
        }
