import numpy as np
import random
import time
import json

agent = None


class TicTacToe_4x4:
    def __init__(self):
        self.lado = 4
        self.board = [" "] * self.lado * self.lado
        self.states_actions = {"X": [], "O": []}

    def reset(self):
        self.board = [" "] * self.lado * self.lado
        self.states_actions = {"X": [], "O": []}

    def is_winner(self, player):
        winning_combinations = [
            (0, 1, 2, 3),
            (0, -1, -2, -3),
            (0, self.lado, self.lado * 2, self.lado * 3),
            (0, -self.lado, -self.lado * 2, -self.lado * 3),
            (0, -(self.lado - 1), -(self.lado - 1) * 2, -(self.lado - 1) * 3),
            (0, (self.lado - 1), (self.lado - 1) * 2, (self.lado - 1) * 3),
            (0, (self.lado + 1), (self.lado + 1) * 2, (self.lado + 1) * 3),
            (0, -(self.lado + 1), -(self.lado + 1) * 2, -(self.lado + 1) * 3),
        ]

        # diagonais descendo
        for coluna in range(0, 1):
            for linha in range(0, 1):
                i = coluna + self.lado * linha
                try:
                    comb = winning_combinations[6]
                    winner = []
                    for sum in comb:
                        if i + sum >= self.lado * self.lado or i + sum < 0:
                            winner.append(False)
                        winner.append(self.board[i + sum] == player)
                        if not all(winner):
                            break
                    if all(winner):
                        return True
                except:
                    pass

        # diagonais subindo
        for coluna in range(0, 1):
            for linha in range(4, 5):
                i = coluna + self.lado * linha
                try:
                    comb = winning_combinations[4]
                    winner = []
                    for sum in comb:
                        if i + sum >= self.lado * self.lado or i + sum < 0:
                            winner.append(False)
                        winner.append(self.board[i + sum] == player)
                        if not all(winner):
                            break
                    if all(winner):
                        return True
                except:
                    pass

        # horizontais pra frente
        for coluna in range(0, 1):
            for linha in range(0, self.lado):
                i = coluna + self.lado * linha
                try:
                    comb = winning_combinations[0]
                    winner = []
                    for sum in comb:
                        if i + sum > self.lado * self.lado or i + sum < 0:
                            winner.append(False)
                        winner.append(self.board[i + sum] == player)
                        if not all(winner):
                            break
                    if all(winner):
                        return True
                except:
                    pass

        # verticais para baixo
        for coluna in range(0, self.lado):
            for linha in range(0, 1):
                i = coluna + self.lado * linha
                try:
                    comb = winning_combinations[2]
                    winner = []
                    for sum in comb:
                        if i + sum > self.lado * self.lado or i + sum < 0:
                            winner.append(False)
                        winner.append(self.board[i + sum] == player)
                        if not all(winner):
                            break
                    if all(winner):
                        return True
                except:
                    pass

        return False

    def print_board(self):

        i = 0
        for j in range(self.lado):
            print("|", end=" ")
            for k in range(self.lado):
                print(self.board[i], end=" ")
                i += 1
            print("|")

    def is_full(self):
        return " " not in self.board

    def get_valid_actions(self):
        return [i for i in range(self.lado * self.lado) if self.board[i] == " "]

    def play(self, action, player):
        if self.board[action] == " ":
            self.board[action] = player
            return True
        return False

    def get_state(self, current_player):
        return [
            1 if i == current_player else " " if i == " " else -1
            for i in self.board.copy()
        ]


