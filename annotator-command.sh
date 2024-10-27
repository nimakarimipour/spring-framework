rm -f nullaway_error_*.txt
uuid=$(uuidgen)
./gradlew spring-expression:compileJava 2> error_temp.txt
head -n 4 error_temp.txt > nullaway_error_${uuid}.txt
grep -E '[0-9]+ errors' error_temp.txt | tail -n 1
rm error_temp.txt
