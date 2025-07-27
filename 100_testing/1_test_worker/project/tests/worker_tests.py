from project.worker import Worker
from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('test', 1000, 5)

    def test_init(self):
        self.assertEqual(self.worker.name, 'test')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 5)

    def test_energy_is_incremented_after_rest(self):
        incremented_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(self.worker.energy, incremented_energy)

    def test_if_the_worker_tries_to_work_negative_or_zero_energy(self):
        for energy in [-5,0]:
            with self.subTest(energy=energy):
                self.worker.energy = energy
                with self.assertRaises(Exception) as e:
                    self.worker.work()
                self.assertEqual(str(e.exception), 'Not enough energy.')

    def test_money_increased_after_work(self):
        expected_money = self.worker.money + self.worker.salary
        self.worker.work()
        self.assertEqual(expected_money, self.worker.money)

    def test_energy_is_decreased_after_work(self):
        expected_energy = self.worker.energy - 1
        self.worker.work()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info(self):
        result = self.worker.get_info()
        expected_result = f'{self.worker.name} has saved {self.worker.money} money.'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    main()

