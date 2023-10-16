from main import task3


def test_task3():
    assert task3() == 'Ревоция!'
    assert task3(inp='Тефываолджст') == 'Тест'
