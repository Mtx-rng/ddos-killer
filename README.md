 **ddos-killer**:

---

# DDos Killer Turbo

![ascii-art](https://raw.githubusercontent.com/Mtx-rng/ddos-killer/main/arte-ascii.png)

## ⚠️ Aviso Legal

> Este script é fornecido **apenas para fins educacionais e testes autorizados em ambientes controlados**.  
> O uso para atacar sistemas de terceiros sem permissão explícita é ilegal e pode resultar em sanções criminais e civis.  
> Use sempre de acordo com as leis locais e obtenha autorização prévia do proprietário do sistema alvo.  
> O desenvolvedor não se responsabiliza por qualquer uso indevido.

---

## 📝 Descrição

O **DDos Killer Turbo** é um script Python para simular ataques DDoS (Distributed Denial of Service) em servidores web, com interface interativa e recursos avançados.  
Ideal para **testes de resiliência**, demonstrações educacionais e aprendizado sobre segurança de redes.

---

## 🚀 Funcionalidades

- 🎯 Escolha do IP e porta do alvo
- ⚡ Ajuste de "turbo" (requisições por thread)
- 🔥 Definição do número de threads
- ⏱ Controle de tempo de ataque
- 🤫 Modo silencioso (quiet mode)
- 🌐 Suporte a protocolos **TCP** e **UDP**
- 🌀 Animação durante o ataque
- 📊 Relatório de pacotes enviados
- 🔄 Randomização de User-Agent nos pacotes
- 🛑 Parada manual do ataque

---

## 🛠 Requisitos

- Python 3.x
- Sistema operacional compatível (Windows, Linux, macOS)

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/Mtx-rng/ddos-killer.git
cd ddos-killer
```

---

## ▶️ Como usar

Execute o script em ambiente de **teste** com permissão:

```bash
python ddos-killer.py
```

Siga o menu interativo para configurar o ataque:

```
--- DDos Killer Turbo Menu ---
1. Set target IP (current: )
2. Set target port (current: 80)
3. Set turbo (requests per thread) (current: 135)
4. Set number of threads (current: 10)
5. Set attack duration (seconds) (current: 10)
6. Toggle quiet mode (current: OFF)
7. Set protocol (TCP/UDP) (current: TCP)
8. Start attack
9. Stop attack
10. Exit
```

---

## ⚠️ Atenção

- **Só execute em ambientes controlados e com autorização!**
- O uso inadequado pode ser crime.

---

## 📚 Aprenda mais

- [O que é DDoS? (Cloudflare)](https://www.cloudflare.com/pt-br/learning/ddos/what-is-a-ddos-attack/)
- [Segurança de redes com Python](https://docs.python.org/3/library/socket.html)

---

## 👨‍💻 Autor

[Mtx-rng](https://github.com/Mtx-rng)