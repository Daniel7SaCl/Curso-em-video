def voto(ano_nascimento):
    from datetime import date
    ano_atual=date.today().year
    idade = ano_atual - ano_nascimento
    
    if idade < 16:
        return "NEGADO - Menor de idade"
    elif 16 <= idade < 18 or idade >= 70:
        return "OPCIONAL - Adolescente ou Idoso"
    else:
        return "OBRIGATÓRIO - Adulto"

ano_nascimento = int(input("Digite o ano de nascimento: "))
print(voto(ano_nascimento))
