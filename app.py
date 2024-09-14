from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from enchantments import enchantment_manager
from equipment import equipment_manager
from utils import HasteCalculator
import os


class HasteApp:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, resources={r"/*": {"origins": "*"}})  # 允许所有来源
        self.haste_calculator = HasteCalculator(equipment_manager.get_equipment_list(), enchantment_manager.get_enchantment_list())
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return send_from_directory('static', 'index.html')

        @self.app.route('/favicon.ico')
        def favicon():
            return send_from_directory(os.path.join(self.app.root_path, 'static'),
                                       'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
