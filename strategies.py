from collections import deque
from models import Strategy

class NaiveMovingAverageStrategy(Strategy):
    """
    This strategy is slow because it calculates the average from scratch every time.
    Time Complexity: O(N) per tick because of the loop.
    Space Complexity: O(N) to store the history list.
    """
    def __init__(self):
        self.history = []

    def generate_signals(self, tick):
        self.history.append(tick.price)
        total_sum = 0
        for price in self.history:
            total_sum += price
            
        avg = total_sum / len(self.history)
        
        if tick.price > avg:
            return {'action': 'SELL', 'price': tick.price}
        elif tick.price < avg:
            return {'action': 'BUY', 'price': tick.price}
        return None

class WindowedMovingAverageStrategy(Strategy):
    """
    This strategy is fast because it uses a sliding window (deque).
    Time Complexity: O(1) per tick because we just pop one and add one.
    Space Complexity: O(K) where K is the window size.
    """
    def __init__(self, window_size=100):
        self.window_size = window_size
        self.window = deque(maxlen=window_size)
        self.current_sum = 0.0

    def generate_signals(self, tick):
        if len(self.window) == self.window_size:
            self.current_sum -= self.window[0]
            
        self.window.append(tick.price)
        self.current_sum += tick.price
        
        avg = self.current_sum / len(self.window)
        
        if tick.price > avg:
            return {'action': 'SELL', 'price': tick.price}
        elif tick.price < avg:
            return {'action': 'BUY', 'price': tick.price}
        return None