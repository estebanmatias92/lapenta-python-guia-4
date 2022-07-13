print(
    "1. Cree dos conjuntos de estudiantes, uno para aquellos que rindieron un examen y"
    + "\notro para aquellos que presentaron un proyecto. Puede usar cadenas para"
    + "\nrepresentar a los estudiantes, por ejemplo:"
)
print("")

examenes = {"Andres", "Katy", "Bety", "Emilio", "Susana"}
proyectos = {"Katy", "Emilio", "Ivan", "Eduardo"}

print("Exámenes:", examenes)
print("Proyectos:", proyectos)


print("\na. ¿Qué estudiantes realizaron el examen y presentaron un proyecto?")
print(
    f"Los estudiantes que realizaron el examen y presentaron el proyecto: {examenes.intersection(proyectos)}"
)

print("")
print("\n2. ¿Qué estudiantes solo rindieron el examen?")
print(f"Los estudiantes que solo rindieron el examen: {examenes.difference(proyectos)}")

print("")
print("3. ¿Qué estudiantes solo presentaron el proyecto?")
print(
    f"Los estudiantes que solo presentaron el proyecto: {proyectos.difference(examenes)}"
)


print(
    "\n4. Haga una lista de todos los estudiantes que tomaron uno (o ambos) del examen y el proyecto."
)
print(
    f"Los estudiantes que tomaron uno (o ambos) del examen y el proyecto: {examenes.union(proyectos)}"
)


print(
    "\n5. Haga una lista de todos los estudiantes que tomaron cualquiera (pero no ambos) del examen y el proyecto."
)
print(
    f"Los estudiantes que tomaron cualquiera (pero no ambos) del examen y el proyecto: {examenes.symmetric_difference(proyectos)}"
)
