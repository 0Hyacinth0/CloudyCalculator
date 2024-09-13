from flask import Flask, request, jsonify
from enchantments import enchantment_list
from equipment import equipment_list
from utils import HasteCalculator


class HasteApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.haste_calculator = HasteCalculator(equipment_list, enchantment_list)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/calculate', methods=['POST'])
        def calculate():
            try:
                data = request.get_json()
                threshold = data.get('threshold', 46160)
                rank = data.get('rank', '普通')
                weapon_type = data.get('weaponType', '无加速武器')

                result = self.haste_calculator.calculate(threshold, rank, weapon_type)
                return jsonify(result)
            except Exception as e:
                return jsonify({'error': str(e)}), 500

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    app = HasteApp()
    app.run()
