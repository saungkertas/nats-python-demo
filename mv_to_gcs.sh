#!/bin/sh
#use e.g ./mv_to_gcs tmp gs://warpin-stream-demo-01/tmp
while true; do
  gsutil cp $1/* $2/;
  rm $1/*
  sleep 60;
done