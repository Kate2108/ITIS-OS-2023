
count=0
misses=0
total=0
answers=()

while true; do
    ((total++))
    answer=$((RANDOM % 10))
    echo -e "Step: $total\nPlease enter a number from 0 to 9 (q - quit): \c"

    read uinput
    if [ "$uinput" == "q" ]; then
        echo "Game over."
        exit 0
    fi

    if ! [[ "$uinput" =~ ^[0-9]$ ]]; then
        echo "Invalid input data. Digits 0-9 allow"
        continue
    fi

    if [ "$uinput" -eq "$answer" ]; then
        ((count++))
        result="Hit! My number: $answer"
        answers=("${answers[@]}" " \e[32m$uinput\e[0m")
    else
        ((misses++))
        result="Miss! My number: $answer"
        answers=("${answers[@]}" " \e[31m$uinput\e[0m")
    fi

    if [ "$total" -gt 0 ]; then
        count1=$(bc <<< "scale=2; ($count/$total) * 100")
        misses1=$(bc <<< "scale=2; ($misses/$total) * 100")
    else
        count1=0
        misses1=0
    fi

    if [ "${#answers[@]}" -gt 10 ]; then
        answers=("${answers[@]:1}")
    fi

    echo -e "$Result\nHit: ${count1}% Miss: ${misses1}%"
    echo -n "Numbers:"
    for num in "${answers[@]}"; do
        echo -en "num"
        if [ $num != "${answers[-1]}" ]; then
            echo -n " "
        fi
    done
    echo
done