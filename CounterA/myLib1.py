from chardet.universaldetector import UniversalDetector
def int_Input(m, text):
    """Funtion to input integers"""
    nums = []
    i=0 #Счетчик
    
    while i<m:
        try:#конструкция для обработки исключений
            i=i+1  
            n = int(input(text))
            nums.append(n)
        except ValueError:
            print('Можно вводить только числа')
            i=i-1   
    return nums
def detect_encoding(filename):
    detector = UniversalDetector()
    with open(filename, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result

def count_letters_RU(text):
    first = 0
    last = 0
    #Найдем в таблице Unicode точку входа т.е. букву "А" 
    #и точку выхода букву "я" и запишем их порядковые номера в переменные first и last
    for i in range(0,10000):
        if chr(i) == 'А':
            first = i
        elif chr(i) == 'я':
            last = i
            break # выход из цикла
    #Создадим пустой список
    alphabet=[]
    #С помощью цикла заполним спиксок
    for i in range(first,last+1):
        alphabet.append(chr(i))

    for i in range(0,10000):
        if chr(i) == 'Ё':
            alphabet.append(chr(i))

        elif chr(i) == 'ё':
            alphabet.append(chr(i))
            break # выход из цикла
    alphabet.insert(alphabet.index('е')+1,alphabet.pop(-1))
    alphabet.insert(alphabet.index('Е')+1,alphabet.pop(-1))
    counter={}
    for letter in alphabet:
        n=text.count(letter)
        counter[letter]=n
    return counter