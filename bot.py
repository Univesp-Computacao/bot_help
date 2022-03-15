"""
Projeto para o bot help
"""

import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


GIT_HELP = """
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

DOCKER_HELP = '''
Comandos de gerenciamento:
  config      Gerenciar Configurações Docker.
  container   Gerenciar Container.
  image       Gerenciar Imagens.
  network     Gerenciar Redes.
  node        Gerenciar Nós de Swarm.
  plugin      Gerenciar Plugins.
  secret      Gerenciar Docker secrets.
  service     Gerenciar Services.
  swarm       Gerenciar Swarm.
  system      Gerenciar Docker.
  trust       Gerenciar a veracidade das imagens Docker .
  volume      Gerenciar Volumes.

Comandos:
  attach      Anexar fluxos de entrada, saída e erro padrão locais a um contêiner em execução. 
  build       Construir uma imagem através de um Dockerfile.
  commit      Criar uma nova imagem das mudanças de um container.
  cp          Copiar arquivos/pastas entre um container e o sistema de arquivos local.
  create      Criar novo Container.
  diff        Inspecionar mudanças para arquivos ou diretórios no sistema de arquivos do Container.
  events      Pegar eventos do servidor em tempo real.
  exec        Executar um comando em um container ativo.
  export      Exportar o sistema de arquivos de um container como um arquivo do tipo tar.
  history     Mostrar a história de uma imagem.
  images      Lista Imagens.
  import      Importar o conteúdo de um trabalho para criar uma imagem de um sistema de arquivos.
  info        Exibe informação de todo o sistema.
  inspect     Retornar informações de baixo nível sobre objetos do Docker.
  kill        Encerrar um ou mais contêineres em execução.
  load        Carregar uma imagem de um arquivo tipo tar ou STDIN.
  login       Faça login em um registro do Docker.
  logout      Faça logout em um registro do Docker.
  logs        Buscar os logs de um contêiner.
  pause       Pausar todos os processos em um ou mais contêineres.
  port        Listar mapeamentos de portas ou um mapeamento específico para o contêiner.
  ps          Listar containers.
  pull        Puxar uma imagem ou um repositório de um registro.
  push        Enviar uma imagem ou um repositório para um registro.
  rename      Renomear um Container.
  restart     Restart de um ou mais containers.
  rm          Remover um ou mais containers.
  rmi         Remover uma ou mais imagens.
  run         Executar um comando em um novo Container.
  save        Salvar uma ou mais imagens para um arquivo tipo tar (STDOUT por default).
  search      Procurar por imagens no Docker Hub.
  start       Começar um ou mais containers pausados.
  stats       Exibir uma transmissão ao vivo das estatísticas de uso de recursos dos containers.
  stop        Pausa um ou mais containers em execução.
  tag         Cria uma tag TARGET_IMAGE que se refere ao SOURCE_IMAGE.
  top         Exibir os processos em execução de um contêiner.
  unpause     Tirar da pausa todos processos em um ou mais containers.
  update      Atualizar configuração de um ou mais contêineres.
  version     Mostrar as informações da versão do Docker.
  wait        Bloquear até que um ou mais contêineres parem e imprima seus códigos de saída.

Execute 'docker COMMAND --help' para mais informações sobre um comando.
'''

updater = Updater(os.getenv('TOKEN'))

def git_help(update: Update, context: CallbackContext):
    """ Envia a Messagem no Telegram """
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode="Markdown", text=GIT_HELP)

def docker_help(update: Update, context: CallbackContext):
    """ Envia a Messagem no Telegram """
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode="Markdown", text=DOCKER_HELP)   

updater.dispatcher.add_handler(CommandHandler('git_help', git_help))
updater.dispatcher.add_handler(CommandHandler('docker_help', docker_help))

updater.start_polling()
