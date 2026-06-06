saldo_disponible = input("Ingresa tu saldo disponible: ")

saldo_disponible = float(saldo_disponible)

# Aquí puedes agregar tus gastos específicos

transporte = 50.0
comida = 30.0
materiales = 25.0

total_gastos = transporte + comida + materiales

saldo_final = saldo_disponible - total_gastos

if saldo_final >= saldo_disponible * 0.2:
    print("Tienes suficiente saldo para tus gastos.")
    print("Tu saldo final después de los gastos es: ", saldo_final)
elif saldo_final == 0:
    print("Has agotado tu saldo completamente.")
elif saldo_final < 0:
    print("Has excedido tu saldo disponible.")
    print("Deberias revisar tus gastos y ajustarlos para no gastar más de lo que tienes.")
else:
    print("Tu saldo final después de los gastos es: ", saldo_final)
    print("Ten cuidado, tu saldo está por debajo del 20% de tu saldo disponible.")


