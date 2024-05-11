
link="https://api.open-meteo.com/v1/forecast?latitude=54.9766&longitude=39.0444&current=temperature_2m&forecast_days=1"

data=$(curl $link)

echo $data | jq ".current .temperature_2m"
