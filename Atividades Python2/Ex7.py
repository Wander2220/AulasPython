def numero_conta_completo(numero_conta):
  
    soma_digitos = sum(int(digito) for digito in str(numero_conta))

  
    digito_verificador = soma_digitos % 10

 
    numero_completo = f"00{numero_conta}-{digito_verificador}"

    return numero_completo


n = 7314


conta_completa = numero_conta_completo(n)


print("Número de conta completo:", conta_completa)
