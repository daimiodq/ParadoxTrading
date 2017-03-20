from ParadoxTrading.Engine import ExecutionAbstract, OrderEvent, OrderType, \
    FillEvent
from ParadoxTrading.Utils import DataStruct


class BarBacktestExecution(ExecutionAbstract):
    def __init__(self):
        super().__init__()

    def dealOrderEvent(self,
                       _order_event: OrderEvent):
        assert _order_event.order_type == OrderType.LIMIT
        fill_event = FillEvent(
            _index=_order_event.index,
            _symbol=_order_event.symbol,
            _tradingday=self.engine.getTradingDay(),
            _datetime=self.engine.getDatetime(),
            _quantity=_order_event.quantity,
            _action=_order_event.action,
            _direction=_order_event.direction,
            _price=_order_event.price,
            _commission=0.0,
        )
        self.addEvent(fill_event)

    def matchMarket(self, _symbol: str, _data: DataStruct):
        pass
