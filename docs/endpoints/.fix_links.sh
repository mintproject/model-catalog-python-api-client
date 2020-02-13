for file in $(ls *.md); do
    sed -i 's/README.md//g' $file
done
