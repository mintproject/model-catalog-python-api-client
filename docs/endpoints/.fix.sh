for file in $(ls *.md); do
    gsed -i 's/README.md//g' $file
done
