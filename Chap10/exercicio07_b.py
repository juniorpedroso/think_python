motocicletas = [
    ('Himalayan', 'Adventure'),
    ('Scram', 'Adventure'),
    ('Meteor', 'Cruiser'),
    ('Super Meteor', 'Cruiser'),
    ('Classic', 'Classic'),
    ('Goan', 'Classic'),
    ('Himalayan', 'Adventure')
]

# Cria um dicionário vazio
categorias = {}

for modelos, categoria in motocicletas:
    if categoria not in categorias:
        categorias[categoria] = []
    categorias[categoria].append(modelos)  # Sempre executa

print("🏍️  MOTOCICLETAS POR CATEGORIA")
print("=" * 40)

for categoria, modelos in categorias.items():
    print(f"\n📁 {categoria} ({len(modelos)} modelos):")
    for modelo in modelos:
        print(f"   • {modelo}")
