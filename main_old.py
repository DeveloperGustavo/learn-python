# Biblioteca para capturar senhas
import getpass

# Biblioteca para controlar coisas do sistema operacional
import os

accounts_list = {
        '001' : {
            'password': '123456',
            'name': 'Gustavo',
            'value': 0,
            'admin': False
        },
        '002' : {
            'password': '321',
            'name': 'Joao',
            'value': 1000,
            'admin': False
        },
        '003' : {
            'password': '123',
            'name': 'Admin',
            'value': 1000,
            'admin': True
        }
    }

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5
}

while True:
    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")
    account_typed = input('Digita sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')
    print(account_typed)
    print(password_typed)

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("****************************************")
        print("*** School of Net - Caixa Eletrônico ***")
        print("****************************************")
        print("1 - Saldo")
        print("2 - Saque")
        
        if accounts_list[account_typed]['admin']:
            print("10 - Incluir cédulas")
        
        option_typed = input("Escolha uma das opções acima: ")
        
        if option_typed == '1':
            print('Seu saldo é %s' % accounts_list[account_typed]['value'])
        
        elif option_typed == '10' and accounts_list[account_typed]['admin']:
            amount_typed = input("Digite a quantidade de cédulas: ")
            money_bill_typed = input("Digite a cédula a ser incluída: ")
            money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
        elif option_typed == '2':
            value_typed = input('Digite o valor a ser sacado: ')
            
            if accounts_list[account_typed]['value'] < int(value_typed):
                print("Saldo insuficiente!")
            else:
                money_slips_user = {}
                value_int = int(value_typed)

                if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                    money_slips_user['100'] = value_int // 100
                    value_int = value_int - value_int // 100 * 100

                if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                    money_slips_user['50'] = value_int // 50
                    value_int = value_int - value_int // 50 * 50

                if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                    money_slips_user['20'] = value_int // 20
                    value_int = value_int - value_int // 20 * 20

                if value_int != 0:
                    print('O caixa não tem cédulas disponóveis para este valor.')
                else:
                    for money_bill in money_slips_user:
                        money_slips[money_bill] -= money_slips_user[money_bill]
                    accounts_list[account_typed]['value'] - int(value_typed)
                    print('Pegue as notas: ')
                    print(money_slips_user)
    else:
        print('Conta inválida')
    input('Pressione <ENTER> para continuar.')
    os.system('cls' if os.name == 'nt' else 'clear')