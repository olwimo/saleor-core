. .env
docker build . -t "olwimo/saleor-core:0.0.1" --build-arg SECRET_KEY="${SECRET_KEY}" --build-arg MEDIA_URL="${MEDIA_URL}" --build-arg STATIC_URL="${STATIC_URL}"
docker tag "olwimo/saleor-core:0.0.1" "olwimo/saleor-core:latest"
docker push -a "olwimo/saleor-core"
