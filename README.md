The goal of the project: 
Writing a simple script for moving forward using the RPi.GPIO library.

Общее описание проекта RobotMotorsControl:

Тестирование пинов Raspberry Pi.
Первый скрипт и тест на основе двух пинов и одного двигателя только движение вперёд.
В дальнейшем были внесены изменения в код и добавлены пины и двигатель для движения назад.

================

Для работы над проектом на GitHub был создан пустой репозитарий:
https://github.com/Sarmatae/RobotMotorsControl

После этого он был склонирован на Raspberry Pi под управлением Ubuntu сервер 20.04
Команда:
git clone https://github.com/Sarmatae/RobotMotorsControl.git  

Созданы файл первого скрипта move_forward.py и файл README.md.

Оба файла добавлены командой:
git add *

И закомичены с сообщением:
git commit -m "Add general script and readme files"

Затем запушены на GitHub (при этом необходимо было ввести имя пользователя, 
и предварительно сгенирированный токен на GitHub с правом записи контента).
Желательно перед этим выполнить команду git pull (могли быть внесены измения в удалёнке и чтобы избежать конфликтов):
git push -u origin master

Создана новая ветка и в неё перенесены все предыдущие изменения:
git checkout -b new_movement

После паузы проверка на активность ветки:
git branch

Были внесены правки в код (добавлено движение вперёд) добавлены, закоммичены, запушена новая ветка на GitHub:
git add move_forward.py
git commit -m "Add moving backwards"
git push --set-upstream origin new_movement
