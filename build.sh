aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 396913712383.dkr.ecr.us-east-1.amazonaws.com
docker build -t brainfarms .
docker tag brainfarms:latest 396913712383.dkr.ecr.us-east-1.amazonaws.com/brainfarms:latest
docker push 396913712383.dkr.ecr.us-east-1.amazonaws.com/brainfarms:latest