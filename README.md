# Esse app foi feito para gerenciar suas finanças de forma fácil e prática


## Estrutura do app

finance_app/
│
├── .venv/                    # Ambiente virtual (recomendado)
│
├── .gitignore                # Arquivo para ignorar arquivos/pastas no Git
│
├── requirements.txt          # Lista de dependências do projeto
│
├── README.md                 # Documentação do projeto
│
├── setup.sh                  # Script para configurar o ambiente (opcional)
│
├── src/
│   ├── __init__.py           # Arquivo para tratar a pasta como um módulo
│   ├── main.py               # Script principal do Streamlit
│   ├── pages/                # Subpasta para páginas adicionais do Streamlit
│   │   ├── __init__.py
│   │   ├── dashboard.py      # Página do dashboard financeiro
│   │   ├── reports.py        # Página de relatórios financeiros
│   │   └── settings.py       # Página de configurações
│   ├── data/                 # Subpasta para dados e bases de dados
│   │   ├── __init__.py
│   │   ├── controller.py     # Script de controle para o app
│   │   ├── creator.py        # Script de criação de arquivos
│   │   ├── loader.py         # Script de leitura de arquivos
│   │   └── saver.py          # Script para salvar dados
│   ├── utils/                # Subpasta para utilitários e funções auxiliares
│   │   ├── __init__.py
│   │   ├── calculations.py   # Funções de cálculo financeiro
│   │   └── helpers.py        # Funções auxiliares gerais
│   └── assets/               # Subpasta para arquivos estáticos (imagens, CSS, etc.)
│       ├── css/
│           └── styles.css    # Arquivo de estilo geral
│       └── img/
│           └── logo.png      # Logo do app
│
└── tests/                    # Subpasta para testes
    ├── __init__.py
    └── test_main.py          # Testes para o script principal

