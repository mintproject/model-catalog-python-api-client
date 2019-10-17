dir=${PWD}
parentdir="$(dirname "$dir")"

REPO_TAG=$1
FILE=https://raw.githubusercontent.com/mintproject/model-catalog-api/$REPO_TAG/model-catalog.yaml
docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.2 \
     generate  \
     -i $FILE \
     -g python  \
     -o /local/ \
     -c /local/openapi-config.json \
     --git-repo-id model-catalog-python-api-client \
     --git-user-id mintproject  \
     --template-dir /local/.openapi-generator/template
mv docs/ModelconfigurationApi.md docs/ModelConfigurationApi.md
