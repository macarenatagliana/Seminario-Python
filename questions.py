import random
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden
#que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, el el
#mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

puntaje = 0


# El usuario deberá contestar 3 preguntas
questions_to_ask = random.sample(list(zip(questions,answers,correct_answers_index)), k=3)

for question,answer,correct_answer_index in questions_to_ask:   
    print(question)
    
    for i, ans in enumerate(answer):
        print(f"{i + 1}. {ans}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es correcta
        # primero chequea q sea numeros
        if not(user_answer.isdigit() and int(user_answer) in range(1,5)):
            print("Respuesta no válida")
            exit(1)
        else:
            user_answer = int(user_answer) - 1

        if user_answer == correct_answer_index:
            print("¡Correcto!")
            puntaje +=1
            break
        else: 
            puntaje -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answer[correct_answer_index])
   
    # Se imprime un blanco al final de la pregunta
    print()
print(f"Su puntaje es: {puntaje}")
