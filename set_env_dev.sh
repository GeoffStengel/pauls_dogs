#!/bin/bash
export ENVIRONMENT_CONDITIONZ=development
export DATABASE_URL=sqlite:///C:/Users/greenhorn/Desktop/pauls_dogs_info/pauls_dogs/pd_proj/db.sqlite3
export ALLOWED_HOSTS=127.0.0.1,localhost
export SECRET_KEY='z#zv@ykr5@+p8=m3-%w@s%@@u)bw^nnusgo4h=5$bv!fa8q5iq'
export ADMIN=slinky/
export DEBUG_DEVELOPMENT=True
export DEBUG_PRODUCTION=False

# For production (optional locally)
#export DO_SPACES_KEY='paulsdogs-DigiOcean-key'
#export DO_SPACES_SECRET='hXmvY4nADL1QXxmISJJTpty5bkoWm3UVUAV0esv330w'
#export DO_SPACES_BUCKET_NAME='paulsdogs-digiocean-bucket'
#export DO_SPACES_REGION='nyc3'
#export DATABASE_URL='postgres://u2n7rg573kind7:p2d26fd7cb92e16e10482d4f31f7e9d7f0b04e17b414b84e5e24b7c4cee9e9b5f@ccj2ci9okh6spb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dfrl1h3eiedofj'
echo "Environment variables set successfully."
