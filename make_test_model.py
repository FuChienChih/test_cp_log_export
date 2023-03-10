import datetime


class MakeTestsModule:
    def make_test_status_running_file(self):
        CURRENT_TIME = datetime.datetime.now()
        input_file = 'name: Server1 \n      status: Running (15538)\n     ' + \
            f' last log read at: {CURRENT_TIME.day} Feb  ' + \
            f'{CURRENT_TIME.hour}:{CURRENT_TIME.minute}:{CURRENT_TIME.second}\n' + \
            '      debug file: /opt/CPmds-R81.10/customers/fwmgr' + \
            '/CPrt-R81.10/log_exporter/targets/'

        output_file = "Server1 is ok"

        self._make_input_output_file(input_file, output_file)

    def make_test_status_not_running_file(self):
        CURRENT_TIME = datetime.datetime.now()
        input_file = 'name: Server1 \n      status: Not Running (15538)\n      ' + \
            f'last log read at: {CURRENT_TIME.day} Feb  ' + \
            f'{CURRENT_TIME.hour}:{CURRENT_TIME.minute}:{CURRENT_TIME.second}\n' + \
            '      debug file: /opt/CPmds-R81.10/customers/fwmgr' + \
            '/CPrt-R81.10/log_exporter/targets/'

        output_file = 'Server: Server1:\nReason: Not running\nDetail:\n' + \
            'name: Server1 \n      status: Not Running (15538)\n      ' + \
            f'last log read at: {CURRENT_TIME.day} Feb  ' + \
            f'{CURRENT_TIME.hour}:{CURRENT_TIME.minute}:{CURRENT_TIME.second}\n'

        self._make_input_output_file(input_file, output_file)

    def make_test_time_exceed_file(self):
        CURRENT_TIME = datetime.datetime.now()
        DELTATIME = 40  # min
        CURRENT_TIME_SUB_DELTATIME = CURRENT_TIME - \
            datetime.timedelta(minutes=DELTATIME)
        input_file = 'name: Server1 \n      status: Running (15538)\n      ' + \
            f'last log read at: {CURRENT_TIME_SUB_DELTATIME.day} Feb  ' + \
            f'{CURRENT_TIME_SUB_DELTATIME.hour}:' + \
            f'{CURRENT_TIME_SUB_DELTATIME.minute}:{CURRENT_TIME_SUB_DELTATIME.second}\n' + \
            '      debug file: /opt/CPmds-R81.10/customers/fwmgr' + \
            '/CPrt-R81.10/log_exporter/targets/'

        output_file = 'Server: Server1:\nReason: Exceed max_interval: 30 Mins\n' + \
            'Current Time: ' + CURRENT_TIME.strftime("%d %b %H:%M:%S") + \
            f'(Interval: {DELTATIME})\n' + \
            'Detail:\n' + \
            'name: Server1 \n      ' + \
            'status: Running (15538)\n      ' + \
            f'last log read at: {CURRENT_TIME_SUB_DELTATIME.day} Feb  ' + \
            f'{CURRENT_TIME_SUB_DELTATIME.hour}:' + \
            f'{CURRENT_TIME_SUB_DELTATIME.minute}:{CURRENT_TIME_SUB_DELTATIME.second}\n'

        self._make_input_output_file(input_file, output_file)

    def make_test_time_through_year_file(self):
        pass

    def _make_input_output_file(self, input_file, output_file):
        with open('./input_file.txt', 'w') as f:
            f.write(input_file)
        with open('./output_file.txt', 'w') as f:
            f.write(output_file)
