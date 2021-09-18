while getopts s: flag
do
    case "${flag}" in
        s) SECRET_KEY=${OPTARG};;
    esac
done

docker-compose down

git pull origin master

docker-compose up --build -d django -e DJ_SECRET_KEY=$SECRET_KEY
