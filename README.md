# Hexagonal Architecture - Estudo em Python

## Objetivo
Este projeto tem como finalidade o estudo prático da arquitetura hexagonal (Ports & Adapters) utilizando Python. Ele foi desenvolvido para ajudar a entender, de forma interativa, conceitos fundamentais de design de software como Polimorfismo e o Princípio da Inversão de Dependência (DIP).

## Descrição
O sistema simula um menu de terminal, onde é possível navegar entre exemplos de polimorfismo e DIP, utilizando diferentes "carros" que implementam uma interface comum. O projeto está organizado em camadas, separando domínio, aplicação e interfaces, seguindo os princípios da arquitetura hexagonal.

### Conceitos Abordados
- **Polimorfismo:** Demonstra como diferentes classes (Ferrari, Fusca, Civic) implementam a mesma interface abstrata `Carro`, permitindo que sejam utilizadas de forma intercambiável.
- **DIP (Dependency Inversion Principle):** A lógica de corrida depende de abstrações (interfaces), não de implementações concretas, facilitando testes, manutenção e extensibilidade.
- **Arquitetura Hexagonal:** O projeto separa claramente o núcleo de domínio das interfaces externas (como terminal), promovendo baixo acoplamento e alta coesão.

## Estrutura do Projeto
- `src/hexagonal_architecture/core/`: Núcleo de domínio (modelos, regras de negócio, interfaces)
- `src/hexagonal_architecture/app/`: Camada de aplicação (menus, fluxos de interação)
- `src/hexagonal_architecture/utils/`: Utilitários e interfaces de saída

## Pré-requisitos
- Python 3.10 ou superior
- poetry (opcional, para gerenciar dependências)

## Instalação
1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd hexagonal-architecture
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   # ou, se preferir poetry
   poetry install
   ```

## Como Executar
No terminal, execute:
```bash
python -m src.hexagonal_architecture.main
```

## Observações
- O projeto utiliza a biblioteca `curses` para interface de terminal. No Windows, pode ser necessário instalar suporte adicional.
- O menu permite navegar entre exemplos de polimorfismo e DIP, escolhendo diferentes carros e observando o comportamento de cada um.

## Licença
Projeto para fins de estudo.

