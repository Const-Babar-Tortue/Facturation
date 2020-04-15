api_doc_output=docs/index.html
api_blueprint_src=api-doc/api.apib
aglio_template=default
aglio_theme=cyborg

help:
	@echo 'help'
	@echo
	@echo 'start|stop|restart|gen-api-doc'

## API
api-start:
	docker-compose up -d --build api

api-stop:
	docker-compose down api

api-logs:
	docker-compose logs api

api-logs-follow:
	docker-compose logs -f api

# Run dev server with auto reload
vue-dev:
	cd frontend && yarn run dev

# Generate static website inside frontend/dist directory
vue-generate:
	cd frontend && yarn run generate

## API doc
gen-api-doc:
	aglio -i $(api_blueprint_src) -o $(api_doc_output)\
	    --theme-template=$(aglio_template) \
	    --theme-variables=$(aglio_theme)

# Serve static output
serve-static-test:
	./weave 8090 to $(shell pwd)/frontend/dist
