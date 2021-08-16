import random
import time


def main():
    print('Progess Bar Simulation')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        bytesDownloaded += random.randint(0, 100)

        barStr = get_progress_bar(bytesDownloaded, downloadSize)
        print(barStr, end='', flush=True)
        time.sleep(0.2)
        print('\b' * len(barStr), end='', flush=True)

    barStr = get_progress_bar(bytesDownloaded, downloadSize)
    print(barStr, end='', flush=True)
    print('\nDownload completed!')


def get_progress_bar(progress, total, width=40):
    BAR = chr(9608)

    progressBar = '['
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    numberOfBars = int((progress / total) * width)
    progressBar += BAR * numberOfBars
    progressBar += ' ' * (width - numberOfBars)
    progressBar += ']'

    percentComplete = round(progress/total * 100, 1)
    progressBar += f' {percentComplete}%'
    progressBar += f' {progress}/{total}'

    return progressBar


if __name__ == "__main__":
    main()
