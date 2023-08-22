import subprocess

def get_installed_packages():
    result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
    lines = result.stdout.splitlines()[2:]  # Skip the header lines
    packages = [line.split()[0] for line in lines]
    return packages

def get_dependencies(package_name):
    result = subprocess.run(['pip', 'show', package_name], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if line.startswith("Requires:"):
            return [dep.strip() for dep in line.replace("Requires:", "").split(",")]
    return []

def main():
    target_packages = [
        # Your 50 packages here
        "attrs", "blinker", "CacheControl", "cattrs", "certifi", "charset-normalizer", 
        "distlib", "docstring-to-markdown", "filelock", "findpython", "greenlet", "idna", 
        "installer", "jedi", "jedi-language-server", "lsprotocol", "markdown-it-py", 
        "mdurl", "msgpack", "optionaldict", "packaging", "parso", "pdm", "Pillow", "pip", 
        "platformdirs", "pydantic", "pygls", "Pygments", "pynvim", "pyproject_hooks", 
        "python-dateutil", "python-dotenv", "ranger-fm", "requests", "requests-toolbelt", 
        "resolvelib", "rich", "setuptools", "shellingham", "six", "tomlkit", "typeguard", 
        "typing_extensions", "unearth", "urllib3", "virtualenv", "wechatpy", "wheel", 
        "xmltodict"
        # ... (list all 50 packages)
    ]
    dependency_map = {pkg: [] for pkg in target_packages}

    for package in target_packages:
        dependencies = get_dependencies(package)
        for dep in dependencies:
            if dep in target_packages:
                dependency_map[dep].append(package)

    for pkg, dependent_packages in dependency_map.items():
        if dependent_packages:
            print(f"{pkg} 依赖 for {len(dependent_packages)} 库: {', '.join(dependent_packages)}.")

        

# def test_get_dependencies():
#     deps = get_dependencies("pdm")
#     print(deps)


if __name__ == "__main__":
    main()
    #test_get_dependencies()

