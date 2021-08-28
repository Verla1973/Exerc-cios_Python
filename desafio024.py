cidade = str(input('Em qual cidade você nasceu? ')).strip()
print(f'Sua cidade possue Santo no primeiro nome? ', (cidade[:5]).upper() == "SANTO")
