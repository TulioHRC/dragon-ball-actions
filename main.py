from gameplay.goku import Goku
from gameplay.game import Game

def main():
    # Cria o jogador e o inimigo
    player = Goku(power_level=5000, x=0, y=0)
    game = Game(
        player=player,
        enemy_x=3,
        enemy_y=2,
        enemy_power=7000
    )

    print("=== Dragon Ball Game ===")
    print("Comandos:")
    print("  w <n> -> mover para cima")
    print("  s <n> -> mover para baixo")
    print("  d <n> -> mover para direita")
    print("  a <n> -> mover para esquerda")
    print("  battle -> iniciar batalha")
    print("  quit -> sair")
    print()

    while game.get_status():
        print(f"\nSua posição: ({player.get_x()}, {player.get_y()})")
        command = input("> ").strip().lower()

        if command == "quit":
            print("Jogo encerrado.")
            break

        elif command == "battle":
            game.battle()

            if not game.get_status():
                print("Você foi derrotado!")
                break

        else:
            parts = command.split()

            if len(parts) != 2:
                print("Comando inválido.")
                continue

            direction, spaces = parts

            try:
                spaces = int(spaces)
            except ValueError:
                print("Número de espaços inválido.")
                continue

            if direction == "w":
                player.move_vertical(spaces)

            elif direction == "s":
                player.move_vertical(-spaces)

            elif direction == "d":
                player.move_horizontal(spaces)

            elif direction == "a":
                player.move_horizontal(-spaces)

            else:
                print("Direção inválida.")
                continue

            print(
                f"Nova posição: ({player.get_x()}, {player.get_y()})"
            )

    print("Fim de jogo.")


if __name__ == "__main__":
    main()