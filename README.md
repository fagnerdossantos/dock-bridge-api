# Dock Bridge API

Este projeto é uma API construída em Python utilizando o SDK do Docker para fornecer funcionalidades básicas de gerenciamento de containers. A API permite ao usuário interagir com o Docker de forma programática, oferecendo endpoints para listar imagens, listar containers em execução, iniciar, parar, pausar e despausar containers.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do backend.
- **Docker SDK para Python**: Biblioteca utilizada para controlar o Docker.
- **Flask**: Framework utilizado para criar a API.

## Funcionalidades

Atualmente, a API possui as seguintes funcionalidades:

- **Listar imagens disponíveis** no Docker local.
- **Listar containers em execução**.
- **Iniciar um container** a partir de uma imagem disponível.
- **Parar um container em execução**.
- **Pausar um container**.
- **Despausar um container pausado**.

## Estrutura do Projeto

```
/project
│── core/                # Módulos principais do sistema
│   ├── docker_manager.py  # Classe responsável pelo gerenciamento do Docker
│   ├── docker_container.py  # Representação de um container Docker
│   ├── docker_image.py  # Representação de uma imagem Docker
│   ├── local_client.py  # Cliente local do Docker
│── data/                # Gerenciamento de cache e armazenamento temporário
│   ├── cache.py          # Cache de containers e imagens
│── project/
│   ├── src/
│   │   ├── main.py      # Script principal que inicializa a API Flask
│── requirements.txt      # Dependências do projeto
│── setup.sh             # Script para configurar o ambiente virtual e iniciar a API
│── .gitignore           # Arquivos e diretórios ignorados pelo Git
│── README.md            # Documentação do projeto
```

## Configuração e Execução

Para rodar o projeto, siga os passos abaixo:

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/fagnerdossantos/dock-bridge-api.git
   cd dock_bridge_api
   ```

2. **Execute o script de configuração**:
   ```sh
   ./setup.sh
   ```
   Esse script irá:
   - Criar um ambiente virtual Python
   - Instalar as dependências do projeto
   - Iniciar a API automaticamente

3. **Rodar manualmente (caso necessário)**:
   Caso precise rodar manualmente:
   ```sh
   source backend_venv/bin/activate  # Ativar o ambiente virtual
   python project/src/main.py        # Rodar a API
   ```

## Endpoints da API

A API possui os seguintes endpoints:

| Método | Endpoint              | Descrição |
|--------|------------------------|-------------------------------------------------|
| GET    | `/images`              | Lista todas as imagens disponíveis no Docker   |
| GET    | `/containers`          | Lista todos os containers em execução         |
| POST   | `/container/start`     | Inicia um novo container a partir de uma imagem |
| POST   | `/container/stop`      | Para um container específico                   |
| POST   | `/container/pause`     | Pausa um container em execução                 |
| POST   | `/container/unpause`   | Despausa um container pausado                  |

## Contribuição

Sinta-se à vontade para contribuir com o projeto enviando pull requests ou relatando problemas na aba de Issues.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

