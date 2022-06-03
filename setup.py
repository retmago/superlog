from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='superlog',
    packages=['superlog'],
    version='0.6',
    license='LGPL v3',  # La licencia que tenga tu paquete
    description='Libreria para mostrar mayor cantidad de informacion en los logs de manera facil',
    author='jsilva95',
    author_email='jsilva2018.95@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
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