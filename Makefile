IMAGE_NAME ?=  "web/mock-server"
ADDITIONAL_DOCKER_BUILD_ARGS ?=


image:
	docker build -f build/Dockerfile -t ${IMAGE_NAME} . --force-rm=True \
								 ${ADDITIONAL_DOCKER_BUILD_ARGS}

compose_config:
	docker-compose -f ./build/docker-compose.test.yml config

run:
	docker-compose -f ./build/docker-compose.yml up mock-server

test:
	@echo NO_TESTS_yet

push_to_registry: image
	docker push ${IMAGE_NAME}

vars:
	@echo IMAGE_NAME=${IMAGE_NAME}
	@echo ADDITIONAL_DOCKER_BUILD_ARGS=${ADDITIONAL_DOCKER_BUILD_ARGS}

clean:
	docker-compose -f ./build/docker-compose.yml down
	docker-compose -f ./build/docker-compose.yml rm -s -v -f
