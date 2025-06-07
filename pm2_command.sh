pm2 start display_clock.py --name display_clock --interpreter python3
pm2 start get_forecast.py --cron '0 0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23 * * *' --name get_forecast --interpreter python3 --no-autorestart
pm2 start main.py --name main --interpreter python3
