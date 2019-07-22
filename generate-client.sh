dir=${PWD}
parentdir="$(dirname "$dir")"

branch=${1:-master}
version=${2:-v0.0.2}

docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli \
     generate  \
     -i https://raw.githubusercontent.com/mintproject/MINT-ModelCatalogIngestionAPI/$branch/model-catalog-$version.yaml \
     -g python  \
     -o /local/ \
     -c /local/openapi-config.json \
     --git-repo-id MINT-ModelCatalogAPI-client \
     --git-user-id mintproject  \
     --template-dir /local/.openapi-generator/template
