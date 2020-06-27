# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import random
from rainbow_print import printr
from rainbow_print import rlogging
import logging
logging.basicConfig(level=logging.INFO)
logger = rlogging.getLogger(__name__)


class TestSimple(unittest.TestCase):

    def generate_random_data(self, string=False):
        d = {
            "Episode": 1,
            "Ep Len": random.randrange(0, 200),
            "Actor Loss": round(random.uniform(0, 1), 2),
            "Critic Loss": round(random.uniform(0, 1), 2),
            "Loss": round(random.uniform(0, 1), 2),
            "Gamma": round(random.uniform(0, 1), 4),
            "INT Reward": random.randrange(0, 50),
            "EXT Reward": random.randrange(0, 50),
            "Reward": random.randrange(0, 100),
            "Mode": ["Explore", "Exploit"][random.randrange(0, 2)]
        }
        if string:
            str_builder = ''
            for k, v in d.items():
                str_builder += f"{k}:{v},"
            return str_builder
        return d

    # def test_print_dict(self):
    #     printr.update_light_palette()
    #     for i in range(10):
    #         printr(self.generate_random_data(string=False))

    def test_print_str(self):
        for i in range(10):
            logger.info(self.generate_random_data(string=True), sep=',')


if __name__ == '__main__':
    unittest.main()
