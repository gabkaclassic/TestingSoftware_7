ab -n 1000 -c 100 http://127.0.0.1:5000/calculator > tests_result/get_apache
echo "====================================="
ab -n 1000 -c 100 -T 'application/json' -p test_data/test_data.json http://127.0.0.1:5000/calculator > tests_result/post_apache
echo "====================================="
locust -f locust_performance_test.py --host=http://127.0.0.1:5000 --headless -u 100 -r 10 --run-time 1m > tests_result/locust


