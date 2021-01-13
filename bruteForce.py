from tqdm import tqdm

import zipfile
import sys


wordlist = sys.argv[2]

zip_file = sys.argv[1]

zip_file = zipfile.ZipFile(zip_file)

n_words = len(list(open(wordlist, "rb")))

print("Senhas:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Senha encontrada:", word.decode().strip())
            exit(0)
print("[!] Não encontrado")