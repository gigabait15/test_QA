from dotenv import load_dotenv
from github import Github
from github import Auth
import unittest
import os


load_dotenv()


class GitHubAPI(unittest.TestCase):

    def setUp(self):
        # подключение к API github и авторизация через токен
        auth = Auth.Token(os.getenv('TOKEN'))
        self.g = Github(auth=auth)

    def test_git_create_repo(self):
        # тест на создание репозитория
        g = self.g
        user = g.get_user()
        user.create_repo('test')
        print(user.get_repo('test'))

    def test_git_get_repo(self):
        # тест на проверку созданного репозитория
        g = self.g
        user = g.get_user()
        for pero in user.get_repos():
            if pero.name == 'test':
                print(pero.name)

    def test_git_del_repo(self):
        # тест на удаление репозитория
        g = self.g
        user = g.get_user()
        for pero in user.get_repos():
            if pero.name == 'test':
                user.get_repo(pero.name).delete()
                print(pero.name)

    def tearDown(self):
        # закрытие подключения к API github
        self.g.close()


if __name__ == "__main__":
    unittest.main()
