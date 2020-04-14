api_doc_output=docs/index.html
api_blueprint_src=api-doc/api.apib
aglio_template=default
aglio_theme=cyborg

help:
	@echo 'help'
	@echo
	@echo 'start|stop|restart|gen-api-doc'

## API
start:
	docker-compose up -d --build api

stop:
	docker-compose down api

restart:
	docker restart api

## API doc
gen-api-doc:
	aglio -i $(api_blueprint_src) -o $(api_doc_output)\
	    --theme-template=$(aglio_template) \
	    --theme-variables=$(aglio_theme)

## Frontend
serve-static-test:
	./weave 8090 to $(shell pwd)/frontend/dist
