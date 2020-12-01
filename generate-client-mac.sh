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

sed -i '.bk' 's~docs/~docs/endpoints/~g' README.md
rm README.md.bk
mv docs/[A-Z]*.md docs/endpoints/
pushd docs/endpoints/
for file in $(ls *.md); do
    sed -i '.bk' 's/README.md//g' $file
done
for file in $(ls *.bk); do
    rm $file
done
popd

pushd modelcatalog/models/
for file in $(ls *.py); do
    sed -i '.bk' 's/AnyOf[a-zA-Z]*/object/g' $file
done
for file in $(ls *.bk); do
    rm $file
done
popd