class TicTacToe_8x8:
    def __init__(self):
        self.board = [" "] * 64
        self.states_actions = {"X": [], "O": []}

    def reset(self):
        self.board = [" "] * 64
        self.states_actions = {"X": [], "O": []}

    def is_winner(self, player):
        winning_combinations = [
            (0, 1, 2, 3),
            (0, -1, -2, -3),
            (0, 8, 16, 24),
            (0, -8, -16, -24),
            (0, -7, -14, -21),
            (0, 7, 14, 21),
            (0, 9, 18, 27),
            (0, -9, -18, -27),
        ]

        # for i in range(64):

        # diagonais descendo
        for coluna in range(0, 5):
            for linha in range(0, 5):
                i = coluna + self.lado * linha
                try:
                    comb = winning_combinations[6]
                    winner = []
                    for sum in comb:
                        if i + sum > 63 or i + sum < 0:
                            winner.append(False)
                        winner.append(self.board[i + sum] == player)
                        if not all(winner):
                            break
                    if all(winner):
                        return True
                except:
                    pass
        # diagonais subindo
        for coluna in range(0, 5):
            for linha in range(3, 8):
                i = coluna + self.lado * linha
                try:
                    comb = winning_combinations[4]
                    winner = []
                    for sum in comb:
                        if i + sum > 63 or i + sum < 0:
                            winner.append(False)
                        winner.append(self.board[i + sum] == player)
                        if not all(winner):
                            break
                    if all(winner):
                        return True
                except:
                    pass

        # horizontais pra frente
        for coluna in range(0, 5):
            for linha in range(0, 8):
                i = coluna + self.lado * linha
                try:
                    comb = winning_combinations[2]
                    winner = []
                    for sum in comb:
                        if i + sum > 63 or i + sum < 0:
                            winner.append(False)
                        winner.append(self.board[i + sum] == player)
                        if not all(winner):
                            break
                    if all(winner):
                        return True
                except:
                    pass

        # verticais para baixo
        for coluna in range(0, 8):
            for linha in range(0, 5):
                i = coluna + self.lado * linha
                try:
                    comb = winning_combinations[0]
                    winner = []
                    for sum in comb:
                        if i + sum > 63 or i + sum < 0:
                            winner.append(False)
                        winner.append(self.board[i + sum] == player)
                        if not all(winner):
                            break
                    if all(winner):
                        return True
                except:
                    pass

        """
        for coluna in range(3, 5):
            for linha in range(3, 5):
                i = coluna * 8 + linha
                try:
                    for comb in winning_combinations:
                        winner = []
                        for sum in comb:
                            if i + sum > 63 or i + sum < 0:
                                winner.append(False)
                            winner.append(self.board[i + sum] == player)
                            if not all(winner):
                                break
                        if all(winner):
                            return True
                except:
                    pass
        """
        return False

    def print_board(self):

        i = 0
        for j in range(8):
            print("|", end=" ")
            for k in range(8):
                print(self.board[i], end=" ")
                i += 1
            print("|")

    def is_full(self):
        return " " not in self.board

    def get_valid_actions(self):
        return [i for i in range(64) if self.board[i] == " "]

    def play(self, action, player):
        if self.board[action] == " ":
            self.board[action] = player
            return True
        return False

    def get_state(self, current_player):
        return [
            1 if i == current_player else " " if i == " " else -1
            for i in self.board.copy()
        ]


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

    def get_state(self, current_player):
        return [
            1 if i == current_player else " " if i == " " else -1
            for i in self.board.copy()
        ]


class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.load_q_table()
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def save_q_table(self, caminho="q_table_4x4.json"):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(self.q_table, arquivo, ensure_ascii=False, indent=4)

    def load_q_table(self, caminho="q_table_4x4.json"):
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
def train_agent(episodes=1000000):
    global agent
    if not agent:
        agent = QLearningAgent(epsilon=0.1)
    game = TicTacToe_4x4()

    for e in range(episodes):

        if e % 100000 == 0:
            print(e)
        game.reset()
        done = False
        current_player = "X"

        state = game.get_state(current_player=current_player)

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
            next_state = game.get_state(current_player)

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

            state = game.get_state(current_player)
        if e % 10000 == 0:
            game.print_board()
    agent.save_q_table()

    return agent


def human_vs_agent(trained_agent=QLearningAgent()):
    game = TicTacToe_4x4()
    game.reset()
    current_player = random.choice(["X", "O"])

    while True:
        print("\nTabuleiro atual:")
        game.print_board()

        if current_player == "X":  # Jogador humano
            action = int(input("Digite sua jogada (0-%i): " % game.lado))
            while action not in game.get_valid_actions():
                action = int(
                    input("Jogada inválida. Digite outra (0-%i): " % game.lado)
                )
        else:  # Agente joga
            state = [
                1 if i == current_player else " " if i == " " else -1
                for i in game.board
            ]
            action = trained_agent.choose_action(
                state, game.get_valid_actions(), rand=False
            )
            for j in range(game.lado):
                print("| ", end="")
                for i in range(game.lado):
                    print(
                        f"{trained_agent.get_q_value(state, j*game.lado + i):.2}",
                        end=" ",
                    )
                print(" |")
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


def main():
    # Treinar o agente
    while True:
        trained_agent = train_agent()
        print("\n\n", len(trained_agent.q_table), "\n\n")
        time.sleep(5)
        # print(trained_agent.q_table)
        # time.sleep(5)

        # Testando um jogo do agente treinado contra ele mesmo
        game = TicTacToe_4x4()
        game.reset()
        state = game.board.copy()
        done = False
        current_player = "X"

        while not done:
            state = game.get_state(current_player)
            print("\nTabuleiro atual:")
            game.print_board()
            time.sleep(1)
            # input()
            action = trained_agent.choose_action(
                state, game.get_valid_actions(), rand=False
            )
            for j in range(game.lado):
                print("| ", end="")
                for i in range(game.lado):
                    print(
                        f"{trained_agent.get_q_value(state, j*game.lado + i):.2}",
                        end=" ",
                    )
                print(" |")
            print(
                "Action: ", action, "q_tble: ", trained_agent.get_q_value(state, action)
            )
            time.sleep(1)
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
        # while input("Jogar contra a maquina? (s/n): ").lower() == "s":
        #    human_vs_agent(trained_agent)


if __name__ == "__main__":
    main()
