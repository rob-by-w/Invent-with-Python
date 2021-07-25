# Require SevenSegment.py from Chapter 64
import os
import time
import sys
sys.path.append('../')
from Chapter_64_SevenSegmentDisplayModule.SevenSegment import getSevSegStr

def main():
    countdown = 3602  # seconds

    try:
        while countdown >= 0:
            os.system('cls' if os.name == 'nt' else 'clear')

            hour = countdown // 3600
            minute = (countdown % 3600) // 60
            second = countdown % 60

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
            
            time.sleep(1)
            countdown -= 1
        
        print('    * * * * BOOM * * * *')

    except KeyboardInterrupt:
        print('\nCountdown ended by user.')
        sys.exit()
        
if __name__ == '__main__':
    main()