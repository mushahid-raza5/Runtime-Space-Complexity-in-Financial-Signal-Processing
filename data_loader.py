import csv
import sys
from datetime import datetime
from models import MarketDataPoint

def load_market_data(file_path):
    data_list = []
    
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                dt = datetime.fromisoformat(row['timestamp'])
                price = float(row['price'])
                symbol = row['symbol']
                
                point = MarketDataPoint(dt, symbol, price)
                data_list.append(point)
                
    except FileNotFoundError:
        print("Could not find the file! Make sure market_data.csv is there.")
        return []
    
    if len(data_list) > 0:
        size_in_mb = sys.getsizeof(data_list) / (1024 * 1024)
        print(f"Loaded {len(data_list)} rows.")
        print(f"List structure memory usage: {size_in_mb:.4f} MB")
        
    return data_list