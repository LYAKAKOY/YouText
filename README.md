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
[Дизайн страниц на figma](https://www.figma.com/file/W04IY9oglFvC84yTvOwNRP/youtext?type=design&node-id=0%3A1&mode=design&t=aRNBUtdZTr2vRrBl-1)
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

