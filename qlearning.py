import numpy as np
import random
import time
import json

agent = None


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.states_actions = {"X": [], "O": []}

    def reset(self):
        self.board = [" "] * 9
        self.states_actions = {"X": [], "O": []}

    def is_winner(self, player):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        return any(
            all(self.board[i] == player for i in combination)
            for combination in winning_combinations
        )

    def print_board(self):

        i = 0
        for j in range(3):
            print("|", end=" ")
            for k in range(3):
                print(self.board[i], end=" ")
                i += 1
            print("|")

    def is_full(self):
        return " " not in self.board

    def get_valid_actions(self):
        return [i for i in range(9) if self.board[i] == " "]

    def play(self, action, player):
        if self.board[action] == " ":
            self.board[action] = player
            return True
        return False


class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.load_q_table()
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def save_q_table(self, caminho="q_table.json"):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(self.q_table, arquivo, ensure_ascii=False, indent=4)

    def load_q_table(self, caminho="q_table.json"):
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                self.q_table = json.load(arquivo)
        except:
            print("impossivel abrir arquivo")
            self.q_table = {}
            time.sleep(10)

    def get_q_value(self, state, action):
        return self.q_table.get(str((tuple(state), action)), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        max_future_q = max(
            [self.get_q_value(next_state, a) for a in self.valid_actions(next_state)],
            default=0.0,
        )
        current_q = self.get_q_value(state, action)
        self.q_table[str((tuple(state), action))] = current_q + self.alpha * (
            reward + self.gamma * max_future_q - current_q
        )
        # print(state)
        # print(next_state)
        # input(self.q_table)

    def choose_action(self, state, valid_actions, rand=True):
        if rand:
            if random.uniform(0, 1) < self.epsilon:
                return random.choice(valid_actions)
        return max(valid_actions, key=lambda a: self.get_q_value(state, a))

    def valid_actions(self, state):

        return [i for i in range(9) if state[i] == " "]

    def update_q_value_result(self, states_actions, result):
        for i in range(len(states_actions)):
            m = self.gamma**i
            current_q = self.q_table.get(states_actions[-i - 1], 0.0)
            if current_q is None:
                current_q = 0
            self.q_table[states_actions[-i - 1]] = current_q + self.alpha * (
                (result - current_q) * self.gamma * m
            )


# Função de treinamento: agente joga contra si mesmo
def train_agent(episodes=100000):
    global agent
    if not agent:
        agent = QLearningAgent(epsilon=0.1)
    game = TicTacToe()

    for e in range(episodes):

        if e % 1000 == 0:
            print(e)
        game.reset()
        state = game.board.copy()
        done = False
        current_player = "X"
        state = [
            1 if i == current_player else " " if i == " " else -1
            for i in game.board.copy()
        ]
        last_state = None
        last_action = None
        last_next_state = None

        while not done:
            valid_actions = game.get_valid_actions()
            action = agent.choose_action(state, valid_actions)
            game.play(action, current_player)

            # Verificar resultado
            if game.is_winner(current_player):
                reward_x = 1 if current_player == "X" else -1
                reward_o = -1 if current_player == "X" else 1
                agent.update_q_value(last_state, last_action, -1, last_next_state)
                done = True
                agent.update_q_value_result(game.states_actions["X"], reward_x)
                agent.update_q_value_result(game.states_actions["O"], reward_o)
            elif game.is_full():
                reward_x = reward_o = -0.1
                done = True
                agent.update_q_value_result(game.states_actions["X"], reward_x)
                agent.update_q_value_result(game.states_actions["O"], reward_o)
            else:
                reward_x = reward_o = 0

            # next_state = game.board.copy()
            next_state = [
                1 if i == current_player else " " if i == " " else -1
                for i in game.board.copy()
            ]

            if current_player == "X":
                if reward_x:
                    agent.update_q_value(state, action, reward_x, next_state)
                game.states_actions[current_player].append(str((tuple(state), action)))
                current_player = "O"
            else:
                if reward_o:
                    agent.update_q_value(state, action, reward_o, next_state)
                game.states_actions[current_player].append(str((tuple(state), action)))
                current_player = "X"
            last_state = state.copy()
            last_next_state = next_state.copy()
            last_action = action

            state = [
                1 if i == current_player else " " if i == " " else -1
                for i in game.board.copy()
            ]
    agent.save_q_table()

    return agent


def human_vs_agent(trained_agent):
    game = TicTacToe()
    game.reset()
    current_player = random.choice(["X", "O"])

    while True:
        print("\nTabuleiro atual:")
        game.print_board()

        if current_player == "X":  # Jogador humano
            action = int(input("Digite sua jogada (0-8): "))
            while action not in game.get_valid_actions():
                action = int(input("Jogada inválida. Digite outra (0-8): "))
        else:  # Agente joga
            state = [
                1 if i == current_player else " " if i == " " else -1
                for i in game.board
            ]
            action = trained_agent.choose_action(
                state, game.get_valid_actions(), rand=False
            )
            print(
                "\n| ",
                f"{trained_agent.get_q_value(state, 0):.2}",
                f"{trained_agent.get_q_value(state, 1):.2}",
                f"{trained_agent.get_q_value(state, 2):.2}",
                " |",
            )
            print(
                "| ",
                f"{trained_agent.get_q_value(state, 3):.2}",
                f"{trained_agent.get_q_value(state, 4):.2}",
                f"{trained_agent.get_q_value(state, 5):.2}",
                " |",
            )
            print(
                "| ",
                f"{trained_agent.get_q_value(state, 6):.2}",
                f"{trained_agent.get_q_value(state, 7):.2}",
                f"{trained_agent.get_q_value(state, 8):.2}",
                " |\n",
            )
            print(f"Agente escolheu a jogada: {action}")

        game.play(action, current_player)

        if game.is_winner(current_player):
            print(f"\n{current_player} venceu!")
            break
        elif game.is_full():
            print("\nEmpate!")
            break

        current_player = "O" if current_player == "X" else "X"

    print("\nTabuleiro final:")
    game.print_board()


# Treinar o agente
while True:
    trained_agent = train_agent()
    print("\n\n", len(trained_agent.q_table), "\n\n")
    time.sleep(5)
    # print(trained_agent.q_table)
    # time.sleep(5)

    # Testando um jogo do agente treinado contra ele mesmo
    game = TicTacToe()
    game.reset()
    state = game.board.copy()
    done = False
    current_player = "X"

    while not done:
        state = [
            1 if i == current_player else " " if i == " " else -1
            for i in game.board.copy()
        ]
        print("\nTabuleiro atual:")
        game.print_board()
        time.sleep(1)
        # input()
        action = trained_agent.choose_action(
            state, game.get_valid_actions(), rand=False
        )
        print(
            "\n\n| ",
            f"{trained_agent.get_q_value(state, 0):.2}",
            f"{trained_agent.get_q_value(state, 1):.2}",
            f"{trained_agent.get_q_value(state, 2):.2}",
            " |",
        )
        print(
            "| ",
            f"{trained_agent.get_q_value(state, 3):.2}",
            f"{trained_agent.get_q_value(state, 4):.2}",
            f"{trained_agent.get_q_value(state, 5):.2}",
            " |",
        )
        print(
            "| ",
            f"{trained_agent.get_q_value(state, 6):.2}",
            f"{trained_agent.get_q_value(state, 7):.2}",
            f"{trained_agent.get_q_value(state, 8):.2}",
            " |",
        )
        print("Action: ", action, "q_tble: ", trained_agent.get_q_value(state, action))
        time.sleep(10)
        game.play(action, current_player)

        if game.is_winner(current_player):
            print(f"\n{current_player} venceu!")
            break
        elif game.is_full():
            print("\nEmpate!")
            break

        current_player = "O" if current_player == "X" else "X"

    print("\nTabuleiro final:", game.print_board())
    time.sleep(5)
    while input("Jogar contra a maquina? (s/n): ").lower() == "s":
        human_vs_agent(trained_agent)
