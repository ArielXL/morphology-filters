.PHONY: clean

NAME 	   	:= Filtros Morfológicos
VERSION		:= 1.0
DEVELOPER 	:= Ariel Plasencia Díaz
COPYRIGHT  	:= Copyright © 2021: $(DEVELOPERS)

run: ## Ejecuta nuestra propuesta de solucion
	python main.py

info: ## Muestra la descripcion de la tarea
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Muestra la version de la tarea
	@echo "$(NAME) v$(VERSION)"

install: ## Instala las dependencias requeridas
	pip3 install numpy
	pip3 install matplotlib
	pip3 install opencv-python

clean: ## Elimina archivos temporalmente
	rm -rf __pycache__/

help: ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
