from Algorithms_and_structures import HashTable, validate_inputs
import os
import struct


class ExternalMemoryDatabase:
    def __init__(self, data_file: str = "storage.db"):
        self.storage = data_file
        self.indexes = HashTable()
        self.current_position = 0
        self.write_buffer = []  # Буфер для накопления записей перед сбросом на диск
        self.buffer_size = 1000  # Максимальное количество записей в буфере
        self._initialize_storage()

    def _initialize_storage(self):
        """Создает файл для базы данных, если его нет."""
        try:
            if os.path.exists(self.storage):
                self.current_position = os.path.getsize(self.storage)
            else:
                with open(self.storage, 'wb'):
                    pass
                self.current_position = 0

        except OSError as e:
            raise RuntimeError(f"Не удалось инициализировать хранилище {self.storage}: {e}") from e

    def _create_compact_record(self, key, value):
        """Создает компактную запись в бинарном формате для эффективного хранения."""
        key_bytes = key.encode('utf-8')
        value_bytes = value.encode('utf-8')
        
        # Компактное кодирование через struct для минимизации размера записи
        record = (struct.pack('>H', len(key_bytes)) +  # 2 байта для длины ключа
                 key_bytes +
                 struct.pack('>H', len(value_bytes)) +  # 2 байта для длины значения
                 value_bytes)
        return record

    def _flush_buffer(self):
        """Записывает накопленные в буфере данные в файл хранилища."""
        if not self.write_buffer:
            return
            
        try:
            # Однократное открытие файла для всех записей в буфере
            with open(self.storage, 'ab') as file:
                for record in self.write_buffer:
                    file.write(record)
            self.write_buffer.clear()
        except OSError as e:
            raise RuntimeError(f"Ошибка записи буфера: {e}") from e
        
    @validate_inputs
    def add(self, key, value):
        try:
            if self.indexes.get(key) is not None:
                return False

            position = self.current_position
            
            # Создание компактной записи в бинарном формате
            record = self._create_compact_record(key, value)
            record_size = len(record)
            
            # Добавление записи в буфер для последующей пакетной записи
            self.write_buffer.append(record)
            self.indexes.put(key, position)
            self.current_position += record_size
            
            # Сброс буфера при достижении максимального размера
            if len(self.write_buffer) >= self.buffer_size:
                self._flush_buffer()
                
            return True
        
        except OSError as e:
            raise RuntimeError(f"Ошибка записи: {e}") from e

    def delete(self, key):
        if self.indexes.get(key) is None:
            return False
        
        self.indexes.delete(key)
        return True

    @validate_inputs
    def update(self, key, value):
        if self.indexes.get(key) is None:
            return False
        
        # Оптимизация: старая запись не удаляется физически, добавляется новая
        # Старая запись остается в файле, но индекс обновляется на новую позицию
        return self.add(key, value)

    def show(self, key):
        position = self.indexes.get(key)
        if position is None:
            return False
        try:
            with open(self.storage, 'rb') as file:
                file.seek(position)
            
                # Чтение компактной записи из бинарного формата
                key_size_bytes = file.read(2)
                if not key_size_bytes:
                    return False
                key_size = struct.unpack('>H', key_size_bytes)[0]
                
                key_data = file.read(key_size).decode('utf-8')
                
                value_size_bytes = file.read(2)
                if not value_size_bytes:
                    return False
                value_size = struct.unpack('>H', value_size_bytes)[0]
                
                value_data = file.read(value_size).decode('utf-8')

                print(f"{key_data} {value_data}")
                return True
    
        except OSError as e:
            raise RuntimeError(f"Ошибка чтения: {e}") from e
    
    def cleanup(self):
        """Очищает файлы базы данных"""
        try:
            # Сброс буфера перед удалением файла хранилища
            self._flush_buffer()
            if os.path.exists(self.storage):
                os.remove(self.storage)
        except OSError:
            pass

def main():
    database = ExternalMemoryDatabase()
    
    try:
        total_commands = int(input().strip())
        if total_commands <= 0:
            raise ValueError("Количество команд должно быть положительным")
        
        for _ in range(total_commands):
            command = input().strip().split()

            if not command:
                continue
        
            cmd_type = command[0]

            if cmd_type == "ADD" and len(command) == 3:
                if not database.add(command[1], command[2]):
                    print("ERROR")

            elif cmd_type == "DELETE" and len(command) == 2:
                if not database.delete(command[1]):
                    print("ERROR")
            
            elif cmd_type == "UPDATE" and len(command) == 3:
                if not database.update(command[1], command[2]):
                    print("ERROR")
            
            elif cmd_type == "PRINT" and len(command) == 2:
                if not database.show(command[1]):
                    print("ERROR")

            else:
                print("ERROR")
    
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        # Гарантированный сброс буфера перед завершением программы
        database.cleanup()

    
if __name__ == "__main__":
    main()
