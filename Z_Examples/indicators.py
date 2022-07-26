import pandas as pd
import pandas_ta as ta

# Help about this, 'ta', extension
help(pd.DataFrame().ta)

# List of all indicators
print(pd.DataFrame().ta.indicators())


# Help about the log_return indicator
help(ta.log_return)
