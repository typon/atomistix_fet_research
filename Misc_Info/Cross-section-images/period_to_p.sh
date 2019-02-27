#!/bin/bash
for fname in *; do
  name="${fname%\.*}"
  extension="${fname#$name}"
  newname="${name//./p}"
  newfname="$newname""$extension"
  if [ "$fname" != "$newfname" ]; then
    echo mv "$fname" "$newfname"
    #mv "$fname" "$newfname"
  fi
done
