source /etc/profile
source ~/.bashrc
PATH="/home/xtj/notebook/xtj2020.github.io"
cd $PATH
currentdate=`/bin/date '+%Y%m%d%H%m'`
/usr/bin/git pull
/usr/bin/git add -A
/usr/bin/git commit -m $currentdate
/usr/bin/git push
/bin/date >>  /home/xtj/notebook/cron.txt
