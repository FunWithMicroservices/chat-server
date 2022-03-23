while getopts s:t:a:k: flag
do
    case "${flag}" in
        a) APPLICATION=${OPTARG};;
        s) SECRET_KEY=${OPTARG};;
        t) SLACK_BOT_TOKEN=${OPTARG};;
        k) KAFKA_HOST=${OPTARG};;
    esac
done

docker-compose down

git pull origin master

export DJ_SECRET_KEY=$SECRET_KEY
export SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN
export KAFKA_HOST=$KAFKA_HOST

docker-compose up --build -d $APPLICATION
