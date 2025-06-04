# 🧠 Sistema de Cadastro Automatizado com Python

Este projeto automatiza o processo de cadastro de alunos em um site, utilizando as bibliotecas **PyAutoGUI** e **Pandas**. Ele lê os dados de um arquivo `.csv` e os insere automaticamente em um sistema web.

---

## 📽 Demonstração do Funcionamento
O script executa as seguintes etapas:

1. Abre o navegador Google Chrome.
2. Acessa o site [cadastrodalunos.netlify.app](https://cadastrodalunos.netlify.app/).
3. Realiza login com e-mail e senha fictícios.
4. Lê os dados da planilha `alunos_30.csv`.
5. Preenche automaticamente o formulário com os dados dos alunos.
6. Repete o processo para todos os alunos da lista.
   
---

## 🚀 Tecnologias Utilizadas
- [Python 3.x](https://www.python.org/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Pandas](https://pandas.pydata.org/)

---

## ✅ Pré-requisitos

Antes de rodar o script, instale os pacotes necessários no cmd:
- pip install pandas pyautogui

Verifique se o Python está instalado:
- python --version

---

## 🛠 Observações
- As posições dos cliques (x, y) podem variar dependendo da resolução da tela, pode ser ajustado com o pyautogui.position().
- O tempo de espera entre as ações pode ser ajustado com time.sleep() se necessário, conforme o desempenho do site e da máquina.

---

## ▶️ Como Executar
Clone o repositório:
- git clone https://github.com/seu-usuario/Python-power-up.git
- cd Python-power-up
- Verifique se o arquivo alunos_30.csv está na pasta src/.

Execute o script:
- python sistema.py
  
⚠️ Importante: Durante a execução do script, não mexa no mouse ou teclado, pois o PyAutoGUI simula interações reais e qualquer ação pode interromper o processo.

