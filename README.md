# Dashboard Clima

Um cliente Python para integração com a API OpenWeatherMap, fornecendo uma forma simples e eficiente de obter dados meteorológicos baseados em coordenadas geográficas.

## 📋 Sobre

Este projeto encapsula a lógica de requisição à API OpenWeatherMap com tratamento robusto de erros, incluindo timeouts de conexão, erros HTTP e respostas JSON inválidas.

## 🚀 Funcionalidades

- Integração com a API OpenWeatherMap
- Obtém dados meteorológicos por latitude e longitude
- Tratamento completo de erros (timeout, conexão, HTTP)
- Validação de respostas JSON
- Suporte a variáveis de ambiente

## 📦 Instalação

### Pré-requisitos

- Python 3.7+
- pip

### Passos

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd dashboard-clima
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure a variável de ambiente com sua chave da API OpenWeatherMap:

```bash
export OPENWEATHER_API_KEY="<sua-chave-aqui>"
```

Ou crie um arquivo .env naraiz do projeto:

```
OPENWEATHER_API_KEY=sua-chave-aqui
```

## 🔧 Uso

Exemplo básico:
```python
from api import OpenWeatherAPI
import json

# Inicializar o cliente
api = OpenWeatherAPI(api_key="<sua-chave-api>")

# Obter dados meteorológicos
data = api.get_weather(lat=44.34, lon=10.99)

# Exibir resultado
if data:
    print(json.dumps(data, indent=2, ensure_ascii=False))    
```

## 🔐 Configuração da API Key

1. Acesse OpenWeatherMap
2. Crie uma conta e obtenha sua chave de API
3. Configure a variável de ambiente conforme descrito acima

## 📋 Dependências

- requests (2.32.5): Biblioteca HTTP para Python
- python-dotenv (1.2.1): Carrega variáveis de ambiente de arquivo .env

## ⚖️ Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## 👤 Autor

Pablo Moraes

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## 📝 Notas de Desenvolvimento

- O tipo de retorno da função get_weather() está marcado como Any e pode ser melhorado com tipos mais específicos.
- Consulte os TODOs no código para futuras melhorias.