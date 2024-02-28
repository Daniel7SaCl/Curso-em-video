import asyncio
import websockets
import aioconsole

usuarioID = ""


async def receive_msg(ws):
    async for msg in ws:
        if '|' + usuarioID + '|' not in msg:  # verifica se está recebendo mensagem dele mesmo
            print("<-- : ", msg)


async def handle_console_input(websocket):
    while True:
        message = await aioconsole.ainput("--> : ")
        if message.lower() == "sair":  # Verifica se o usuário digitou "sair"
            print("Fechando conexões e saindo...")
            await websocket.close()
            print("Sempre rumo ao tesouro de Bresa!!")
            return  # Sai da função para encerrar o loop
        if message:
            await websocket.send(f"{usuarioID}|{message}")


async def main():
    uri = "ws://192.168.100.183:2023"
    async with websockets.connect(uri) as websocket:
        print("Já pode enviar mensagens...")
        # Executa as tarefas de receber mensagens e lidar com a entrada do console simultaneamente
        await asyncio.gather(
            receive_msg(websocket),
            handle_console_input(websocket),
        )

usuarioID = input("Informe o Id do usuário: ")

if __name__ == "__main__":
    asyncio.run(main())