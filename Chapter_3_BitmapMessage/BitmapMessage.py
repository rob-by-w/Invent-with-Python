def main():
    print('Enter the message to display with the bitmap.')
    inputMessage = input_message()
    
    with open('bitmapworld.txt', 'r') as rawBitmap:
        bitmap = rawBitmap.readlines()
    
    print(''.join(replace_bitmap(bitmap, inputMessage)))

def input_message():
    while True:
        inputMessage = input('> ')
        
        if inputMessage != '':
            break
        
        print('Empty message. Please input a message.')
        
    return inputMessage

def replace_bitmap(bitmap, message):
    messageLength = len(message)
    bitmapMessage = []
    replaceChar = ['.', '*']
    
    for line in bitmap:
        idx = 0
        lineMessage = ''
        for char in line:
            lineMessage += message[idx % messageLength] if char in replaceChar else char
            idx += 1
            
        bitmapMessage.append(lineMessage)
    
    return bitmapMessage
    
if __name__ == '__main__':
    main()