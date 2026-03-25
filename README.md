# 🐾 Pets MVC Architecture

API REST desenvolvida em Python com foco em **arquitetura MVC (Model-View-Controller)**, priorizando organização, separação de responsabilidades e escalabilidade.

---

## 🎯 Objetivo do projeto

O principal objetivo deste projeto foi aplicar na prática o padrão **MVC**, estruturando uma aplicação backend de forma limpa, testável e de fácil manutenção.

---

## 🧠 Arquitetura MVC

O projeto foi dividido em camadas bem definidas:

* **Model** → Responsável pelas entidades e acesso ao banco de dados
* **View** → Responsável pela entrada e saída de dados (HTTP)
* **Controller** → Responsável pela lógica de negócio

Essa separação permite:

* maior organização do código
* facilidade para testes
* melhor escalabilidade
* baixo acoplamento entre camadas

---

## 📂 Estrutura do projeto

```id="y3a2g7"
src/
├── controller/     # Lógica de negócio
├── models/         # Entidades e repositórios (SQLite)
├── view/           # Camada HTTP (request/response)
├── validators/     # Validação de dados
├── main/           # Rotas e inicialização da aplicação
```

---

## 🚀 Tecnologias utilizadas

### Backend

* Python
* Flask
* SQLAlchemy
* SQLite

### Testes

* pytest
* pytest-mock
* mock-alchemy

### Qualidade de código

* pylint
* isort
* pre-commit

### Outras ferramentas

* flask-cors
* Jinja2
* Werkzeug

---

## ⚙️ Funcionalidades

* Criação de pessoas
* Busca de pessoas com seus pets
* Gerenciamento de pets (criação, busca e deleção)
* Validação de dados de entrada
* Testes unitários cobrindo controllers, validators e repositories

---

## ▶️ Como rodar o projeto

```bash id="j8l2mp"
# Clone o repositório
git clone https://github.com/Guip7/Pets-mvc-architecture.git

# Acesse a pasta
cd Pets-mvc-architecture

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
python run.py
```

---

## 🧪 Testes

```bash id="y9c7xz"
pytest
```

---

## ⚠️ Observação sobre versionamento

Durante o desenvolvimento, o projeto possuía um histórico maior de commits locais.
Por um erro ao reconfigurar o repositório Git, parte desse histórico foi perdida antes da publicação.

O código e toda a estrutura da aplicação foram preservados, e o versionamento segue normalmente a partir deste ponto.

---

## 📌 Melhorias futuras

* Autenticação de usuários
* Documentação com Swagger
* Deploy em ambiente cloud
* Paginação de resultados

---

## 👨‍💻 Autor

Guilherme Braga
