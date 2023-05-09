import os

def split_file_by_keyword(file_path, keyword_prefix, start_number, end_number, output_path):
    try:
        with open(file_path, 'r', encoding='UTF-8-SIG') as file:
            content = file.read()
            lines = content.split('\n')

            current_keyword = None
            current_file = None

            for line in lines:
                if line.startswith(keyword_prefix):
                    current_keyword = line.strip()
                    if current_file:
                        current_file.close()
                    current_file_path = os.path.join(output_path, f"{current_keyword}.txt")
                    current_file = open(current_file_path, 'w', encoding='utf-8')
                elif current_file:
                    current_file.write(line + '\n')

            if current_file:
                current_file.close()

        print("Pemisahan kata kunci selesai.")
    except FileNotFoundError:
        print("File tidak ditemukan.")

file_path = r'your_path_file'  # Path file yang ingin dipisahkan
output_path = r'your_path_folder'  # Path folder untuk output file
keyword_prefix = 'your_keyword'  # Awalan kata kunci
start_number = 1  # Nomor awal
end_number = 2 # Nomor akhir

split_file_by_keyword(file_path, keyword_prefix, start_number, end_number, output_path)
