# Bot de Promoções - Telegram

Bot que formata textos de promoção de afiliados automaticamente.

## Como fazer o deploy no Railway (gratuito)

### 1. Criar conta no GitHub
- Acesse github.com e crie uma conta gratuita

### 2. Criar repositório
- Clique em "New repository"
- Nome: `bot-promocoes`
- Deixe como Public
- Clique em "Create repository"

### 3. Subir os arquivos
- Clique em "uploading an existing file"
- Arraste os 3 arquivos: bot.py, requirements.txt, Procfile
- Clique em "Commit changes"

### 4. Criar conta no Railway
- Acesse railway.app
- Clique em "Login with GitHub"
- Autorize o acesso

### 5. Criar o projeto
- Clique em "New Project"
- Escolha "Deploy from GitHub repo"
- Selecione o repositório bot-promocoes
- Clique em "Deploy Now"

### 6. Pronto!
O bot vai estar online em cerca de 2 minutos.
Abra o Telegram, procure pelo seu bot e mande /start para testar.

## Como usar o bot

Mande qualquer texto de promoção — do jeito que vier:

**Exemplo de entrada:**
Tênis Nike Air 40% off de 300 por 180 cupom PROMO10 link https://...

**Saída formatada:**
Tênis Nike Air
de R$ 300,00
por R$ 180,00 🔥
🎟️Use o cupom: PROMO10
🛒 Pega o link: https://...
