1. Installing and crating a Project

   - django-admin startproject mysite

     - create a new python project

   - conda create --name mysite python=3.6

     - indicates a conda project from the previews command

   - conda activate mysite
   - pip install django
   - python manage.py runserver

     - Testa para ver se o servidor está funcioanando

   - python manage.py startapp polls

     - Create the modules where we'll work. As views, models and migrations

   - python manage.py migrate

     - Cria as primeiras configurações de migração da db.

   - python manage.py makemigrations polls

     - após a criaçao dos meus models e configurações eu atualizo meu ficheiro de migração

   - python manage.py sqlmigrate polls 0001

     - atualizo a bd

   - python manage.py migrate
     - corro novamente o comando de migraçao para adequar às config do comando anterior e atualizar

2. python manage.py shell

   - abrimos a shell do python para utilizar a api interativa

   * from polls.models import Choice, Question

     - importamos os nossos modelos, que por enquanto ainda estão vazios, nao criamos nenhuma linha na tabela
       podemos ver isso com Question.objects.all() -> isso faz um "get all" na tabela

   * from django.utils import timezone

   * q = Question(question_text="What's new?", pub_date=timezone.now())

     - Criamos um objeto "Question" (que segue a nossa tabela do modelo) e preenchemos as colunas "questio text" e "pub_date".

   * q.save()

     - salvamos o nosso objeto

   * q.id / q.question_text / q.pub_date

     - Agora podemos aceder os elementos do objeto

   * q.question_text = "What's up?" 6.1 -> q.save()

     - Podemos altarar os seus atributos.

   * Question.objects.filter(id=1) / Question.objects.filter(question_text\_\_startswith='What')

     - voce pode filtrar o objeto e ter o retorno que escolher

   * Question.objects.get(pk=1)

     - Podemos buscar um objeto baseado em um atributo tb utilizando o "get".

     obs: o "get" só retorna um elemento que se encaixa, se mais de um elemento se enquadrar ele nao retorna. Já o filter nos traz um array de todos os elementos que se enquadrem na busca

   * q = Question.objects.get(pk=1)
     q.choice_set.create(choice_text='Not much', votes=0)
     q.choice_set.create(choice_text='The sky', votes=0)
     c = q.choice_set.create(choice_text='Just hacking again', votes=0)

     - com isso nós pegamos um objeto (Question) e atribuímos 3 "Choices". Lembrando que o 'Objeto Choice' possui uma FKey de 'Question'.

   * q.choice_set.all() / q.choice_set.count() / c.delete()
     - Traz o resultado, a contagem e deleta

3. Django Admin (gere nosso app por interface)

   - python manage.py createsuperuser
     username/email/pass

     - Cria um usuário para associar a interface de admin do python

   - python manage.py runserver

     - Corre o servidor

   - inside: pool/admin.py
     from .models import Question
     admin.site.register(Question)

     - Isso insere dentro do diretorio admin os modelos e resitra, assim, conseguimos modificá-los pela interface

4. Django app basics

   - Add views (quantas forem necessárias)
   - acrescenta as urls em "urls.py"
   - cria "templates/polls" dentro de "polls" para salvar os nossos templates das views. para separar html de python.
