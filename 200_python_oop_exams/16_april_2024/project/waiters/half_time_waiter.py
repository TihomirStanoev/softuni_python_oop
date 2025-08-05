from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    _HOURLY_WAGE = 12.0

    @property
    def _worker_type(self):
        return 'half-time'
