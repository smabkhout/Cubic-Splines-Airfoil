#!/bin/bash

# Lire tout le contenu du fichier dans une seule variable
content=$(cat file.txt)

# Remplacer les retours à la ligne pour que tout soit sur une seule ligne
content=$(echo "$content" | tr '\n' ' ')

# Ajouter un espace avant chaque crochet ouvrant pour bien séparer
content=$(echo "$content" | sed 's/\[/ \[/g')

# Découper par crochet ouvrant
IFS='[' read -ra blocks <<< "$content"

for block in "${blocks[@]}"; do
    if [[ -n "$block" ]]; then
        # Supprimer crochets fermants, puis remplacer espaces par virgules
        clean=$(echo "$block" | sed 's/]//g' | tr -s ' ' | sed 's/^\s*//;s/\s*$//' | tr ' ' ',')

        # Remettre les crochets
        echo "[$clean]"
    fi
done