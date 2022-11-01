class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        return f'Se ha eliminado el CD'

mi_cd = CD('Pink Floyd','The Wall', 24)
print(mi_cd.__str__())