# Flask Shop проект
### Проєкт для продажу різноманітного товару

---

## Склад нашої команди:
0. Микола Скрипник - Створив дизайн для всього нашого сайту
1. [Терешонок Максим](https://github.com/TereshonokMaksim) - Тімлід команди
2. [Агеев Данило](https://github.com/Ageev-Danilo) - Активний написач коду
3. [Овчаренко Юлія](https://github.com/JuliaOvcarenko) - Єдина працівниця
4. [Єрмаченков Пересвет](https://github.com/PeresvietErmachenkov) - Працював над кодом проекту
5. [Ткачук Глєб](https://github.com/Gleb-Tkachuk) - Працівник
6. [Литвиненко Христина](https://example.com) - Не вказала свій GitHub

---

## Використані технології
### Python 
#### Наша основна мова програмування на якій написан увесь бекенд проекту
_нижче приведені фреймворки які були використані при написанні сайту_
1. >Flask - Головний фреймворк для написання будови сайту
2. >telebot - Головний фреймворк який відповідає за роботу боту у [Telegram](https://telegram.org/)  
### HTML5 
#### Мова-конструктор, на якому побудована структура всіх веб-сторінок проекту
### CSS
#### Мова для надання сторінкам стилів і деякого косметичного функціоналу
### JavaScript
#### Мова для створення сайту фронтенду, функціоналу і краси на сайті для користувача

---

## Структура нашої програми
#### Нижче приведена структура нашого проекту 
```bash

Shop Flask:
│   manage.py
│   
├───admin_page
│   │   app.py
│   │   views.py
│   │   __init__.py
│   │   
│   └───templates
│           admin.html
│         
│   
│
├───authorization_page
│   │   app.py
│   │   views.py
│   │   __init__.py
│   │   
│   └───templates
│           login.html
│   
├───basket_page
│   │   app.py
│   │   views.py
│   │   __init__.py
│   │
│   └────templates
│           basket.html
│           basket_send.html
│   
├───bot
│       tele_bot.py
│       __init__.py
│   
├───home_page
│   │   app.py
│   │   models.py
│   │   views.py
│   │   __init__.py
│   │
│   └───templates
│           logined_home.html
│           not_logined_home.html
│   
├───project
│   │   data.db
│   │   login_manager.py
│   │   mail_config.py
│   │   settings.py
│   │   urls.py
│   │   __init__.py
│   │   
│   ├──migrations
│   │       {migrations folder}
│   │     
│   │    
│   │   
│   │
│   └───templates
│           acc_base.html
│           base.html
│   
├───registration_page
│   │   app.py
│   │   views.py
│   │   __init__.py
│   │
│   └───templates
│           registration.html
│
├───shop_page
│   │   app.py
│   │   views.py
│   │   __init__.py
│   │   
│   └───templates
│           shop.html
│   
└───static
    ├───admin_page
    │   ├───css
    │   │       style.css
    │   │
    │   ├───images
    │   │       delete.png
    │   │       pencil.png
    │   │       trash_icon.png
    │   │
    │   └───js
    │           script.js
    │
    ├───authorization_page
    │   └───css
    │           style.css
    ├───basket_page
    │   ├───css
    │   │       style.css
    │   │       style_send.css
    │   │
    │   ├───images
    │   │       trash_icon.png
    │   │
    │   └───js
    │           script.js
    │
    ├───home_page
    │   └───css
    │           logined_style.css
    │           not_logined_style.css
    │
    ├───project
    │   ├───css
    │   │       base_style.css
    │   │
    │   └───js
    │           script.js
    │
    ├───registration_page
    │   └───css
    │           style.css
    │
    └───shop_page
        ├───css
        │       style.css
        │
        ├───images
        │       {put product images here}
        │
        └───js
                script.js
```