while getopts s:t: flag
do
    case "${flag}" in
        s) SECRET_KEY=${OPTARG};;
        t) SLACK_SUPPORT_CHANNEL=${OPTARG};;
    esac
done

docker-compose down

git pull origin master

export DJ_SECRET_KEY=$SECRET_KEY
export SLACK_SUPPORT_CHANNEL=$SLACK_SUPPORT_CHANNEL

docker-compose up --build -d django
