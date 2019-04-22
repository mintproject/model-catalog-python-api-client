dir=${PWD}
parentdir="$(dirname "$dir")"

docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli \
     generate  \
     -i https://raw.githubusercontent.com/mintproject/MINT-ModelCatalogIngestionAPI/master/model-catalog-v0.0.2.yaml \
     -g python  \
     -o /local/ \
     -c /local/openapi-config.json \
     --git-repo-id MINT-ModelCatalogAPI-client \
     --git-user-id mintproject  \
     --template-dir /local/.openapi-generator/template