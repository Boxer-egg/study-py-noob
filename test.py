import subprocess

def test_get_dependencies():
    deps = get_dependencies("pdm")
    print(deps)

test_get_dependencies()
