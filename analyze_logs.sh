#!/bin/bash

# генерируем файл access.log как в условии (если уже есть, можно закомментировать)
cat <<EOL > access.log
192.168.1.1 - - [28/Jul/2024:12:34:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [28/Jul/2024:12:35:56 +0000] "POST /login HTTP/1.1" 200 567
192.168.1.3 - - [28/Jul/2024:12:36:56 +0000] "GET /home HTTP/1.1" 404 890
192.168.1.1 - - [28/Jul/2024:12:37:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.4 - - [28/Jul/2024:12:38:56 +0000] "GET /about HTTP/1.1" 200 432
192.168.1.2 - - [28/Jul/2024:12:39:56 +0000] "GET /index.html HTTP/1.1" 200 1234
EOL

# 1) Общее количество запросов
total_requests=$(wc -l < access.log)

# 2) Количество уникальных IP-адресов (строго с использованием awk)
unique_ips=$(awk '{print $1}' access.log | awk '!seen[$0]++{c++}END{print c+0}')

# 3) Количество запросов по методам (строго с использованием awk)
# извлекаем метод из первой кавычной группы: "METHOD URL HTTP/..."
# поле с кавычками обычно 6-е в стандартном формате, но надежнее извлечь между кавычками
methods_counts=$(awk -F'"' '{split($2,a," "); method=a[1]; if(method!="") m[method]++} END {for(k in m) print k, m[k]}' access.log)

# 4) Самый популярный URL (строго с использованием awk)
# извлечь URL из второй части в кавычках (поле $2) и взять второй элемент split -> URL
most_popular_url=$(awk -F'"' '{split($2,a," "); url=a[2]; if(url!="") u[url]++} END {max=0; best=""; for(k in u) if(u[k]>max){max=u[k]; best=k} if(best=="") print ""; else print best, max}' access.log)

# 5) Создать отчет report.txt
{
  echo "Отчет по access.log"
  echo "-------------------"
  echo "Общее количество запросов: $total_requests"
  echo "Количество уникальных IP-адресов: $unique_ips"
  echo ""
  echo "Количество запросов по методам:"
  # вывести методы в упорядоченном виде
  echo "$methods_counts" | sort -k2 -nr
  echo ""
  echo "Самый популярный URL и число обращений:"
  echo "$most_popular_url"
} > report.txt

# вывести кратко в консоль куда сохранён отчёт
echo "Отчёт сохранён в report.txt"
