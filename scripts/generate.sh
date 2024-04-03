#!/bin/bash

# Remove the existing 'seam' directory
rm -rf ./seam

# Generate SDK files
nextlove-sdk-generator generate python ./temp_sdk

# Move only the 'seam' folder
mv ./temp_sdk/seam ./seam

# Clean up the temporary SDK generation folder
rm -rf ./temp_sdk