import os
import glob
from auchan_file_process.settings import Settings
from typing import List

setting = Settings()


def process_file(file_path: str) -> List:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    result = []
    for line in lines:
        numbers = line.split(',')
        for number in numbers:
            if '-' in number:
                start, end = map(int, number.split('-'))
                result.extend(range(start, end + 1))
            else:
                result.append(int(number.replace('"', '')))
    return result


def save_files(file_name: str, proc_data: List[List[int]], dir_path: str) -> None:
    prefix = file_name.split('_')[-1].replace('.txt', '')
    for _, data in enumerate(proc_data):
        file_name = f'TEST_AUCHAN_success_{prefix}.txt'
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as file:
            for number in data:
                file.write(f'{number}\n')


def process_files(dir_paths: List[str]) -> None:
    result = []
    for patch in dir_paths:
        patch_and_mask = os.path.join(patch + f'/{setting.file_name_mask}')
        file_paths = glob.glob(patch_and_mask, recursive=True)
        for file_path in file_paths:
            proc_data = process_file(file_path)
            result.append(proc_data)
            file_name = os.path.basename(file_path)
            save_files(file_name, result, setting.output_dir)
            result.clear()
