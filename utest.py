import sys

sys.path.append("src/")

from test_unica.utest.tools.test_function_dict import *
from test_unica.utest.tools.test_function_jwt import *
from test_unica.utest.models.test_user import *

if __name__ == '__main__':
    unittest.main(verbosity=2)