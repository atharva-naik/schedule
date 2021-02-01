##################################################################################################
#### Add to .bashrc #############################
#### Function to interpret terminal commands ####
##################################################################################################
abcd () {
    # ABsolute Change Directory 
    cd 
    cd "$1"
}

schd() {
    bold=$(tput bold)
    dir=$PWD
    abcd "schedule" # replace with absoulte path (after /home/user/)
    if [ "$#" -lt 1 ]; then
        python shell.py
        abcd "$dir"
    else
        command="python execute.py"
        case $1 in
            build)
                command="python installer.py";;
            show)
                echo -e "\033[44m displaying \033[0m"
                command="${command} --opcode show";;
            add)
                echo -e "\033[42m adding \033[0m"
                command="${command} --opcode add";;
            edit)
                if [ "$#" -lt 3 ]; then
                    echo -e "\033[31m${bold}Fatal: Need to supply event name and detail to be edited\033[0m"
                    abcd "$dir"      
                    return
                else
                    echo -e "\033[43m editing \033[0m"
                    command="${command} --opcode edit --name '$2' --datetime_info '$3'"
                fi
                ;;
            del)
                if [ "$#" -lt 2 ]; then
                    echo -e "\033[31m${bold}Fatal: Event to be deleted not specified\033[0m"
                    abcd "$dir"      
                    return
                else
                    echo -e "\033[41m deleting \033[0m" 
                    command="${command} --opcode delete --name '$2'"
                fi
                ;;
            info)
                echo -e "\033[44m About ${bold}schd \033[0m:"
                echo -e "This a schedule management package made by Atharva Naik (${bold}\033[4m\033[34mhttps://atharva-naik.github.io/\033[0m)"
                echo -e "Source code can be found at: (${bold}\033[4m\033[34mhttps://github.com/atharva-naik/schedule\033[0m)"
                echo -e "To host your schedule you need to have a github account and fork this repo. Your schedule will be shared at: (${bold}\033[4m\033[34mhttps://<username>.github.io/schedule\033[0m)"
                echo -e "\033[42m Running instructions \033[0m:"
                echo -e "\033[41m Debugging pointers \033[0m:"
                return 
                ;;
            -h)
                command="${command} --help";;
            -d|daily)
                echo -e "\033[44m displaying \033[0m"
                echo -e "\t\e[48;5;232m \e[32m${bold}daily schedule \e[m"
                command="${command} --schedule_type daily --opcode show";;    
            -w|weekly)
                echo -e "\033[44m displaying \033[0m"
                echo -e "\t\e[48;5;232m \e[32m${bold}weekly schedule \e[m"
                command="${command} --schedule_type weekly --opcode show";;    
            -m|monthly)
                echo -e "\033[44m displaying \033[0m"
                echo -e "\t\e[48;5;232m \e[32m${bold}monthly schedule \e[m"
                command="${command} --schedule_type monthly --opcode show";;                
            hol|holiday)
                echo -e "\033[44m displaying \033[0m"
                echo -e "\t\e[48;5;232m \e[32m${bold}holidays :) \e[m"
                command="${command} --schedule_type holidays --opcode show";;
            rem|remind)
                echo -e "\033[44m displaying \033[0m"
                echo -e "\t\e[48;5;232m \e[32m${bold}reminders :( \e[m"
                command="${command} --schedule_type reminders --opcode show";;
            *)
                echo -e "\033[31m${bold}Fatal: Unrecognised operation\033[0m"
                abcd "$dir"
                return 
                ;;
        esac
        if [ $1 != show -a $1 != add ]; then 
            eval $command 
            abcd "$dir"
            return
        fi
        if [[ "$#" -eq 1 ]]; then 
            echo -e "\033[31m${bold}Fatal: Missing schedule type\033[0m"
            abcd "$dir"
            return 
        fi
        case $2 in 
            -d|daily)
                command="${command} --schedule_type daily";;
            -w|weekly)
                command="${command} --schedule_type weekly";;
            -m|monthly)
                command="${command} --schedule_type monthly";;
            rem|remind)
                command="${command} --schedule_type reminders";;
            ho|holiday)
                command="${command} --schedule_type holidays";;
            *)
                echo -e "\033[31m${bold}Fatal: Invalid schedule type\033[0m"
                abcd "$dir"
                return
                ;;
        esac
        case $1 in 
            show)
                eval $command;;
            add)
                if [[ "$#" -lt 4 ]]; then 
                    echo -e "\033[31m${bold}Fatal: Missing mandatory arguments\033[0m"
                else
                    command="${command} --name '$3' --datetime_info '$4'"
                    eval $command
                fi     
                ;;
        esac
        abcd "$dir"
        return 
    fi
}
##################################################################################################