#separar el email de su dominio y guardar su dominio como un dominio

def main():
    email_input = input('input your email adress: ')
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    print('username: ',username)
    print('domain: ',domain)
    print('extention: ', extension)

main()