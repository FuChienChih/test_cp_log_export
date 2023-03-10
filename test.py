import unittest
import os
from make_test_model import MakeTestsModule

OUTPUTPATH = os.path.join(".", os.path.splitext(os.path.basename(__file__))[0])


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.file_maker = MakeTestsModule()

    def test_status_running(self):
        # Arrange
        self.file_maker.make_test_status_running_file()
        test_input, expected_output = test_input_and_oexpected_output()

        # Act
        execute_main_program_by_test_input(test_input)

        # Assert
        test_output = test_input_and_oexpected_output()
        self.assertEqual(test_output, expected_output)

    def test_status_not_running(self):
        # Arrange
        self.file_maker.make_test_status_not_running_file()
        test_input, expected_output = test_input_and_oexpected_output()

        # Act
        execute_main_program_by_test_input(test_input)

        # Assert
        test_output = test_input_and_oexpected_output()
        self.assertEqual(test_output, expected_output)

    def test_time_exceed(self):
        # Arrange
        self.file_maker.make_test_time_exceed_file()
        test_input, expected_output = test_input_and_oexpected_output()

        # Act
        execute_main_program_by_test_input(test_input)

        # Assert
        test_output = test_input_and_oexpected_output()
        self.assertEqual(test_output, expected_output)

    # def test_time_through_year(self):
    #     CURRENT_TIME = datetime.datetime(2025, 1, 1, 0, 0, 1)
    #     test_input = 'name: Server1 \n      status: Running (15538)\n      last log read at: 31 Dec  23:59:59\n      debug file: /opt/CPmds-R81.10/customers/fwmgr/CPrt-R81.10/log_exporter/targets/'

    #     # Act
    #     with open('./cp_log_export_output.txt', 'w') as f:
    #         f.write(test_input)

    #     exec(open("cp_log_export.py").read(), globals())
    #     # Assert
    #     with open(os.path.join(OUTPUTPATH, 'output.txt'), "r") as f:
    #         test_output = f.read()
    #     expected_output = 'Server1 is ok'
    #     self.assertEqual(test_output, expected_output)
    def tearDown(self):
        try:
            os.remove("./input_file.txt")
            os.remove("./output_file.txt")
            os.remove("./test/output.txt")
            os.rmdir("./test")
        except OSError:
            pass


def test_input_and_oexpected_output():
    with open("./input_file.txt", "r") as f:
        test_input = f.read()
    with open("./output_file.txt", "r") as f:
        expected_output = f.read()
    return test_input, expected_output


def execute_main_program_by_test_input(test_input):
    with open("./cp_log_export_output.txt", "w") as f:
        f.write(test_input)
    exec(open("cp_log_export.py").read(), globals())


def open_test_output_file():
    with open(os.path.join(OUTPUTPATH, "output.txt"), "r") as f:
        return f.read()


if __name__ == "__main__":
    unittest.main()
