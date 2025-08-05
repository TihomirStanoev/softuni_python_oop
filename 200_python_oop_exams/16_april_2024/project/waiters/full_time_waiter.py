from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    _HOURLY_WAGE = 15.0

    @property
    def _worker_type(self):
        return 'full-time'
