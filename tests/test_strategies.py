import unittest
from datetime import datetime
from strategies import WindowedMovingAverageStrategy
from models import MarketDataPoint

class TestStrategies(unittest.TestCase):
    def test_windowed_strategy_logic(self):
        strategy = WindowedMovingAverageStrategy(window_size=2)
        tick1 = MarketDataPoint(datetime.now(), "AAPL", 100.0)
        tick2 = MarketDataPoint(datetime.now(), "AAPL", 110.0)
        
        self.assertIsNone(strategy.generate_signals(tick1))
        sig = strategy.generate_signals(tick2)
        self.assertEqual(sig['action'], 'SELL')

if __name__ == '__main__':
    unittest.main()