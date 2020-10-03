#!/bin/sh

while true; do
  gsutil cp $1/* $2/;
  sleep 60;
done