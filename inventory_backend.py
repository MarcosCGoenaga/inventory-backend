from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Temporary in-memory storage
inventory_data = {
    "vendorLeadTime": "25",
    "dcClubLeadTime": "23",
    "maxOrderDays": "24",
    "safetyStockDays": "7",
    "orderCycleDays": "14",
    "dailyDemand": "2.29",
    "clubOnHand": "24",
    "pipelineQuantity": "24",
    "leadTimeDemand": "126",
    "orderCycleDemand": "32",
    "safetyStock": "16",
    "replenishPoint": "174",
    "needQuantity": "48",
}

@app.route("/get", methods=["GET"])
def get_inventory():
    return jsonify(inventory_data)

@app.route("/update", methods=["POST"])
def update_inventory():
    global inventory_data
    data = request.json
    inventory_data.update(data)  # Update stored values
    return jsonify({"message": "Inventory updated successfully", "data": inventory_data})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
