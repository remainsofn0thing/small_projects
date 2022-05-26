from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='en'):
    # file exists or not
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':  # suffix - the extension we want
        print(f'[+ Original file: {Path(file_path).name}')
        print('[+] Processing...')
        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        # with open('text1.txt', 'w') as file:
        # file.write(text)
        # text = text.replace('\n', '')
        # with open('text2.txt', 'w') as file:
        # file.write(text)
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem  # получили имя файла
        my_audio.save(f'{file_name}.mp3')  # сохраняем аудиофайл
        return f'[+]{file_name}.mp3 saved successfully\n'

    else:
        return 'File doesn\'t exists,check the file path pls!'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    print(pdf_to_mp3(file_path="D:\Downloads\Punch, Brothers, Punch!.pdf"))  # add ur path to pdf file


#  print(pdf_to_mp3(file_path="C:/Users/Пользователь/Desktop/some_file.pdf"))

if __name__ == '__main__':
    main()
