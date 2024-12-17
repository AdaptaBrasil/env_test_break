from hunspell import Hunspell

# Caminho para a DLL e os dicionários
hunspell_path = r"ddl/libhunspell.dll"
dic_path = r"pt_BR/pt_BR.dic"
aff_path = r"pt_BR/pt_BR.aff"

h = Hunspell(hunspell_path, dic_path, aff_path)
print(h.suggest('pyhton'))  # Deve sugerir 'python'