'''
2593. Find Score of an Array After Marking All Elements
Medium

Companies
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm.

 
'''
def calculate_score(nums):
    n = len(nums)  # определяем длину обрабатываемого массива
    marked = [False] * n  # создаем массив длинной как обрабатываемый и заполняет его значениями False, чтобы отслеживать, 
    #какие элементы были помечены(True), а какие ещё нет(False)
    score = 0  # инициализируем счетчик
    
    for i in range(n):  # проходим по всем элементам обрабатываемого массива (i используется только для задания количества проходок по массиву)
        min_index = -1  # инициализируем для цикла индекс минимального элемента (так как массив начинается с 0, то задается число с конца массива)
        min_val = float('inf') # Бесконечно большое значение что бы первая проходка точно не сработала и пометила элемент

        for j in range(n):  # проходим по всем элементам массива для того что бы определить САМЫЙ малый элемент в массиве
            # В первом круге определяем самый малый элемент массива, в последующих сравниваем его с другими и запускаем основную логику программы

            # Eсли элемент ещё не помечен True в marked И min_index равен -1 или ЗНАЧЕНИЕ проверяемого элемента меньше ЗНАЧЕНИЯ минимального элемента определенного 
            # циклом ранее, или Значение проверяемого элемента меньше значения min_val или же равно ему и индекс текущего элемента ниже индекса минимального элемента
            if not marked[j] and (min_index == -1 or nums[j] < nums[min_index] or (nums[j] < min_val or (nums[j] == min_val and j < min_index))):  
                min_index = j  # обновляем индекс минимального элемента
                min_val = nums[j]     

        score += nums[min_index]  # добавляем минимальный элемент к счетчику 
        marked[min_index] = True  # В массиве Помеченных элементов, по индексу минимального элемента определенного в 1 круге, находим элемент с соответствующим 
        #индексом и помечаем его как использованный True  
        
        # Теперь мы получили суммирование всех элементов от самого малого к самому большому, теперь создаем алгоритм пометки соседних элементов 
        # рядом с выбранным минимальным что бы они не участвовали в счете больше.
        if min_index > 0:  # если есть предыдущий элемент
            marked[min_index - 1] = True  # помечаем его
        if min_index < n - 1:  # если есть следующий элемент
            marked[min_index + 1] = True  # помечаем его
    
    return score  # возвращаем счетчик


if __name__ == "__main__":
    nums = [3, 4, 2, 1, 5, 2]
    score = calculate_score(nums)
    print(score)  
    