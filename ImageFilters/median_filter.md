# Медианный фильтр

Медианный фильтр — один из видов цифровых фильтров, широко используемый в цифровой обработке сигналов и изображений для уменьшения уровня шума. 

#  Алгоритм
+ Из соседей пикселя [i,j] формируем вектор
+ Сортируем вектор по возрастанию
+ Значение, находящееся в середине упорядоченного вектора, поступает на выход фильтра

Ниже представлены результаты работы алгоритма, c использованием матрицы свертки 3x3 и 5x5

![Примеры ](https://github.com/IvankoPo/Python/raw/master/ImageFilters/lenaShum.jpg)
![Примеры ](https://github.com/IvankoPo/Python/raw/master/ImageFilters/lenaShumFiltered3.jpg)
![Примеры ](https://github.com/IvankoPo/Python/raw/master/ImageFilters/lenaShumFiltered5.jpg)
