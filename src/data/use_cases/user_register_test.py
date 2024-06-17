from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():
    first_name = 'ola'
    last_name = 'aqui'
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    print(repo.insert_user_attributes)

    assert response['type'] == 'Users'
    assert response['count'] == 1
    assert response['attributes'] == {"first_name": first_name, "last_name": last_name, "age": age}

def test_register_error_name_with_number():
    first_name = 'ola123'
    last_name = 'aqui'
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    print(repo.insert_user_attributes)

    try:
        user_register.register(first_name, last_name, age)
    except Exception as e:
        assert str(e) == "Nome inválido para o cadastro"


def test_register_error_in_long_name():
    first_name = 'olahujhfljksdahljkfhjksafhjsdafhjklhjsad'
    last_name = 'aqui'
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    print(repo.insert_user_attributes)

    try:
        user_register.register(first_name, last_name, age)
    except Exception as e:
        assert str(e) == "Nome muito grande para o cadastro"
