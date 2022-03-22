while getopts s:t:a: flag
do
    case "${flag}" in
        s) SECRET_KEY=${OPTARG};;
        t) SLACK_BOT_TOKEN=${OPTARG};;
        a) AZ_SB_CONN_STR=${OPTARG};;
        k) KAFKA_HOST=${OPTARG};;
    esac
done

docker-compose down

git pull origin master

export DJ_SECRET_KEY=$SECRET_KEY
export SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN
export AZ_SB_CONN_STR=$AZ_SB_CONN_STR
export KAFKA_HOST=$KAFKA_HOST

docker-compose up --build -d django
