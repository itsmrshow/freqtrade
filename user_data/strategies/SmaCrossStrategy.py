import talib.abstract as ta
from pandas import DataFrame

from freqtrade.strategy import IStrategy


class SmaCrossStrategy(IStrategy):
    """Simple SMA cross strategy."""

    minimal_roi = {"0": 0.01}
    stoploss = -0.10
    timeframe = "5m"

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["sma_short"] = ta.SMA(dataframe["close"], timeperiod=20)
        dataframe["sma_long"] = ta.SMA(dataframe["close"], timeperiod=50)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe["sma_short"] > dataframe["sma_long"]),
            "enter_long",
        ] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe["sma_short"] < dataframe["sma_long"]),
            "exit_long",
        ] = 1
        return dataframe
