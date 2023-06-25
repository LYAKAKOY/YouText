# youtext
Приложение для генерации статей по видеороликам из YouTube.

## Стек программы
[ChatGPT](https://platform.openai.com/docs/guides/gpt/chat-completions-api), [Whisper](https://github.com/openai/whisper), Django, Celery.

## Как запустить проект
1. Требуется сделать git clone проекта;
```
git clone https://github.com/LYAKAKOY/YouText
```
2. Собрать docker-compose образ;
```
docker-compose build
```
3. Запустить docker-compose;
```
docker-compose up
```
4. Подождать загрузки модели [Whisper](https://github.com/openai/whisper) для распознавания речи и загрузки русского языка для исправления орфографических ошибок;
5. Проект будет доступен по адресу [http://localhost:8000/](http://localhost:8000/)
## Дизайн проекта
### Палитра проекта
![Палитра проекта](https://i.imgur.com/iAV7ysi.png)
[Ссылка на палитру проекта](https://coolors.co/palette/202020-0e0e0e-1a1a1a-ffffff)

### Вид страницы со вставкой ссылки и параметрами
#### [Дизайн страниц на figma](https://www.figma.com/file/W04IY9oglFvC84yTvOwNRP/youtext?type=design&node-id=0%3A1&mode=design&t=aRNBUtdZTr2vRrBl-1)
#### Для компьютеров
![Вид страницы со вставкой ссылки и параметрами для компьютеров](https://i.imgur.com/JhM3Iw2.png)
![Вид страницы со вставкой ссылки и параметрами для компьютеров](https://i.imgur.com/FmF8RkE.png)
#### Для ноутбуков
![Вид страницы со вставкой ссылки и параметрами для ноутбуков](https://i.imgur.com/dCaWbr8.png)
#### Для планшетов
![Вид страницы со вставкой ссылки и параметрами для планшетов](https://i.imgur.com/vCdpMqf.png)
#### Для телефонов
![Вид страницы со вставкой ссылки и параметрами для телефонов](https://i.imgur.com/Ar9Ye01.png)
![Вид страницы со вставкой ссылки и параметрами для телефонов](https://i.imgur.com/Yw5Nk5A.png)
### Вид страницы со сгенерированной статьей
#### Это лишь пример, а не рабочая модель. Рабочая модель представлена после
#### Для компьютеров
![Вид страницы со сгенерированной статьей](https://i.imgur.com/bk0BqSF.png)
#### Для ноутбуков
![Вид страницы со сгенерированной статьей](https://i.imgur.com/n8Cb7wT.png)
#### Для планшетов
![Вид страницы со вставкой ссылки и параметрами для планшетов](https://i.imgur.com/T2bnr4p.png)
#### Для телефонов
![Вид страницы со вставкой ссылки и параметрами для телефонов](https://i.imgur.com/wD8r3D0.png)
### Пример работы программы (рабочая модель)
![Рабочая модель](https://i.imgur.com/FnO4ycO.png)
![Рабочая модель](https://i.imgur.com/mVu0Zp8.png)
![Рабочая модель](https://i.imgur.com/mPGNQDI.png)
![Рабочая модель](https://i.imgur.com/qjRUDeg.png)
![Рабочая модель](https://i.imgur.com/teDdY8A.png)
![Рабочая модель](https://i.imgur.com/kypcBcH.png)



