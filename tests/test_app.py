# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
import unittest
FILE = Path(__file__).resolve().parents[1] / "CoinFlipping.py"
spec = importlib.util.spec_from_file_location("app_under_test", FILE)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)
class ApplicationTests(unittest.TestCase):

    def test_coin(self):
        self.assertTrue({app.toss() for _ in range(200)} <= {"Heads", "Tails"})

    def test_gui(self):
        window = app.CoinApp()
        try:
            window.flip()
            self.assertEqual(window.count, 1)
            window.reset()
            self.assertEqual(window.count, 0)
        finally: window.destroy()

if __name__ == "__main__":
    unittest.main()
