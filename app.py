import gradio as gr

from enchantments import enchantment_list
from equipment import equipment_list
from utils import HasteCalculator

TEMPLATE = """
总加速等级: {}
溢出值: {}
选择的品阶: {}
选择的武器类型: {}
最优配装（套装鞋子无根骨孔）:
{}

附魔选择:
{}

注：由于暗器附魔存在根骨附魔，所以暂不考虑使用暗器加速附魔。
"""


class HasteApp:

    def __init__(self):
        self.haste_calculator = HasteCalculator(equipment_list, enchantment_list)
        with gr.Blocks() as self.app:
            threshold = gr.Slider(minimum=0, maximum=100000, step=1, label='Threshold', value=46160)
            with gr.Row():
                rank = gr.Dropdown(label="Rank", choices=["英雄", "普通"])
                weapon_type = gr.Dropdown(label="Weapon Type", choices=["无加速武器", "加速武器", "橙武"])
            button = gr.Button("Calculate")
            result = gr.Textbox(label="Result")
            button.click(self.calculate, inputs=[threshold, rank, weapon_type], outputs=result)

    def calculate(self, threshold, rank, weapon_type):
        result = self.haste_calculator.calculate(threshold, rank, weapon_type)
        template_args = list(result.values())
        template_args[-2] = "\n".join((f"  - {equip_name}: {haste}" for equip_name, haste in template_args[-2]))
        template_args[-1] = "\n".join((f"  - {enchant_name}: {haste}" for enchant_name, haste in template_args[-1]))

        return TEMPLATE.format(*template_args)

    def run(self):
        self.app.title = "Haste Calculator"
        self.app.queue()
        self.app.launch()


if __name__ == '__main__':
    app = HasteApp()
    app.run()
