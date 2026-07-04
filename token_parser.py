import json

# Parse mock token metadata from a JSON string
token_data = '{"symbol": "ETH", "name": "Ethereum", "decimals": 18, "is_active": true}'
token = json.loads(token_data)

print(f"Token: {token['name']} ({token['symbol']})")
print(f"Active status: {token['is_active']}")
