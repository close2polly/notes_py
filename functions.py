import json
from datetime import date

def print_all_notes():
    with open('notes.json') as file:
        notes = json.load(file)
        print()
        print('Заметки:')
        for noteId in notes['order']:
            note = notes['notes'][noteId]
            print()
            print(f'id: {noteId}')
            print(f'Заголовок: {note['title']}')
            print(f'Описание: {note['description']}')
            print(f'Дата: {note['date']}')
        print()
        print('-- Вывод завершен --')

def print_one_note():
    with open('notes.json') as file:
        notes = json.load(file)
        print()
        print('Доступные заметки')
        print(', '.join(map(lambda x: f'{x} ({notes['notes'][x]['title']})', notes['order'])))
        print()
        print('Введите id:')
        id = input().strip()
        if id not in notes['order']: 
            print('Такого id не существует')
        else:
            note = notes['notes'][id]
            print()
            print('Заметка:')
            print(f'id: {id}')
            print(f'Заголовок: {note['title']}')
            print(f'Описание: {note['description']}')
            print(f'Дата: {note['date']}')
            print()
            print('-- Вывод завершен --')

def delete_note():
    with open('notes.json') as file:
        notes = json.load(file)
        file.close()
        print()
        print('Доступные заметки')
        print(', '.join(map(lambda x: f'{x} ({notes['notes'][x]['title']})', notes['order'])))
        print()
        print('Введите id:')
        id = input().strip()
        if id not in notes['order']: 
            print('Такого id не существует')
        else:
            del notes['notes'][id]
            notes['order'] = list(filter(lambda x: x != id, notes['order']))
            print(notes)
            with open('notes.json', 'w', encoding='utf-8') as fileW:
                fileW.writelines(json.dumps(notes, sort_keys=True, indent=4))
            print()
            print('-- Заметка удалена --')

def add_note():
    with open('notes.json') as file:
        notes = json.load(file)
        file.close()
        print()
        print('Введите заголовок:')
        title = input().strip()
        print('Введите тело:')
        description = input().strip()
        id = int(notes['order'][len(notes['order']) - 1]) + 1
        notes['notes'][str(id)] = { "title": title, "description": description, "date": date.today().strftime("%Y-%m-%d") }
        notes['order'].append(str(id))
        with open('notes.json', 'w', encoding='utf-8') as fileW:
            fileW.writelines(json.dumps(notes, sort_keys=True, indent=4))
        print()
        print('-- Заметка добавлена --')


def edit_note():
    with open('notes.json') as file:
        notes = json.load(file)
        file.close()
        print('Доступные заметки')
        print(', '.join(map(lambda x: f'{x} ({notes['notes'][x]['title']})', notes['order'])))
        print()
        print('Введите id:')
        id = input().strip()
        if id not in notes['order']: 
            print('Такого id не существует')
        else:
            print()
            print('Введите заголовок:')
            title = input().strip()
            print('Введите тело:')
            description = input().strip()
            notes['notes'][str(id)] = { "title": title, "description": description, "date": date.today().strftime("%Y-%m-%d") }
            with open('notes.json', 'w', encoding='utf-8') as fileW:
                fileW.writelines(json.dumps(notes, sort_keys=True, indent=4))
            print()
            print('-- Заметка изменена --')


