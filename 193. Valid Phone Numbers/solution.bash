# Read from the file file.txt and output all valid phone numbers to stdout.
lines=""
file="file.txt"
regex='^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$'

while read line; do
    if [[ $line =~ $regex ]]; then
        echo "$line"
    fi
done < "$file"
