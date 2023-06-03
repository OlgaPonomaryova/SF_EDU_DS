"""Game guess a number version2"""
import numpy as np

def random_predict(number:int=1) -> int:
    """random guessing of number

    Args:
        number (int, optional): guessed number. Defaults to 1.

    Returns:
        int: counts of tries
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)#predicted number
        if number == predict_number:
            break #break of cicle when number is guessed 
        
    return (count)

def score_game(random_predict) -> int:
    """За каое количество попыток в среднем угадываем 1000 загаданных чисел

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее число попыток
    """
    counts_ls = []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))#загадали список чисел
    
    for number in random_array:
        counts_ls.append(random_predict(number))
    
    score = int(np.mean(counts_ls))
    print(f'ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)

#Run 
if __name__ == '__main__':
    score_game(random_predict)
  


        
    
