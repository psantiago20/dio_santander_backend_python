import sys
import subprocess


def main():
    if len(sys.argv) < 2:
        print("Uso: python run.py [comando]")
        print("Comandos disponíveis:")
        print("  create-migration <mensagem>   -> Criar nova migration")
        print("  run-migrations                -> Aplicar migrations (upgrade head)")
        print("  downgrade <versão>            -> Reverter migration")
        print("  runserver                     -> Rodar servidor FastAPI (uvicorn)")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "create-migration":
        if len(sys.argv) < 3:
            print("Erro: informe uma mensagem para a migration.")
            sys.exit(1)
        message = sys.argv[2]
        subprocess.run(["alembic", "revision", "--autogenerate", "-m", message])

    elif cmd == "run-migrations":
        subprocess.run(["alembic", "upgrade", "head"])

    elif cmd == "downgrade":
        if len(sys.argv) < 3:
            print("Erro: informe a versão para fazer downgrade.")
            sys.exit(1)
        version = sys.argv[2]
        subprocess.run(["alembic", "downgrade", version])

    elif cmd == "runserver":
        subprocess.run([
            "uvicorn",
            "workout_api.main:app",
            "--reload",
            "--host", "0.0.0.0",
            "--port", "8000"
        ])

    else:
        print(f"Comando desconhecido: {cmd}")


if __name__ == "__main__":
    main()
