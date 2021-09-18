while getopts s: flag
do
    case "${flag}" in
        s) SECRET_KEY=${OPTARG};;
    esac
done

docker-compose down

git pull origin master

export DJ_SECRET_KEY=$SECRET_KEY
docker-compose up --build -d django
