while getopts s:t: flag
do
    case "${flag}" in
        s) SECRET_KEY=${OPTARG};;
        t) SLACK_BOT_TOKEN=${OPTARG};;
    esac
done

docker-compose down

git pull origin master

export DJ_SECRET_KEY=$SECRET_KEY
export SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN

docker-compose up --build -d django
