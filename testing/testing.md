Лабиринт генерируется для различных параметров height и width:

![image](https://user-images.githubusercontent.com/64738836/233796985-60ce4883-1007-42bf-9261-15843bf890ec.png) ![image](https://user-images.githubusercontent.com/64738836/233797025-3e623ac1-57db-47b1-ac27-71d56f54755e.png)

При вводе не чисел или не натуральных чисел в поля height и width, выводится сообщение об ошибке:

![image](https://user-images.githubusercontent.com/64738836/233797262-c54f1ea6-32c2-4dc5-9213-4818b16d3962.png) ![image](https://user-images.githubusercontent.com/64738836/233797424-776ba7cb-eda0-4c97-a3e7-5ac723170647.png)

При получении в одном из параметров height и width значения больше 100, выводится сообщение об ошибке:

![image](https://user-images.githubusercontent.com/64738836/233797341-6a683925-7b72-4852-b261-684c70523226.png)

Путь между клетками строится для различных координат клеток:

![image](https://user-images.githubusercontent.com/64738836/233797591-bc10e0f2-d159-415a-a20c-549f04e8140b.png) ![image](https://user-images.githubusercontent.com/64738836/233797629-1cc45f51-2db7-4215-b699-805b62c132e0.png)

При вводе не чисел или не натуральных чисел в поля ввода координат клеток, выводится сообщение об ошибке:

![image](https://user-images.githubusercontent.com/64738836/233797714-d0f67b9f-7cde-4500-8a9a-b109989bc865.png) ![image](https://user-images.githubusercontent.com/64738836/233797731-13cc9cf8-21ab-48de-a9ff-40223f9e1837.png)

При получении в одной из x-координат числа больше width или в одной из y-координат числа больше height, выводится сообщение об ошибке:

![image](https://user-images.githubusercontent.com/64738836/233798002-f98bdcc5-f4c2-4262-a447-efdeb59a7503.png)

При нажатии на кнопку "Save", лабиринт сохраняется в папку data:

![image](https://user-images.githubusercontent.com/64738836/233798159-3ea730cf-4108-4dfe-8314-2f4674f2bd81.png) ![image](https://user-images.githubusercontent.com/64738836/233798181-982e8af5-6e47-45da-9452-0292bb366ea6.png)

При попытке сохранения лабиринта, пока он ещё не сгенерирован, выводится сообщение об ошибке:

![image](https://user-images.githubusercontent.com/64738836/233798117-b6f7ea82-9348-4e2b-813c-4e42fb927618.png)

При попытке импортировать файл, не являющийся лабиринтом, выводится сообщение об ошибке:

![image](https://user-images.githubusercontent.com/64738836/233798401-0efc21f7-9004-41ee-b9b6-02831b99098f.png) ![image](https://user-images.githubusercontent.com/64738836/233798412-ddc3c704-9365-45ba-9f19-aafac18d0c82.png)

