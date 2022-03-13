"""
Projeto para o bot help
"""

import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


TODOS_OS_COMANDOS = """
Estes são os comandos Git mais comuns usados em várias situações:

Começando uma área de trabalho: (git help tutorial)
   - clone: Clona um repositório remoto dentro de um diretório local.
   - init: Cria um repositório Git vazio ou reinicializa um existente.

Trabalhando no diretório corrente: (git help everyday)
   - add: Adiciona conteúdo dos arquivos ao index.
   - mv: Move ou renomeia um arquivo, um diretório , ou um symlink.
   - restore: Restaura árvore de arquivos de trabalho (working tree).
   - rm: Remove arquivos da árvore de trabalhos e do index.

Examinando a história e o estado: (git help revisions)
   - bisect: Usa busca binária para achar o commit que introduziu um bug.
   - diff: Mostra mudanças entre commits.
   - grep: Imprime linhas que correspondem a um padrão.
   - log: Mostra o log dos commits.
   - show: Mostra vários tipos de objetos.
   - status: Mostra o status da área de trabalho.

Crescer, marcar e ajustar sua história comum:
   - branch: Lista, cria ou deleta branches.
   - commit: Grava as mudanças para o repositório.
   - merge: Junta duas ou mais histórias de desenvolvimento juntas.
   - rebase: Reaplicar commits em cima de outra base.
   - reset: Reseta a HEAD corrente para um estado específico.
   - switch: Alterna entre branches.
   - tag: Cria, lista, deleta ou verifica a tag de um objeto.

Colaborar: (see also: git help workflows)
   - fetch: Baixar objetos e referências de outro repositório.
   - pull: Busca e integra com outro repositório ou uma branch local.
   - push: Atualiza referências remotas junto com objetos associados.

"""


updater = Updater(`TOKEN`)

def git_help(update: Update, context: CallbackContext):
    """ Envia a Messagem no Telegram """
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode="Markdown", text=TODOS_OS_COMANDOS)


updater.dispatcher.add_handler(CommandHandler('git_help', git_help))

updater.start_polling()
