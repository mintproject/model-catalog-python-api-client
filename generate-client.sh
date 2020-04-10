set -e
dir=${PWD}
parentdir="$(dirname "$dir")"

REPO_TAG=$1
FILE=https://raw.githubusercontent.com/mintproject/model-catalog-api/$REPO_TAG/openapi.yaml
docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.2 \
     generate  \
     -i $FILE \
     -g python  \
     -o /local/ \
     -c /local/openapi-config.json \
     --git-repo-id model-catalog-python-api-client \
     --git-user-id mintproject  \

mv -f docs/ModelconfigurationApi.md docs/ModelConfigurationApi.md

sed -i 's~docs/~docs/endpoints/~g' README.md
mv docs/[A-Z]*.md docs/endpoints/
pushd docs/endpoints/
for file in $(ls *.md); do
    sed -i 's/README.md//g' $file
done
popd
