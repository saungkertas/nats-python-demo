#!/bin/sh

while true; do
  gsutil cp $1/* $2/;
  rm $1/*
  sleep 60;
done