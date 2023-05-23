#How to run it --> ./CheckImage.sh /your/path
if [$1 == ""]; then
    echo "You should run in this way --> ./CheckImage.sh /your/path"
    exit 1
fi
echo "Initializiating CheckImage.sh"
if [ -d "$1" ]; then
  ### Take action if $DIR exists ###
    #filelist= `ls $1/*`
    echo "${1} Folder exist --> Looking for images"
    
else
  ###  Control will jump here if $DIR does NOT exists ###
  echo "Error: ${1} not found. Cannot continue."
  exit 1
fi

for file in "$1"/*; do
        filename=$(basename "$file")
        ext="${filename##*.}"
        if [[ $ext == *"png"* ]] || [[ $ext == *"jpeg"* ]]; then
            echo "File $file is a figure"
        fi
    done;

