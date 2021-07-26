import os
import time
import sys
sys.path.append('../')
from Chapter_64_SevenSegmentDisplayModule.SevenSegment import getSevSegStr

if __name__ == "__main__":
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            currentTime = time.localtime()
            hour = currentTime.tm_hour
            minute = currentTime.tm_min
            second = currentTime.tm_sec

            hourDigit = getSevSegStr(hour, 2)
            minuteDigit = getSevSegStr(minute, 2)
            secondDigit = getSevSegStr(second, 2)

            output = []
            for idx in range(len(hourDigit)):
                line = list(hourDigit[idx] + minuteDigit[idx] + secondDigit[idx])
                if idx != 0:
                    line.insert(4, ' * ')
                    line.insert(2, ' * ')
                else:
                    line.insert(4, '   ')
                    line.insert(2, '   ')

                output.append(line)

            for line in output:
                print(' '.join(line))
            print('\nPress Ctrl-C to quit.')

            while True:
                time.sleep(0.01)
                if time.localtime().tm_sec != currentTime.tm_sec:
                    break

    except KeyboardInterrupt:
        print('\nClock ended by user.')
        sys.exit()
