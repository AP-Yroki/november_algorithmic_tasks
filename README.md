# november_algorithmic_tasks
Алгоритмические задачи на Ноябрь 2023
1) Учитывая массив целых чисел(nums), отсортированных в порядке неубывания, найдите начальную и конечную позицию заданного целевого значения(target).

Если target не найден в массиве, верните [-1, -1].

Вы должны написать алгоритм со сложностью выполнения O(log n).

Пример 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Пример 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Пример 3:

Input: nums = [], target = 0
Output: [-1,-1]


2) Учитывая матрицу размера m x n, верните все элементы матрицы в спиральном порядке.

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
Пример: 


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

3) Определите, действительна ли доска для судоку 9 x 9. Только заполненные ячейки подлежат проверке согласно следующим правилам:

    Каждая строка должна содержать цифры от 1 до 9 без повторений.
    Каждый столбец должен содержать цифры 1–9 без повторений.
    Каждый из девяти подполей сетки размером 3х3 должен содержать цифры от 1 до 9 без повторений.

Примечание:

    Доска судоку (частично заполненная) может быть допустимой, но не обязательно решаемой.
    Только заполненные ячейки должны быть проверены в соответствии с указанными правилами.

Пример 1: 

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Пример 2: 

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
