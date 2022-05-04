from setuptools import setup

setup(
    name='superlog',
    packages=['superlog'],
    version='0.4',
    license='LGPL v3',  # La licencia que tenga tu paquete
    description='Libreria para mostrar mayor cantidad de informacion en los logs de manera facil',
    author='jsilva95',
    author_email='jsilva2018.95@gmail.com',
    url='https://github.com/retmago/superlog.git',  # Usa la URL del repositorio de GitHub
    #download_url='https://github.com/retmago/superlog/archive/refs/heads/main.zip',
    # Te lo explico a continuación
    keywords='test example develop',  # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',
                 # Clasificadores de compatibilidad con versiones de Python para tu paquete
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)