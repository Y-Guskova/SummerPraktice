# SummerPraktice
# Система управления роботом на основе KasperskyOS c помощью веб камеры
___
### Команда: __"Самая красивая команда этого хакатона"__
---

## Краткое описание:
Управление Alphabot-ом с RaspberryPi 4 с ядром KasperskyOS с помощью GPIO, TCP и веб-камеры. 
![Alphabot](https://github.com/Y-Guskova/SummerPraktice/blob/main/alphabot.jpeg)
___
### Цель:
1. Реализовать удаленное соединение робота с управляющей программой поTCP протоколу в одной локальной среде.
2. Реализовать функционал с управлением двигателем через порты GPIO.
3. Реализовать функционал распознавания робота и его целей.
4. Создать алгоритм управления роботом через внешнюю камеру.
![Схема](https://github.com/Y-Guskova/SummerPraktice/blob/main/scheme.jpeg) 
___
### Реализация:

> - [__Detect_color__](https://github.com/Y-Guskova/SummerPraktice/tree/main/Detect_color)
 >>[color.py](https://github.com/Y-Guskova/SummerPraktice/blob/main/Detect_color/color.py) - программа распознования стикеров разных цветов, записи координат их расположения и переводом в реальные координаты с помощью гомографии, написанная на Python.
 >>![Распознование стикеров](https://github.com/Y-Guskova/SummerPraktice/blob/main/detecting.jpeg)
 >>![Координаты стикеров](https://github.com/Y-Guskova/SummerPraktice/blob/main/coord.jpeg)
 >>![Траектопия](https://github.com/Y-Guskova/SummerPraktice/blob/main/trajectory.jpg)

> - [__GPIO_output__](https://github.com/Y-Guskova/SummerPraktice/tree/main/gpio_output) - интерфейс ввода-вывода пинов Alphabot. 
 >>client
 >>>src 
 >>>>[gpio.c](https://github.com/Y-Guskova/SummerPraktice/blob/main/gpio_output/client/src/gpio.c)
 >>>>```{c} {#define GPIO_PIN_NUM_IN1 12U
>>>>#define GPIO_PIN_NUM_IN2 13U
>>>>#define GPIO_PIN_NUM_ENA 6U
>>>>#define GPIO_PIN_NUM_IN4 20U
>>>>#define GPIO_PIN_NUM_IN3 21U
>>>>#define GPIO_PIN_NUM_ENB 26U
>>>>#define DELAY_S 2
>>>>
>>>> /*Указываем пины, создаем функци back, forward, left, right, stop, подавая сигналы 1 и 0 на определенные порты. В main-е вызываем функции.*/
>>[mount.sh](https://github.com/Y-Guskova/SummerPraktice/blob/main/gpio_output/mount.sh) - сценарий, записывабщий образ kos-image на sd-карту

> - [__TCP/tcpserver__](https://github.com/Y-Guskova/SummerPraktice/tree/main/TCP/tcpserver)
> -[__hello_with_args__](https://github.com/Y-Guskova/SummerPraktice/tree/main/hello_with_args)
> - [__mqtt_publisher__](https://github.com/Y-Guskova/SummerPraktice/tree/main/mqtt_publisher)
> - [__net_server__](https://github.com/Y-Guskova/SummerPraktice/tree/main/net_server)
> - [__separate_storage__](https://github.com/Y-Guskova/SummerPraktice/tree/main/separate_storage)
>>- примеры из KOS SDK, собранные при изучении и начале работы с KOS.

> - [__linux_client__](https://github.com/Y-Guskova/SummerPraktice/tree/main/linux_client)
> - [__TCP/tcpserver__](https://github.com/Y-Guskova/SummerPraktice/tree/main/TCP/tcpserver)
>> - попытка соединения с Alphabot через TCP и передачи сообщения.
___
### Проблемы:
Не ассоциировано совместное использование GPIO и сети. Обусловлено ошибками при написании psl-политик.
___
### Итог:
Реализация езды Alphabot по заданной траектории (прямоугольник) на KOS.
[Видео тут.](https://github.com/Y-Guskova/SummerPraktice/blob/main/AlphaBot.MOV)
___
### Инструкция:
1. [Скачать KsperskyOS](https://os.kaspersky.ru/development/).
2. Ввести в командной строке:
 >./cross-build.sh
3. Записать kos-image на SD-карту:
>./mount.sh
4. Вставить карту в робота и включить его.
___
### Лицензия распространения 
> MIT



