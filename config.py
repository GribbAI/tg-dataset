import json
import os

def load_chat_data(file_path):
	"""
	Загружает данные чата из указанного JSON файла.
	
	Аргументы:
	file_path -- путь к JSON файлу
	
	Возвращает:
	Объект с данными чата, или None, если произошла ошибка.
	"""
	
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			return json.load(file)
	except (FileNotFoundError, json.JSONDecodeError) as e:
		print(f"Ошибка загрузки файла {file_path}: {e}")
		return None

def extract_chat_info(chat_data):
	"""
	Извлекает информацию о чате из JSON данных.
	
	Аргументы:
	chat_data -- данные чата в формате JSON
	
	Возвращает:
	Кортеж (name, size, messages), где:
	name -- имя чата
	size -- количество сообщений
	messages -- список сообщений
	"""
	
	if not chat_data or 'chat' not in chat_data:
		return None, None, None
	
	chat = chat_data['chat']
	name = chat.get('name')
	size = chat.get('size')
	messages = chat.get('messages', [])
	
	return name, size, messages


def display_messages(messages):
	"""
	Выводит сообщения в читаемом формате.
	
	Аргументы:
	messages -- список сообщений
	"""
	for message in messages:
		user = message.get('user')
		text = message.get('text')
		timestamp = message.get('timestamp')
		print(f"{user} ({timestamp}): {text}")




def process_chat_files(dataset_path):
	"""
	Обрабатывает все JSON файлы в указанной папке.
	
	Аргументы:
	dataset_path -- путь к папке с JSON файлами
	"""
	for filename in os.listdir(dataset_path):
		if filename.endswith('.json'):
			file_path = os.path.join(dataset_path, filename)
			chat_data = load_chat_data(file_path)
			name, size, messages = extract_chat_info(chat_data)
			
			if name and size is not None:
				print(f"Чат: {name}, Количество сообщений: {size}")
				display_messages(messages)
				print("\n")
			else:
				print(f"Не удалось извлечь информацию из файла {filename}.")


# Укажите путь к папке с dataset
dataset_path = 'dataset'
process_chat_files(dataset_path)